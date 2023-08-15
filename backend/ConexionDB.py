from azure.cosmos import CosmosClient

# Configuración de la conexión
items_endpoint_uri = 'https://botland.documents.azure.com:443/'
items_access_key = 'ZcD4fI61wxesfeUimAiKA1pZ5627zS2qsqRLX2W5HCfPzh9mxZsfS0fnEPK8YlK00IkQMNdOnyncACDbZKsByw=='
items_database_name = 'ToDoList'
items_container_name = 'Items'


# Establecer la conexión
items_client = CosmosClient(items_endpoint_uri, items_access_key)
items_database = items_client.get_database_client(items_database_name)
items_container = items_database.get_container_client(items_container_name)

bots_endpoint_uri = 'https://botland.documents.azure.com:443/'
bots_access_key = 'ZcD4fI61wxesfeUimAiKA1pZ5627zS2qsqRLX2W5HCfPzh9mxZsfS0fnEPK8YlK00IkQMNdOnyncACDbZKsByw=='
bots_database_name = 'ToDoList'
bots_container_name = 'Bots'

bots_client = CosmosClient(bots_endpoint_uri, bots_access_key)
bots_database = bots_client.get_database_client(bots_database_name)
bots_container = bots_database.get_container_client(bots_container_name)




# Función para registrar un nuevo usuario
def registrar_usuario(usuario_id,nombre, correo, contraseña):
    # Verificar si el usuario ya existe en la base de datos
    query = f"SELECT * FROM c WHERE c.correo = '{correo}'"
    resultado = list(items_container.query_items(query, enable_cross_partition_query=True))
    
    if resultado:
        return 'El usuario ya está registrado'
    
    # Crear un nuevo documento para el usuario
    nuevo_usuario = {
        'id': usuario_id,
        'nombre': nombre,
        'correo': correo,
        'contraseña': contraseña
    }
    
    items_container.create_item(nuevo_usuario)
    
    return 'Registro exitoso'

def crear_bot():
  
   
    nuevo_bot = {
        'id': '4',
        'nombre': 'Bot nutricionista',
        'descripcion': 'Este bot te ayudara a realizar tu dieta dependiendo de lo que necesites',
        'precio': '60'
    }
    
    bots_container.create_item(nuevo_bot)
    
    return 'Registro exitoso'


def obtener_bots():
    query = "SELECT * FROM c"
    items = list(bots_container.query_items(query, enable_cross_partition_query=True))

    bots = []
    for item in items:
        bot = {
            'nombre': item['nombre'],
            'descripcion': item['descripcion'],
            'precio': item['precio']
            # Agrega más campos según tu estructura de datos
        }
        bots.append(bot)

    return bots

