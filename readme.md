# Get gas station prices by location

## **Introduction**

This notebook extract gas and diesel prices for all stations in Mexico and create a dataframe and map locations.

The data was extracted from [datos.gob.mx](https://datos.gob.mx/) and its provided by CRE (Comisión Reguladora de Energía).

![Comisión reguladora de energía](/images/cre.JPG)

### **Info about data:**

[https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel](https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel)

The dataset consist in two XML file format, first contains attributes of gas stations services and second file contains prices for all gas stations services.

List of service stations, XML File [https://bit.ly/2V1Z3sm](https://bit.ly/2V1Z3sm)

List prices of gas and diesel for station, XML file [https://bit.ly/2JNcTha](https://bit.ly/2JNcTha)

### **License info:**

[https://datos.gob.mx/libreusomx](https://datos.gob.mx/libreusomx)

## **Files descriptions**

### File *gasolinas.ipynb*

This file contents all ETL procedures for the project starting with data adquisition from [datos.gob.mx](https://datos.gob.mx/) portal, the processing data and export file data, and creating map with gas stations locations.

#### **Gas stations Dataframe**

![Gas stations dataframe](/images/final_dataframe.JPG)

#### **Map stations**

![Map gas locations](/images/map_gas_locations.JPG)

### File *map_locations.ipynb*

This file just import csv file and create map with gas stations and export to an html file.

### File *get_gas_stations.py* and *gas_functions.py*

The file [get_gas_stations.py](/get_gas_stations.py) automate [gasolinas_aio.ipynb](/gasolinas_aio.ipynb) process and export csv file data and html map file.

The file [gas_functions.py](/gas_functions.py) contains the functions used in [get_gas_stations.py](/get_gas_stations.py).