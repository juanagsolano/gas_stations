import pandas as pd
from geopy.geocoders import Nominatim
from time import time
import numpy as np
import datetime

path_file = "export_files\gas_prices_20220415_160024.csv"
df = pd.read_csv(path_file)
df.set_index("place_id", inplace=True)

geolocator = Nominatim(user_agent="geoapiExercides")

[counter, wrongs] = [0,0]
indexs = df.dropna(subset=["latitude", "longitude"]).index
nplaces = len(indexs)

start_time = time()
estimate_time = 10

locations = []
for idx in indexs:

    # Get locations
    location = geolocator.reverse(
        str(df.loc[idx, "latitude"])+","+str(df.loc[idx, "longitude"]))

    # If location has address, append to list
    if location:
        location = location.raw["address"]
        location["place_id"] = idx
        locations.append(location)
    else:
        wrongs += 1

    counter += 1

    # Calculate estimate remaining time
    if counter % 10 == 0:
        estimate_time = np.round(
            (time()-start_time)/(3600*counter)*(nplaces-counter), 4)

    # Print status process
    print('\rProcessed places {}/{}. Remaining time: {:5.4f} h'.format(counter,
          nplaces, estimate_time), end='')

#Creating name of file based in gas_prices name
date_ex = path_file[-19:]

address_df = pd.DataFrame(locations)
address_df.set_index("place_id", inplace=True)
address_df.to_csv("export_files\gas_address_{}".format(date_ex))

print("Iteration process complete")
print("{} places has been processed with {} errors".format(counter-wrongs, wrongs))
print("Process end:", datetime.datetime.now())
print("Elapsed time: {} h.".format((time()-start_time)/3600))