# Get gas station prices by location

 ## **Content**
 1. [Introduction](#introduction)
     * [Info about data](#info-about-data)
     * [License info](#license-info)
 2. [Files description](#files-descriptions)
    * [File gas_stations_features.ipynb](#file-gasstationsfeaturesipynbgasstationsfeaturesipynb)
    * [File gas_stations_address.ipynb](#file-gasstationsaddressipynbgasstationsaddressipynb)
    * [File gas_stations_maps.ipynb](#file-gasstationsmapsipynbgasstationsmapsipynb)
    * [File gas_stations_mysql.ipynb](#file-gasstationsmysqlipynbgasstationsmysqlipynb)
 3. [Python scripts](#python-scripts)

<hr>

## **1. Introduction**

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

<hr>

## **2. Files descriptions**

### **File *[gas_stations_features.ipynb](gas_stations_features.ipynb)***

This file contents all ETL procedures for the project starting with data adquisition from [datos.gob.mx](https://datos.gob.mx/) portal, the processing data (fixing) and export file data as gas_prices_{date}.csv.

#### **Gas stations Dataframe**

![Gas stations dataframe](/images/final_dataframe.JPG)

### **File *[gas_stations_address.ipynb](/gas_stations_address.ipynb)***

This file use geopy library to get address from location coordinates (latitude, longitude) obtained by [gas_stations_features.ipynb](/gas_stations_features.ipynb), and export to [gas_address.csv](/export_files/gas_address_20220415_160024.csv). The data is following dataframe:

![Address dataframe](/images/address_dataframe.JPG)

### **File *[gas_stations_maps.ipynb](gas_stations_maps.ipynb)***

This file import csv file and create two maps:

First one shows gas stations around a 5 km distance from an specified location coordinates with some information about stations, including prices and a color code to locate the cheapest station. This map export to a [map.html](/export_files/map_20220418_230806.html) file.

#### **Map stations prices**

![Location map](/images/map_gas_locations.JPG)

Second map consist in a choropleth map using a geojson file for states in Mexico. The map shows you the average price of regular gas by state.

#### **Choropleth map with folium**

![Choropleth map folium](/images/choropleth_folium.JPG)

The exported file for folium map is [map_states.html](/export_files/map_states_20220418_213403.html)

#### **Choropleth map with plotly**

![Choropleth map plotly](/images/choropleth_plotly.JPG)

This map was not exported but you can find it in [gas_stations_maps.ipynb](/gas_stations_maps.ipynb)

### **File *[gas_stations_mysql.ipynb](/gas_stations_mysql.ipynb)***

This file creates a conection to mysql database and upload tables exported by previous scripts, after this process we get a database as follows:

![mysql tables](/images/mysql_tables.JPG)

<hr>

## **3. Python scripts**

Python scripts are for automate some process to implement an automatic process.

The script [get_gas_stations.py](/python_scripts/get_gas_stations.py) automate [gas_stations_features.ipynb](/gas_stations_features.ipynb) process and export csv file data and html map location [file](/export_files/map_20220418_230806.html).

The script [gas_functions.py](/python_scripts/gas_functions.py) contains the functions used in [get_gas_stations.py](/python_scripts/get_gas_stations.py).

The script [get_address.py](/python_scripts/get_address.py) automate all process in [gas_stations_address.ipynb](/gas_stations_address.ipynb)