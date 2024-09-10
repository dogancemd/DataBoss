import requests

def create_db_source(table_name, db_name="source_db", db_user="postgres_user", db_password="postgres_password",db_host_name="postgresql", port= 5432, mode = "incrementing", column_name = None):
    config = {
    "name": f"source-{db_name}-{table_name}",
    "config":{
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "tasks.max": "1",
        "connection.url": f"jdbc:postgresql://{db_host_name}:{port}/{db_name}",
        "connection.user": db_user,
        "connection.password": db_password,
        "mode": mode,
        f"{mode}.column.name" : column_name,
        "table.whitelist": table_name
        }
    }
    response = requests.post("http://localhost:8083/connectors", json=config)
    if int(response.status_code/100) != 2:
        raise Exception(response.json())

def create_db_sink(table_name, db_name="destination_db", db_user="postgres_user", db_password="postgres_password",db_host_name="postgresql", port= 5432, source_table = None):
    config = {
    "name": f"sink-{db_name}-{table_name}",
    "config":{
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "tasks.max": "1",
        "topics": table_name,
        "connection.url": f"jdbc:postgresql://{db_host_name}:{port}/{db_name}",
        "connection.user": db_user,
        "connection.password": db_password,
        "table.name.format": source_table if source_table is not None else "new_${topic}",
        "auto.create": True,
        
    }
    }
    response = requests.post("http://localhost:8083/connectors", json=config)
    if int(response.status_code/100) != 2:
        raise Exception(response.json())

def delete_connector(connector_name):
    requests.delete(f"http://localhost:8083/connectors/{connector_name}")

def get_connector_names():
    response = requests.get("http://localhost:8083/connectors")
    return response.json()

