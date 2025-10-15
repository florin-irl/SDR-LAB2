from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
from recombee_api_client.exceptions import APIException
import pandas as pd

# configurare client
client = RecombeeClient(
  'florin-ivana-dev',
  'q3D7QnkhjuQdcWvb8LL0UScCKkuLjsO4PKwNky3CiCLujjbsK5sHI70PqS7Y0Uy3',
  region=Region.EU_WEST
)

# definire proprietați user
requests = [
    AddUserProperty("name", "string"),
    AddUserProperty("age", "int"),
    AddUserProperty("country", "string"),
    AddUserProperty("subscription_type", "string"),
    AddUserProperty("watch_time_hours", "double"),
    AddUserProperty("favorite_genre", "string"),
    AddUserProperty("last_login", "timestamp"),
]
client.send(Batch(requests))
print("Proprietăți Users create.")

# incarcare CSV local
csv_path = "netflix_users.csv"
dfu = pd.read_csv(csv_path)

# adaugare Users + setare valori
reqs = []

for idx, row in dfu.iterrows():
    # ID-ul utilizatorului
    if "User_ID" in dfu.columns and pd.notna(row["User_ID"]):
        user_id = str(row["User_ID"])
    else:
        user_id = f"user_{idx}"

    reqs.append(AddUser(user_id))

    values = {}

    if "Name" in dfu.columns and isinstance(row.get("Name"), str):
        values["name"] = row["Name"].strip()

    if "Age" in dfu.columns and pd.notna(row.get("Age")):
        try:
            values["age"] = int(row["Age"])
        except:
            pass

    if "Country" in dfu.columns and isinstance(row.get("Country"), str):
        values["country"] = row["Country"].strip()

    if "Subscription_Type" in dfu.columns and isinstance(row.get("Subscription_Type"), str):
        values["subscription_type"] = row["Subscription_Type"].strip()

    if "Watch_Time_Hours" in dfu.columns and pd.notna(row.get("Watch_Time_Hours")):
        try:
            values["watch_time_hours"] = float(row["Watch_Time_Hours"])
        except:
            pass

    if "Favorite_Genre" in dfu.columns and isinstance(row.get("Favorite_Genre"), str):
        values["favorite_genre"] = row["Favorite_Genre"].strip()

    if "Last_Login" in dfu.columns and pd.notna(row.get("Last_Login")):
        try:
            ts = pd.to_datetime(row["Last_Login"], errors="coerce")
            if pd.notna(ts):
                values["last_login"] = int(ts.timestamp())
        except:
            pass

    if values:
        reqs.append(SetUserValues(user_id, values, cascade_create=True))

# trimitere in batch-uri
CHUNK = 50
for i in range(0, len(reqs), CHUNK):
    client.send(Batch(reqs[i:i+CHUNK]))
    print(f"Trimis batch {i//CHUNK + 1}")

print(f"Incarcat {len(dfu)} utilizatori in Recombee.")
