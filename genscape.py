import pandas as pd
import requests
import io

ApiKey = "YOURAPIKEY"

genscape_storage = requests.get("https://api.genscape.com/oil-fundamentals/v1/crude-storage/weekly?region=NorthAmerica&revision=revised&format=csv",headers = {
                'Gen-Api-Key': str(ApiKey),})

genscape_storage = genscape_storage.content
genscape_storage = pd.read_csv(io.StringIO(genscape_storage.decode('utf-8')))

genscape_transportation = requests.get("https://api.genscape.com/oil-fundamentals/v1/crude-transportation/weekly?region=NorthAmerica&revision=revised&format=csv",headers = {
                'Gen-Api-Key': str(ApiKey),})

genscape_transportation = genscape_transportation.content
genscape_transportation = pd.read_csv(io.StringIO(genscape_transportation.decode('utf-8')))

