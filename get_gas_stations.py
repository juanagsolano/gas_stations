"""
Get a csv file with all gas stations, attributes are: \n
[place_id,name,cree_id,latitude,longitude,regular,premium,diesel] and save csv file.

Plot an interactive map with top 100 nearest locations around a coordinates locations.

input: location = [latitude, longitude]
output: csv file and map in export files folder.
"""

# Librarys
import folium
import re
from datetime import datetime
import numpy as np
import pandas as pd
import requests
import xml.etree.ElementTree as et
from gas_functions import place_info
from gas_functions import price_info
from gas_functions import distances

#-------------------------------------------
# Select location
center = [25.69651, -100.31676]

# gas type ["regular","premium","diesel"]
gas_type = "regular"
#-------------------------------------------

# xml file information
url = "https://bit.ly/2V1Z3sm"

# Load xml file in memory
r = requests.get(url, allow_redirects=True)

# Using element tree to handle xml file
root = et.fromstring(r.content)

# Creating pandas dataframe for places
places_list = []
for i in range(len(root)):
    places_list.append(place_info(i,root))

places = pd.DataFrame(places_list)
places.set_index("place_id", inplace=True)
places.replace(0, np.nan, inplace=True)

# Drop 
places.loc[23393, ["latitude", "longitude"]] = [np.nan, np.nan]

# Fix location coordinates latitude <--> longitude
for index in places.index:
    # latitude domain [-90,90]
    # longitude domain [-180,180]
    if places.loc[index, "latitude"] > 90 or places.loc[index, "latitude"] < -90:
        longitud = places.loc[index, "latitude"].copy()
        latitud = places.loc[index, "longitude"].copy()

        places.loc[index, "longitude"] = longitud
        places.loc[index, "latitude"] = latitud

coordinates_fix_idx = places[["longitude"]][places["longitude"] > 50].index
places.loc[coordinates_fix_idx, "longitude"] *= -1

# Regquest gas prices
url = "https://bit.ly/2JNcTha"
r = requests.get(url, allow_redirects=True)
root = et.fromstring(r.content)

# Create pandas dataframe for prices
prices_list = []
for i in range(len(root)):
    prices_list.append(price_info(i,root))

prices = pd.DataFrame(prices_list)
prices.set_index("place_id", inplace=True)
prices = prices.groupby(prices.index).sum()
prices.replace(0.0, np.nan, inplace=True)

# Mergin dataframes
df = places.merge(prices, how="left", left_index=True, right_index=True)

#Creating name of file based in date
date_ex = re.sub("[-]", "", str(datetime.today()))
date_ex = re.sub("[ ]", "_", date_ex)
date_ex = re.sub("[:]", "", date_ex)
date_ex = date_ex[:-7]

# Export file to csv
df.to_csv("export_files\gas_prices_{}.csv".format(date_ex))

# Dropping nan coordinates to plot
df.dropna(subset=["latitude","longitude"],inplace=True)

# Create map object
map = folium.Map(
    location=[center[0], center[1]],
    zoom_start=13
)

distance_index = distances(center[0], center[1], df)

max_price = df.loc[distance_index, gas_type].max()
min_price = df.loc[distance_index, gas_type].min()

thresold1 = df.loc[distance_index, gas_type].quantile(0.25)
thresold2 = df.loc[distance_index, gas_type].quantile(0.75)

for idx in distance_index:
    price = df.loc[idx, gas_type]

    if price < thresold1 and price > min_price:
        set_color = "lightgreen"

    elif price >= thresold1 and price <= thresold2:
        set_color = "blue"

    elif price > thresold2 and price < max_price:
        set_color = "lightred"

    if price == min_price:
        set_color = "green"

    elif price == max_price:
        set_color = "red"

    folium.Marker(
        location=[df.loc[idx, "latitude"], df.loc[idx, "longitude"]],
        popup=df.loc[idx, "name"]+"\nRegular: "+str(df.loc[idx, "regular"])+"\nPremium: " +
        str(df.loc[idx, "premium"])+"\nDiesel: "+str(df.loc[idx, "diesel"]),
        icon=folium.Icon(color=set_color)
    ).add_to(map)

# Export html map file
map.save("export_files\map_{}.html".format(date_ex))