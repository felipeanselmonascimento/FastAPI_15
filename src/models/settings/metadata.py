# informar a orm oque existe no nosso banco de dados, meio q mapear
# Está dizendo: "registra essa tabela no metadata"
# Então o metadata fica sabendo de todas as tabelas:
# metadata
#     └── users (id, user_name, age, uf)
#     └── products (id, name, price)   ← se tivesse outra tabela
#     └── ...
from sqlalchemy import MetaData

metadata = MetaData()