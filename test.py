import os
import glob
from pathlib import Path

# Basisverzeichnis, wo die Städte-Ordner liegen
base_path = r"/Users/jonas/DHBW/BA/demand-anomaly-detection/data/demand"

# Alle Unterordner (Städte) finden
cities = [d for d in os.listdir(base_path) 
          if os.path.isdir(os.path.join(base_path, d))]

print(f"Gefundene Städte: {cities}")

all_parquet_files = []
total_size_bytes = 0

# Jede Stadt durchlaufen und Parquet-Dateien einlesen + Größe zählen
for city in cities:
    city_path = os.path.join(base_path, city)
    # Alle *.parquet Dateien in der Stadt finden
    parquet_files = glob.glob(os.path.join(city_path, "*.parquet"))
    
    print(f"\nStadt '{city}': {len(parquet_files)} Dateien gefunden")
    
    for file_path in parquet_files:
        all_parquet_files.append(file_path)
        file_size = os.path.getsize(file_path)
        total_size_bytes += file_size
        print(f"  - {os.path.basename(file_path)}: {file_size / (1024*1024):.2f} MB")

# Zusammenfassung
num_files = len(all_parquet_files)
total_size_mb = total_size_bytes / (1024 * 1024)
total_size_gb = total_size_mb / 1024

print(f"\n{'='*50}")
print(f"ANZAHL DATEIEN: {num_files}")
print(f"GESAMTGRÖSSE: {total_size_mb:.2f} MB ({total_size_gb:.2f} GB)")
print(f"{'='*50}")

# Optional: Dateien einlesen mit pandas (Beispiel für erste Datei)
# import pandas as pd
# if all_parquet_files:
#     df = pd.read_parquet(all_parquet_files[0])
#     print(f"\nErste Datei '{os.path.basename(all_parquet_files[0])}' hat Shape: {df.shape}")
