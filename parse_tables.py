import json
from kafka_connectors import *

with open("example.json", "r") as f:
    tables_data = json.load(f)

tables = tables_data["tables"]
source_db = tables_data["source_db"]
destination_db = tables_data["destination_db"]
for table in tables:
    print(f"{table['table_name']}:", end="\t")
    try:
        create_db_source(table_name=table["table_name"], db_name = source_db["db_name"], db_user = source_db["db_user"], db_password=source_db["db_password"], db_host_name=source_db["db_host_name"], port=source_db["db_port"], mode = table["mode"])
        create_db_sink(table_name=table["table_name"], db_name = destination_db["db_name"], db_user = destination_db["db_user"], db_password=destination_db["db_password"], db_host_name=destination_db["db_host_name"], port=destination_db["db_port"])
        print("DONE")
    except Exception as e:
        print("Failed")
        print(str(e))