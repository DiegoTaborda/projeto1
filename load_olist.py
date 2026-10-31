# load_olist.py
import duckdb
from pathlib import Path

# Caminho do banco (o mesmo do profiles.yml)
DB_PATH = "olist.duckdb"
DATA_DIR = Path("data_raw")

# Conecta (ou cria) o banco
con = duckdb.connect(DB_PATH)

# Cria o schema raw (camada de dados brutos)
con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

# Lista todos os CSVs da pasta data_raw
csv_files = list(DATA_DIR.glob("*.csv"))

for csv_path in csv_files:
    # O nome da tabela será o nome do arquivo sem a extensão .csv
    table_name = csv_path.stem  # ex: "olist_customers_dataset"
    print(f"Carregando {csv_path.name} -> raw.{table_name} ...")

    # Lê o CSV e cria/substitui a tabela no schema raw
    # O DuckDB é ótimo em ler CSV diretamente
    con.execute(f"""
        CREATE OR REPLACE TABLE raw.{table_name} AS
        SELECT * FROM read_csv_auto('{csv_path.as_posix()}');
    """)

print("Carga concluída.")
con.close()