import pandas as pd
import sqlite3
import great_expectations as ge
from sqlalchemy import create_engine

# STEP 1: Extract Data
sqlite_conn = sqlite3.connect("c:/sqlite/shop.db")
df_product1 = pd.read_sql_query("SELECT * FROM product1", sqlite_conn)
sqlite_conn.close()
csv_path = "C:/Users/munir/Downloads/Orders_Data.csv"
df_orders = pd.read_csv(csv_path)

# STEP 2: Validate Data
ge_product1 = ge.from_pandas(df_product1)
ge_orders = ge.from_pandas(df_orders)

ge_product1.expect_column_values_to_not_be_null("product_name")
ge_orders.expect_column_to_exist("Sales")

print("product1 Validation:")
print(ge_product1.validate())
validation_orders = ge_orders.validate()


# STEP 3: Load to PostgreSQL (Only if data is valid)
valid_product= ge_product1.validate()["success"]
validation_orders = ge_orders.validate()
print("Validation orders:", validation_orders["success"])

if valid_product and validation_orders:
    engine = create_engine("postgresql+psycopg2://postgres:ds123@localhost:5432/demo")
    df_product1.to_sql("stage_product1", engine, if_exists="replace", index=False)
    df_orders.to_sql("stage_orders1", engine, if_exists="replace", index=False)
    print("Data successfully loaded into PostgreSQL staging tables.")
else:
    print("Data validation failed. Data not loaded to PostgreSQL.")
    