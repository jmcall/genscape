library(httr)
library(dplyr)
library(readr)
library(jsonlite)
library(rlist)
library(tidyr)
library(bigrquery)
library(Quandl)
library(eia)
library(lubridate)

# Genscape Storage Data

baseUrl = "https://api.genscape.com/oil-fundamentals/v1/crude-storage/weekly?region=NorthAmerica&revision=revised&format=csv"
api_key = "YOURAPIKEY"

genscape_storage <- GET(baseUrl, accept_json(),
                        add_headers(    'gen-api-key' = api_key,
                                        'cache-control' = 'no-cache'))

genscape_storage <- content(genscape_storage)