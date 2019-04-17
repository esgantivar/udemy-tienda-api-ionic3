import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_text
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from jwt_auth.mixins import JSONWebTokenAuthMixin

from rest.models import Producto, Linea, Orden, DetalleOrden
from api.settings import SITE_URL


class AuthView(JSONWebTokenAuthMixin, View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LineasView(AuthView):
    def get(self, request):
        lineas = list(Linea.objects.all().values('id', 'linea', 'icono'))
        return JsonResponse(lineas, status=200, safe=False)


class ProductsView(AuthView):
    def get(self, request, page=1):
        p = Paginator(list(Producto.objects.all().values('codigo', 'producto')), 10)
        if page <= p.num_pages:
            return JsonResponse(p.page(page).object_list, safe=False)
        else:
            return JsonResponse([], safe=False)


class ProductByCategoryView(AuthView):
    def get(self, request, tipo, page=1):
        linea = Linea.objects.filter(id=tipo).first()
        if linea:
            p = Paginator(list(Producto.objects.filter(fk_linea_id=tipo).values('codigo', 'producto')), 10)
            if page <= p.num_pages:
                return JsonResponse(p.page(page).object_list, safe=False)
            else:
                return JsonResponse([], safe=False)
        else:
            return JsonResponse({'message': ''}, status=400)


class ProductSearchView(AuthView):
    def get(self, request, term=''):
        return JsonResponse(list(Producto.objects.filter(producto__icontains=term).values('codigo', 'producto')),
                            safe=False)


class ProductDetailView(AuthView):
    def get(self, request, codigo):
        product: Producto = Producto.objects.filter(codigo=codigo).first()
        if product:
            return JsonResponse({
                'codigo': product.codigo,
                'producto': product.producto,
                'linea': product.linea,
                'proveedor': product.proveedor,
                'descripcion': product.descripcion,
                'precio_compra': product.precio_compra,
                'imagen': f'{SITE_URL}{product.imagen.url}' if product.imagen else ''
            })
        else:
            return JsonResponse({}, status=404)


class OrdersView(AuthView):
    def get(self, request):
        orders = []
        for o in Orden.objects.filter(user=request.user):
            orders.append(o.to_dict)
        return JsonResponse(orders, safe=False, status=200)


class OrderView(AuthView):
    def get(self, request, order_id):
        order = Orden.objects.filter(id=order_id).first()
        if order:
            return JsonResponse({
                'id': order.id
            }, status=200)
        else:
            return JsonResponse({
            }, status=404)

    def delete(self, request, order_id):
        orden = Orden.objects.filter(user=request.user, id=order_id).first()
        if orden:
            orden.delete()
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({}, status=404)

    def post(self, request):
        data = json.loads(smart_text(request.body))
        items = data.get('items', [])
        if len(items) > 0:
            orden = Orden(
                user=request.user
            )
            orden.save()
            for item in items:
                p = Producto.objects.filter(codigo=item).first()
                if p:
                    DetalleOrden(
                        orden=orden,
                        producto=p
                    ).save()
            return JsonResponse({
                'orden_id': orden.id
            }, status=201)
        else:
            return JsonResponse({
                'error': 'No se han enviado items'
            }, status=400)
