# enter venv with: source venv/bin/activate
import pandas as pd
from io import StringIO

data = "/Users/jonas/DHBW/BA/Bachelorarbeit_Demand-AD/City-System_Category/V1_C_network_stats.csv"

# Einlesen
df = pd.read_csv(data)

# sicherstellen, dass bike_return_pct numerisch ist
df["bike_return_pct"] = pd.to_numeric(df["bike_return_pct"], errors="coerce")

# Bedingungen anwenden und system_type ersetzen
df.loc[df["bike_return_pct"] < 8, "system_type"] = "station_based"
df.loc[df["bike_return_pct"] > 18, "system_type"] = "free_floating"
df.loc[(df["bike_return_pct"] >= 8) & (df["bike_return_pct"] <= 18), "system_type"] = "ungewiss"

print(df)

df.to_csv("/Users/jonas/DHBW/BA/Bachelorarbeit_Demand-AD/City-System_Category/V1_C_network_stats_updated.csv", index=False)