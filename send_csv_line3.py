import requests
import csv
import io
import os

CSV_URL = "https://monde8.empireimmo.com/api/materials_materiaux.csv"
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

response = requests.get(CSV_URL)
response.raise_for_status()

csv_file = io.StringIO(response.text)
reader = list(csv.reader(csv_file, delimiter=';'))


headers = ""
line3 = reader[2]

message = "📊 **Taux Promoteur Matériaux**\n"
for h, v in zip(headers, line3):
    message += f"**{h}** : {v}\n"

requests.post(DISCORD_WEBHOOK, json={"content": message})
