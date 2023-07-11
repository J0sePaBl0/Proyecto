from azure.cosmos import CosmosClient, DatabaseProxy

# Configuración de la conexión
endpoint_uri = 'https://botland.documents.azure.com:443/'
access_key = 'ZcD4fI61wxesfeUimAiKA1pZ5627zS2qsqRLX2W5HCfPzh9mxZsfS0fnEPK8YlK00IkQMNdOnyncACDbZKsByw=='
database_name = 'ToDoList'

# Establecer la conexión
client = CosmosClient(endpoint_uri, access_key)
database = client.get_database_client(database_name)

# Ejemplo: Crear un nuevo documento en un contenedor
container_name = 'Items'

container = database.get_container_client(container_name)

new_document = {
    'id': 'documento_id',
    'nombre': 'Ejemplo',
    'edad': 30
}

container.create_item(new_document)

# Otros operaciones con la base de datos...


