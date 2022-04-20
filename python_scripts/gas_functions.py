def place_info(idx: int,root):
    """
    Create a dictionary list from xml file with attributes.\n
    [place_id, name, cree_id, latitude, longitude]
    """
    place_dict = {}
    # Get place_id
    place_dict["place_id"] = int(root[idx].attrib.get("place_id"))

    # Get name station
    place_dict["name"] = root[idx][0].text

    # Get cree_id
    place_dict["cree_id"] = root[idx][1].text

    # Get location coordinates
    place_dict["latitude"] = float(root[idx][2][1].text)
    place_dict["longitude"] = float(root[idx][2][0].text)

    return place_dict

def price_info(idx: int,root):
    """
    The function extract features from an xml file.
    [regular, premium, diesel]
    """
    place_dict = {}
    # Get place_id
    place_dict["place_id"] = int(root[idx].attrib.get("place_id"))

    for gas_types in root[idx]:
        place_dict[gas_types.get("type")] = float(gas_types.text)

    return place_dict

def distances(latitude: float, longitude: float, df):
    import geopy.distance
    import pandas as pd
    distances = []
    for idx in df.index:
        distances.append(
            geopy.distance.geodesic(
                (latitude, longitude),
                (df.loc[idx, "latitude"], df.loc[idx, "longitude"])
            ).km
        )
    distances = pd.DataFrame(distances, columns=["distances"])
    distances["place_id"] = df.index
    distances.set_index("place_id", inplace=True)
    distances_idx = distances.sort_values(by="distances").index[1:100]
    return list(distances_idx)