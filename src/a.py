from deta import Deta

user = {'date_joined': '2023-11-20 05:18:02.204100', 'favorites': ['25009e0a-0e60-4169-9f76-f464225549a9'], 'key': '8xv6jmzp08j8', 'password': 'clave123', 'username': 'usuario'}

token = "e0m3ypPCenY_6yhHxaZYb4LDBhYTD3DKPsnd9ABPk5gN"

deta = Deta(token)

# Inicializar Base de Datos de Deta para usuarios
db = deta.Base('Appetito_usuarios')

print(user.items())

dict = {k: v for k, v in user.items() if k != 'key'}

print(dict)

db.update(
    dict,
    user['key'],
)