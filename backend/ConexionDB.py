from azure.cosmos import CosmosClient

# Configuración de la conexión
endpoint_uri = 'https://botland.documents.azure.com:443/'
access_key = 'ZcD4fI61wxesfeUimAiKA1pZ5627zS2qsqRLX2W5HCfPzh9mxZsfS0fnEPK8YlK00IkQMNdOnyncACDbZKsByw=='
database_name = 'ToDoList'
container_name = 'Items'

# Establecer la conexión
client = CosmosClient(endpoint_uri, access_key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Función para registrar un nuevo usuario
def registrar_usuario(usuario_id,nombre, correo, contraseña):
    # Verificar si el usuario ya existe en la base de datos
    query = f"SELECT * FROM c WHERE c.correo = '{correo}'"
    resultado = list(container.query_items(query, enable_cross_partition_query=True))
    
    if resultado:
        return 'El usuario ya está registrado'
    
    # Crear un nuevo documento para el usuario
    nuevo_usuario = {
        'id': usuario_id,
        'nombre': nombre,
        'correo': correo,
        'contraseña': contraseña
    }
    
    container.create_item(nuevo_usuario)
    
    return 'Registro exitoso'


