import logging

from django.core.management import BaseCommand

from rest.models import Producto

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Bulk Productos'

    def handle(self, *args, **options):
        data = {
            "productos": [{
                "codigo": "S10_1678",
                "producto": "1969 Harley Davidson Ultimate Chopper",
                "linea": "Motorcycles",
                "fk_linea": "2",
                "proveedor": "Min Lin Diecast",
                "descripcion": "This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.",
                "precio_compra": "48810"
            },
                {
                    "codigo": "S10_1949",
                    "producto": "1952 Alpine Renault 1300",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "98580"
                },
                {
                    "codigo": "S10_2016",
                    "producto": "1996 Moto Guzzi 1100i",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts and baked enamel finish.",
                    "precio_compra": "68990"
                },
                {
                    "codigo": "S10_4698",
                    "producto": "2003 Harley-Davidson Eagle Drag Bike",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand\r\n, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine",
                    "precio_compra": "91020"
                },
                {
                    "codigo": "S10_4757",
                    "producto": "1972 Alfa Romeo GTA",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "85680"
                },
                {
                    "codigo": "S10_4962",
                    "producto": "1962 LanciaA Delta 16V",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "103420"
                },
                {
                    "codigo": "S12_1099",
                    "producto": "1968 Ford Mustang",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "Hood, doors and trunk all open to reveal highly detailed interior features. Steering wheel actually turns the front wheels. Color dark green.",
                    "precio_compra": "95340"
                },
                {
                    "codigo": "S12_1108",
                    "producto": "2001 Ferrari Enzo",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "95590"
                },
                {
                    "codigo": "S12_1666",
                    "producto": "1958 Setra Bus",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "Model features 30 windows, skylights & glare resistant glass, working steering system, original logos",
                    "precio_compra": "77900"
                },
                {
                    "codigo": "S12_2823",
                    "producto": "2002 Suzuki XREO",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Official logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts and baked enamel finish.",
                    "precio_compra": "66270"
                },
                {
                    "codigo": "S12_3148",
                    "producto": "1969 Corvair Monza",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "1:18 scale die-cast about 10' long doors open, hood opens, trunk opens and wheels roll",
                    "precio_compra": "89140"
                },
                {
                    "codigo": "S12_3380",
                    "producto": "1968 Dodge Charger",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "1:12 scale model of a 1968 Dodge Charger. Hood, doors and trunk all open to reveal highly detailed interior features. Steering wheel actually turns the front wheels. Color black",
                    "precio_compra": "75160"
                },
                {
                    "codigo": "S12_3891",
                    "producto": "1969 Ford Falcon",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "83050"
                },
                {
                    "codigo": "S12_3990",
                    "producto": "1970 Plymouth Hemi Cuda",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "Very detailed 1970 Plymouth Cuda model in 1:12 scale. The Cuda is generally accepted as one of the fastest original muscle cars from the 1970s. This model is a reproduction of one of the orginal 652 cars built in 1970. Red color.",
                    "precio_compra": "31920"
                },
                {
                    "codigo": "S12_4473",
                    "producto": "1957 Chevy Pickup",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Exoto Designs",
                    "descripcion": "1:12 scale die-cast about 20' long Hood opens, Rubber wheels",
                    "precio_compra": "55700"
                },
                {
                    "codigo": "S12_4675",
                    "producto": "1969 Dodge Charger",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "Detailed model of the 1969 Dodge Charger. This model includes finely detailed interior and exterior features. Painted in red and white.",
                    "precio_compra": "58730"
                },
                {
                    "codigo": "S18_1097",
                    "producto": "1940 Ford Pickup Truck",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "This model features soft rubber tires, working steering, rubber mud guards, authentic Ford logos, detailed undercarriage, opening doors and hood,  removable split rear gate, full size spare mounted in bed, detailed interior with opening glove box",
                    "precio_compra": "58330"
                },
                {
                    "codigo": "S18_1129",
                    "producto": "1993 Mazda RX-7",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "This model features, opening hood, opening doors, detailed engine, rear spoiler, opening trunk, working steering, tinted windows, baked enamel finish. Color red.",
                    "precio_compra": "83510"
                },
                {
                    "codigo": "S18_1342",
                    "producto": "1937 Lincoln Berline",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "Features opening engine cover, doors, trunk, and fuel filler cap. Color black",
                    "precio_compra": "60620"
                },
                {
                    "codigo": "S18_1367",
                    "producto": "1936 Mercedes-Benz 500K Special Roadster",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "This 1:18 scale replica is constructed of heavy die-cast metal and has all the features of the original: working doors and rumble seat, independent spring suspension, detailed interior, working steering system, and a bifold hood that reveals an engine so accurate that it even includes the wiring. All this is topped off with a baked enamel finish. Color white.",
                    "precio_compra": "24260"
                },
                {
                    "codigo": "S18_1589",
                    "producto": "1965 Aston Martin DB5",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Die-cast model of the silver 1965 Aston Martin DB5 in silver. This model includes full wire wheels and doors that open with fully detailed passenger compartment. In 1:18 scale, this model measures approximately 10 inches/20 cm long.",
                    "precio_compra": "65960"
                },
                {
                    "codigo": "S18_1662",
                    "producto": "1980s Black Hawk Helicopter",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "1:18 scale replica of actual Army's UH-60L BLACK HAWK Helicopter. 100% hand-assembled. Features rotating rotor blades, propeller blades and rubber wheels.",
                    "precio_compra": "77270"
                },
                {
                    "codigo": "S18_1749",
                    "producto": "1917 Grand Touring Sedan",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "This 1:18 scale replica of the 1917 Grand Touring car has all the features you would expect from museum quality reproductions: all four doors and bi-fold hood opening, detailed engine and instrument panel, chrome-look trim, and tufted upholstery, all topped off with a factory baked-enamel finish.",
                    "precio_compra": "86700"
                },
                {
                    "codigo": "S18_1889",
                    "producto": "1948 Porsche 356-A Roadster",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "This precision die-cast replica features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "53900"
                },
                {
                    "codigo": "S18_1984",
                    "producto": "1995 Honda Civic",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "This model features, opening hood, opening doors, detailed engine, rear spoiler, opening trunk, working steering, tinted windows, baked enamel finish. Color yellow.",
                    "precio_compra": "93890"
                },
                {
                    "codigo": "S18_2238",
                    "producto": "1998 Chrysler Plymouth Prowler",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "101510"
                },
                {
                    "codigo": "S18_2248",
                    "producto": "1911 Ford Town Car",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "Features opening hood, opening doors, opening trunk, wide white wall tires, front door arm rests, working steering system.",
                    "precio_compra": "33300"
                },
                {
                    "codigo": "S18_2319",
                    "producto": "1964 Mercedes Tour Bus",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Exact replica. 100+ parts. working steering system, original logos",
                    "precio_compra": "74860"
                },
                {
                    "codigo": "S18_2325",
                    "producto": "1932 Model A Ford J-Coupe",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "This model features grille-mounted chrome horn, lift-up louvered hood, fold-down rumble seat, working steering system, chrome-covered spare, opening doors, detailed and wired engine",
                    "precio_compra": "58480"
                },
                {
                    "codigo": "S18_2432",
                    "producto": "1926 Ford Fire Engine",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "Gleaming red handsome appearance. Everything is here the fire hoses, ladder, axes, bells, lanterns, ready to fight any inferno.",
                    "precio_compra": "24920"
                },
                {
                    "codigo": "S18_2581",
                    "producto": "P-51-D Mustang",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "Has retractable wheels and comes with a stand",
                    "precio_compra": "49000"
                },
                {
                    "codigo": "S18_2625",
                    "producto": "1936 Harley Davidson El Knucklehead",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "Intricately detailed with chrome accents and trim, official die-struck logos and baked enamel finish.",
                    "precio_compra": "24230"
                },
                {
                    "codigo": "S18_2795",
                    "producto": "1928 Mercedes-Benz SSK",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "This 1:18 replica features grille-mounted chrome horn, lift-up louvered hood, fold-down rumble seat, working steering system, chrome-covered spare, opening doors, detailed and wired engine. Color black.",
                    "precio_compra": "72560"
                },
                {
                    "codigo": "S18_2870",
                    "producto": "1999 Indy 500 Monte Carlo SS",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "Features include opening and closing doors. Color: Red",
                    "precio_compra": "56760"
                },
                {
                    "codigo": "S18_2949",
                    "producto": "1913 Ford Model T Speedster",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "This 250 part reproduction includes moving handbrakes, clutch, throttle and foot pedals, squeezable horn, detailed wired engine, removable water, gas, and oil cans, pivoting monocle windshield, all topped with a baked enamel red finish. Each replica comes with an Owners Title and Certificate of Authenticity. Color red.",
                    "precio_compra": "60780"
                },
                {
                    "codigo": "S18_2957",
                    "producto": "1934 Ford V8 Coupe",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "Chrome Trim, Chrome Grille, Opening Hood, Opening Doors, Opening Trunk, Detailed Engine, Working Steering System",
                    "precio_compra": "34350"
                },
                {
                    "codigo": "S18_3029",
                    "producto": "1999 Yamaha Speed Boat",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "Exact replica. Wood and Metal. Many extras including rigging, long boats, pilot house, anchors, etc. Comes with three masts, all square-rigged.",
                    "precio_compra": "51610"
                },
                {
                    "codigo": "S18_3136",
                    "producto": "18th Century Vintage Horse Carriage",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "Hand crafted diecast-like metal horse carriage is re-created in about 1:18 scale of antique horse carriage. This antique style metal Stagecoach is all hand-assembled with many different parts.\r\n\r\nThis collectible metal horse carriage is painted in classic Red, and features turning steering wheel and is entirely hand-finished.",
                    "precio_compra": "60740"
                },
                {
                    "codigo": "S18_3140",
                    "producto": "1903 Ford Model A",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Features opening trunk,  working steering system",
                    "precio_compra": "68300"
                },
                {
                    "codigo": "S18_3232",
                    "producto": "1992 Ferrari 360 Spider red",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "his replica features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "77900"
                },
                {
                    "codigo": "S18_3233",
                    "producto": "1985 Toyota Supra",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "This model features soft rubber tires, working steering, rubber mud guards, authentic Ford logos, detailed undercarriage, opening doors and hood, removable split rear gate, full size spare mounted in bed, detailed interior with opening glove box",
                    "precio_compra": "57010"
                },
                {
                    "codigo": "S18_3259",
                    "producto": "Collectable Wooden Train",
                    "linea": "Trains",
                    "fk_linea": "7",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "Hand crafted wooden toy train set is in about 1:18 scale, 25 inches in total length including 2 additional carts, of actual vintage train. This antique style wooden toy train model set is all hand-assembled with 100% wood.",
                    "precio_compra": "67560"
                },
                {
                    "codigo": "S18_3278",
                    "producto": "1969 Dodge Super Bee",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "This replica features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "49050"
                },
                {
                    "codigo": "S18_3320",
                    "producto": "1917 Maxwell Touring Car",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Exoto Designs",
                    "descripcion": "Features Gold Trim, Full Size Spare Tire, Chrome Trim, Chrome Grille, Opening Hood, Opening Doors, Opening Trunk, Detailed Engine, Working Steering System",
                    "precio_compra": "57540"
                },
                {
                    "codigo": "S18_3482",
                    "producto": "1976 Ford Gran Torino",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "Highly detailed 1976 Ford Gran Torino 'Starsky and Hutch' diecast model. Very well constructed and painted in red and white patterns.",
                    "precio_compra": "73490"
                },
                {
                    "codigo": "S18_3685",
                    "producto": "1948 Porsche Type 356 Roadster",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "This model features working front and rear suspension on accurately replicated and actuating shock absorbers as well as opening engine cover, rear stabilizer flap,  and 4 opening doors.",
                    "precio_compra": "62160"
                },
                {
                    "codigo": "S18_3782",
                    "producto": "1957 Vespa GS150",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "Features rotating wheels , working kick stand. Comes with stand.",
                    "precio_compra": "32950"
                },
                {
                    "codigo": "S18_3856",
                    "producto": "1941 Chevrolet Special Deluxe Cabriolet",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Exoto Designs",
                    "descripcion": "Features opening hood, opening doors, opening trunk, wide white wall tires, front door arm rests, working steering system, leather upholstery. Color black.",
                    "precio_compra": "64580"
                },
                {
                    "codigo": "S18_4027",
                    "producto": "1970 Triumph Spitfire",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "Features include opening and closing doors. Color: White.",
                    "precio_compra": "91920"
                },
                {
                    "codigo": "S18_4409",
                    "producto": "1932 Alfa Romeo 8C2300 Spider Sport",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Exoto Designs",
                    "descripcion": "This 1:18 scale precision die cast replica features the 6 front headlights of the original, plus a detailed version of the 142 horsepower straight 8 engine, dual spares and their famous comprehensive dashboard. Color black.",
                    "precio_compra": "43260"
                },
                {
                    "codigo": "S18_4522",
                    "producto": "1904 Buick Runabout",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Exoto Designs",
                    "descripcion": "Features opening trunk,  working steering system",
                    "precio_compra": "52660"
                },
                {
                    "codigo": "S18_4600",
                    "producto": "1940s Ford truck",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "This 1940s Ford Pick-Up truck is re-created in 1:18 scale of original 1940s Ford truck. This antique style metal 1940s Ford Flatbed truck is all hand-assembled. This collectible 1940's Pick-Up truck is painted in classic dark green color, and features rotating wheels.",
                    "precio_compra": "84760"
                },
                {
                    "codigo": "S18_4668",
                    "producto": "1939 Cadillac Limousine",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "Features completely detailed interior including Velvet flocked drapes,deluxe wood grain floor, and a wood grain casket with seperate chrome handles",
                    "precio_compra": "23140"
                },
                {
                    "codigo": "S18_4721",
                    "producto": "1957 Corvette Convertible",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "1957 die cast Corvette Convertible in Roman Red with white sides and whitewall tires. 1:18 scale quality die-cast with detailed engine and underbvody. Now you can own The Classic Corvette.",
                    "precio_compra": "69930"
                },
                {
                    "codigo": "S18_4933",
                    "producto": "1957 Ford Thunderbird",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "This 1:18 scale precision die-cast replica, with its optional porthole hardtop and factory baked-enamel Thunderbird Bronze finish, is a 100% accurate rendition of this American classic.",
                    "precio_compra": "34210"
                },
                {
                    "codigo": "S24_1046",
                    "producto": "1970 Chevy Chevelle SS 454",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "This model features rotating wheels, working streering system and opening doors. All parts are particularly delicate due to their precise scale and require special care and attention. It should not be picked up by the doors, roof, hood or trunk.",
                    "precio_compra": "49240"
                },
                {
                    "codigo": "S24_1444",
                    "producto": "1970 Dodge Coronet",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "1:24 scale die-cast about 18' long doors open, hood opens and rubber wheels",
                    "precio_compra": "32370"
                },
                {
                    "codigo": "S24_1578",
                    "producto": "1997 BMW R 1100 S",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "Detailed scale replica with working suspension and constructed from over 70 parts",
                    "precio_compra": "60860"
                },
                {
                    "codigo": "S24_1628",
                    "producto": "1966 Shelby Cobra 427 S/C",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "This diecast model of the 1966 Shelby Cobra 427 S/C includes many authentic details and operating parts. The 1:24 scale model of this iconic lighweight sports car from the 1960s comes in silver and it's own display case.",
                    "precio_compra": "29180"
                },
                {
                    "codigo": "S24_1785",
                    "producto": "1928 British Royal Navy Airplane",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Official logos and insignias",
                    "precio_compra": "66740"
                },
                {
                    "codigo": "S24_1937",
                    "producto": "1939 Chevrolet Deluxe Coupe",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "This 1:24 scale die-cast replica of the 1939 Chevrolet Deluxe Coupe has the same classy look as the original. Features opening trunk, hood and doors and a showroom quality baked enamel finish.",
                    "precio_compra": "22570"
                },
                {
                    "codigo": "S24_2000",
                    "producto": "1960 BSA Gold Star DBD34",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "Detailed scale replica with working suspension and constructed from over 70 parts",
                    "precio_compra": "37320"
                },
                {
                    "codigo": "S24_2011",
                    "producto": "18th century schooner",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "All wood with canvas sails. Many extras including rigging, long boats, pilot house, anchors, etc. Comes with 4 masts, all square-rigged.",
                    "precio_compra": "82340"
                },
                {
                    "codigo": "S24_2022",
                    "producto": "1938 Cadillac V-16 Presidential Limousine",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "This 1:24 scale precision die cast replica of the 1938 Cadillac V-16 Presidential Limousine has all the details of the original, from the flags on the front to an opening back seat compartment complete with telephone and rifle. Features factory baked-enamel black finish, hood goddess ornament, working jump seats.",
                    "precio_compra": "20610"
                },
                {
                    "codigo": "S24_2300",
                    "producto": "1962 Volkswagen Microbus",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "This 1:18 scale die cast replica of the 1962 Microbus is loaded with features: A working steering system, opening front doors and tailgate, and famous two-tone factory baked enamel finish, are all topped of by the sliding, real fabric, sunroof.",
                    "precio_compra": "61340"
                },
                {
                    "codigo": "S24_2360",
                    "producto": "1982 Ducati 900 Monster",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "Features two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand",
                    "precio_compra": "47100"
                },
                {
                    "codigo": "S24_2766",
                    "producto": "1949 Jaguar XK 120",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Precision-engineered from original Jaguar specification in perfect scale ratio. Features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "47250"
                },
                {
                    "codigo": "S24_2840",
                    "producto": "1958 Chevy Corvette Limited Edition",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "The operating parts of this 1958 Chevy Corvette Limited Edition are particularly delicate due to their precise scale and require special care and attention. Features rotating wheels, working streering, opening doors and trunk. Color dark green.",
                    "precio_compra": "15910"
                },
                {
                    "codigo": "S24_2841",
                    "producto": "1900s Vintage Bi-Plane",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "Hand crafted diecast-like metal bi-plane is re-created in about 1:24 scale of antique pioneer airplane. All hand-assembled with many different parts. Hand-painted in classic yellow and features correct markings of original airplane.",
                    "precio_compra": "34250"
                },
                {
                    "codigo": "S24_2887",
                    "producto": "1952 Citroen-15CV",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Exoto Designs",
                    "descripcion": "Precision crafted hand-assembled 1:18 scale reproduction of the 1952 15CV, with its independent spring suspension, working steering system, opening doors and hood, detailed engine and instrument panel, all topped of with a factory fresh baked enamel finish.",
                    "precio_compra": "72820"
                },
                {
                    "codigo": "S24_2972",
                    "producto": "1982 Lamborghini Diablo",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "This replica features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "16240"
                },
                {
                    "codigo": "S24_3151",
                    "producto": "1912 Ford Model T Delivery Wagon",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "This model features chrome trim and grille, opening hood, opening doors, opening trunk, detailed engine, working steering system. Color white.",
                    "precio_compra": "46910"
                },
                {
                    "codigo": "S24_3191",
                    "producto": "1969 Chevrolet Camaro Z28",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Exoto Designs",
                    "descripcion": "1969 Z/28 Chevy Camaro 1:24 scale replica. The operating parts of this limited edition 1:24 scale diecast model car 1969 Chevy Camaro Z28- hood, trunk, wheels, streering, suspension and doors- are particularly delicate due to their precise scale and require special care and attention.",
                    "precio_compra": "50510"
                },
                {
                    "codigo": "S24_3371",
                    "producto": "1971 Alpine Renault 1600s",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "This 1971 Alpine Renault 1600s replica Features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "38580"
                },
                {
                    "codigo": "S24_3420",
                    "producto": "1937 Horch 930V Limousine",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "Features opening hood, opening doors, opening trunk, wide white wall tires, front door arm rests, working steering system",
                    "precio_compra": "26300"
                },
                {
                    "codigo": "S24_3432",
                    "producto": "2002 Chevy Corvette",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "The operating parts of this limited edition Diecast 2002 Chevy Corvette 50th Anniversary Pace car Limited Edition are particularly delicate due to their precise scale and require special care and attention. Features rotating wheels, poseable streering, opening doors and trunk.",
                    "precio_compra": "62110"
                },
                {
                    "codigo": "S24_3816",
                    "producto": "1940 Ford Delivery Sedan",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "Chrome Trim, Chrome Grille, Opening Hood, Opening Doors, Opening Trunk, Detailed Engine, Working Steering System. Color black.",
                    "precio_compra": "48640"
                },
                {
                    "codigo": "S24_3856",
                    "producto": "1956 Porsche 356A Coupe",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.",
                    "precio_compra": "98300"
                },
                {
                    "codigo": "S24_3949",
                    "producto": "Corsair F4U ( Bird Cage)",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Has retractable wheels and comes with a stand. Official logos and insignias.",
                    "precio_compra": "29340"
                },
                {
                    "codigo": "S24_3969",
                    "producto": "1936 Mercedes Benz 500k Roadster",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "This model features grille-mounted chrome horn, lift-up louvered hood, fold-down rumble seat, working steering system and rubber wheels. Color black.",
                    "precio_compra": "21750"
                },
                {
                    "codigo": "S24_4048",
                    "producto": "1992 Porsche Cayenne Turbo Silver",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Exoto Designs",
                    "descripcion": "This replica features opening doors, superb detail and craftsmanship, working steering system, opening forward compartment, opening rear trunk with removable spare, 4 wheel independent spring suspension as well as factory baked enamel finish.",
                    "precio_compra": "69780"
                },
                {
                    "codigo": "S24_4258",
                    "producto": "1936 Chrysler Airflow",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Features opening trunk,  working steering system. Color dark green.",
                    "precio_compra": "57460"
                },
                {
                    "codigo": "S24_4278",
                    "producto": "1900s Vintage Tri-Plane",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Hand crafted diecast-like metal Triplane is Re-created in about 1:24 scale of antique pioneer airplane. This antique style metal triplane is all hand-assembled with many different parts.",
                    "precio_compra": "36230"
                },
                {
                    "codigo": "S24_4620",
                    "producto": "1961 Chevrolet Impala",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "This 1:18 scale precision die-cast reproduction of the 1961 Chevrolet Impala has all the features-doors, hood and trunk that open; detailed 409 cubic-inch engine; chrome dashboard and stick shift, two-tone interior; working steering system; all topped of with a factory baked-enamel finish.",
                    "precio_compra": "32330"
                },
                {
                    "codigo": "S32_1268",
                    "producto": "1980‚Äôs GM Manhattan Express",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "This 1980‚Äôs era new look Manhattan express is still active, running from the Bronx to mid-town Manhattan. Has 35 opeining windows and working lights. Needs a battery.",
                    "precio_compra": "53930"
                },
                {
                    "codigo": "S32_1374",
                    "producto": "1997 BMW F650 ST",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Exoto Designs",
                    "descripcion": "Features official die-struck logos and baked enamel finish. Comes with stand.",
                    "precio_compra": "66920"
                },
                {
                    "codigo": "S32_2206",
                    "producto": "1982 Ducati 996 R",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "Features rotating wheels , working kick stand. Comes with stand.",
                    "precio_compra": "24140"
                },
                {
                    "codigo": "S32_2509",
                    "producto": "1954 Greyhound Scenicruiser",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "Model features bi-level seating, 50 windows, skylights & glare resistant glass, working steering system, original logos",
                    "precio_compra": "25980"
                },
                {
                    "codigo": "S32_3207",
                    "producto": "1950's Chicago Surface Lines Streetcar",
                    "linea": "Trains",
                    "fk_linea": "7",
                    "proveedor": "Gearbox Collectibles",
                    "descripcion": "This streetcar is a joy to see. It has 80 separate windows, electric wire guides, detailed interiors with seats, poles and drivers controls, rolling and turning wheel assemblies, plus authentic factory baked-enamel finishes (Green Hornet for Chicago and Cream and Crimson for Boston).",
                    "precio_compra": "26720"
                },
                {
                    "codigo": "S32_3522",
                    "producto": "1996 Peterbilt 379 Stake Bed with Outrigger",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "This model features, opening doors, detailed engine, working steering, tinted windows, detailed interior, die-struck logos, removable stakes operating outriggers, detachable second trailer, functioning 360-degree self loader, precision molded resin trailer and trim, baked enamel finish on cab",
                    "precio_compra": "33610"
                },
                {
                    "codigo": "S32_4289",
                    "producto": "1928 Ford Phaeton Deluxe",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "This model features grille-mounted chrome horn, lift-up louvered hood, fold-down rumble seat, working steering system",
                    "precio_compra": "33020"
                },
                {
                    "codigo": "S32_4485",
                    "producto": "1974 Ducati 350 Mk3 Desmo",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "This model features two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand",
                    "precio_compra": "56130"
                },
                {
                    "codigo": "S50_1341",
                    "producto": "1930 Buick Marquette Phaeton",
                    "linea": "Vintage Cars",
                    "fk_linea": "6",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "Features opening trunk,  working steering system",
                    "precio_compra": "27060"
                },
                {
                    "codigo": "S50_1392",
                    "producto": "Diamond T620 Semi-Skirted Tanker",
                    "linea": "Trucks and Buses",
                    "fk_linea": "5",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "This limited edition model is licensed and perfectly scaled for Lionel Trains. The Diamond T620 has been produced in solid precision diecast and painted with a fire baked enamel finish. It comes with a removable tanker and is a perfect model to add authenticity to your static train or car layout or to just have on display.",
                    "precio_compra": "68290"
                },
                {
                    "codigo": "S50_1514",
                    "producto": "1962 City of Detroit Streetcar",
                    "linea": "Trains",
                    "fk_linea": "7",
                    "proveedor": "Classic Metal Creations",
                    "descripcion": "This streetcar is a joy to see. It has 99 separate windows, electric wire guides, detailed interiors with seats, poles and drivers controls, rolling and turning wheel assemblies, plus authentic factory baked-enamel finishes (Green Hornet for Chicago and Cream and Crimson for Boston).",
                    "precio_compra": "37490"
                },
                {
                    "codigo": "S50_4713",
                    "producto": "2002 Yamaha YZR M1",
                    "linea": "Motorcycles",
                    "fk_linea": "2",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "Features rotating wheels , working kick stand. Comes with stand.",
                    "precio_compra": "34170"
                },
                {
                    "codigo": "S700_1138",
                    "producto": "The Schooner Bluenose",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Autoart Studio Design",
                    "descripcion": "All wood with canvas sails. Measures 31 1/2 inches in Length, 22 inches High and 4 3/4 inches Wide. Many extras.\r\nThe schooner Bluenose was built in Nova Scotia in 1921 to fish the rough waters off the coast of Newfoundland. Because of the Bluenose racing prowess she became the pride of all Canadians. Still featured on stamps and the Canadian dime, the Bluenose was lost off Haiti in 1946.",
                    "precio_compra": "34000"
                },
                {
                    "codigo": "S700_1691",
                    "producto": "American Airlines: B767-300",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Min Lin Diecast",
                    "descripcion": "Exact replia with official logos and insignias and retractable wheels",
                    "precio_compra": "51150"
                },
                {
                    "codigo": "S700_1938",
                    "producto": "The Mayflower",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Studio M Art Models",
                    "descripcion": "Measures 31 1/2 inches Long x 25 1/2 inches High x 10 5/8 inches Wide\r\nAll wood with canvas sail. Extras include long boats, rigging, ladders, railing, anchors, side cannons, hand painted, etc.",
                    "precio_compra": "43300"
                },
                {
                    "codigo": "S700_2047",
                    "producto": "HMS Bounty",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Measures 30 inches Long x 27 1/2 inches High x 4 3/4 inches Wide. \r\nMany extras including rigging, long boats, pilot house, anchors, etc. Comes with three masts, all square-rigged.",
                    "precio_compra": "39830"
                },
                {
                    "codigo": "S700_2466",
                    "producto": "America West Airlines B757-200",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "Official logos and insignias. Working steering system. Rotating jet engines",
                    "precio_compra": "68800"
                },
                {
                    "codigo": "S700_2610",
                    "producto": "The USS Constitution Ship",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Red Start Diecast",
                    "descripcion": "All wood with canvas sails. Measures 31 1/2' Length x 22 3/8' High x 8 1/4' Width. Extras include 4 boats on deck, sea sprite on bow, anchors, copper railing, pilot houses, etc.",
                    "precio_compra": "33970"
                },
                {
                    "codigo": "S700_2824",
                    "producto": "1982 Camaro Z28",
                    "linea": "Classic Cars",
                    "fk_linea": "1",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "Features include opening and closing doors. Color: White. \r\nMeasures approximately 9 1/2' Long.",
                    "precio_compra": "46530"
                },
                {
                    "codigo": "S700_2834",
                    "producto": "ATA: B757-300",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Highway 66 Mini Classics",
                    "descripcion": "Exact replia with official logos and insignias and retractable wheels",
                    "precio_compra": "59330"
                },
                {
                    "codigo": "S700_3167",
                    "producto": "F/A 18 Hornet 1/72",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "10' Wingspan with retractable landing gears.Comes with pilot",
                    "precio_compra": "54400"
                },
                {
                    "codigo": "S700_3505",
                    "producto": "The Titanic",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Carousel DieCast Legends",
                    "descripcion": "Completed model measures 19 1/2 inches long, 9 inches high, 3inches wide and is in barn red/black. All wood and metal.",
                    "precio_compra": "51090"
                },
                {
                    "codigo": "S700_3962",
                    "producto": "The Queen Mary",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Welly Diecast Productions",
                    "descripcion": "Exact replica. Wood and Metal. Many extras including rigging, long boats, pilot house, anchors, etc. Comes with three masts, all square-rigged.",
                    "precio_compra": "53630"
                },
                {
                    "codigo": "S700_4002",
                    "producto": "American Airlines: MD-11S",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Second Gear Diecast",
                    "descripcion": "Polished finish. Exact replia with official logos and insignias and retractable wheels",
                    "precio_compra": "36270"
                },
                {
                    "codigo": "S72_1253",
                    "producto": "Boeing X-32A JSF",
                    "linea": "Planes",
                    "fk_linea": "3",
                    "proveedor": "Motor City Art Classics",
                    "descripcion": "10' Wingspan with retractable landing gears.Comes with pilot",
                    "precio_compra": "32770"
                },
                {
                    "codigo": "S72_3212",
                    "producto": "Pont Yacht",
                    "linea": "Ships",
                    "fk_linea": "4",
                    "proveedor": "Unimax Art Galleries",
                    "descripcion": "Measures 38 inches Long x 33 3/4 inches High. Includes a stand.\r\nMany extras including rigging, long boats, pilot house, anchors, etc. Comes with 2 masts, all square-rigged",
                    "precio_compra": "33300"
                }]
        }

        for item in data.get('productos'):
            Producto(
                codigo=item.get('codigo'),
                producto=item.get('producto'),
                linea=item.get('linea'),
                fk_linea_id=int(item.get('fk_linea')),
                proveedor=item.get('proveedor'),
                descripcion=item.get('descripcion'),
                precio_compra=float(item.get('precio_compra'))
            ).save()
