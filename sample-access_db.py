import pandas as pd
import json
import csv
from dotenv import dotenv_values
from google.oauth2 import service_account

import pygsheets

config = dotenv_values(".env")
with open("service_account.json") as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

client = pygsheets.authorize(service_account_file="service_account.json")

spreadsheet_url = config["URL"]
sheet_data = client.sheet.get(config["ID"])

sheet = client.open_by_url(spreadsheet_url)
print(sheet)
