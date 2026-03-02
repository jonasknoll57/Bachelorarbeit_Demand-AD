import os
import glob
from pathlib import Path
import pandas as pd

# Basisverzeichnis
base_path = r"/Users/jonas/DHBW/BA/demand-anomaly-detection/data/demand"

# Erste Stadt: AW-bike (VRM)
first_city = "AW-bike (VRM)"
city_path = os.path.join(base_path, first_city)
print(f"🔍 Analyse für: '{first_city}' ({city_path})")

# Alle Dateien
parquet_files = sorted(glob.glob(os.path.join(city_path, "*.parquet")))
print(f"\n📁 Dateien (9 total):")
for f in parquet_files:
    size_mb = os.path.getsize(f) / (1024*1024)
    print(f"  {os.path.basename(f)}: {size_mb:.1f} MB")

# Versuche Datei zu laden (mit Fehlerbehandlung)
first_file = parquet_files[0]
print(f"\n📊 Lade: {os.path.basename(first_file)}")

try:
    df = pd.read_parquet(first_file)
    print("✅ Erfolgreich geladen!")
    
    print(f"\nSHAPE: {df.shape}")
    print(f"SPALTEN ({len(df.columns)}): {list(df.columns)}")
    
    print("\n📈 NUMERISCHE STATISTIK:")
    numeric = df.select_dtypes(include='number')
    if not numeric.empty:
        print(numeric.describe().round(2))
    
    print("\n❌ Fehlende Werte:")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.any() else "Keine!")
    
    print("\n👀 Erste 5 Zeilen:")
    print(df.head())
    
    # Zeitreihen-Check
    for col in df.columns:
        if df[col].dtype == 'object':
            unique_dates = df[col].dropna().unique()[:5]
            print(f"\n{col} (Beispiele): {unique_dates}")
            
except ImportError as e:
    print("❌ PyArrow fehlt! Installiere: pip install pyarrow")
except Exception as e:
    print(f"❌ Fehler beim Laden: {e}")
    print("Dateigröße:", os.path.getsize(first_file) / (1024*1024), "MB")

print(f"\n💡 Nächste Schritte: pip install pyarrow && rerun")
