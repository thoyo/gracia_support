# gracia_support
Aquest programa converteix una llista de noms de persones i les seves corresponents adreces al barri de Gràcia, en xinxetes per a ser visualitzades en un mapa.

## Requeriments
Aconsegueix una API key de Google Maps per a la aplicació de Geocoding. Guarda-la en un fitxer api_key.txt en el mateix directori que el programa principal, main.py (ATENCIÓ: aquesta API és de pagament, fes un cop d'ull a les tarifes a la pàgina de suport).

## Instal·lació
Es recomana utilitzar entorns virtuals de Python

```
virtualenv -p python3.6 _env
source _env/bin/activate
(_env) pip install -r requirements.txt
```

## Execució
El programa llegeix els noms i les adreces del fitxer list.csv, i n'escriu per pantalla les coordenades corresponents. Pots enviar els resultats a un altre fitxer list_out.csv
```
(_env) python main.py > list_out.csv
```

El fitxer CSV resultant es pot convertir a KML per a visualitzar-lo a Google Earth amb la segent eina web:
https://www.convertcsv.com/csv-to-kml.htm

