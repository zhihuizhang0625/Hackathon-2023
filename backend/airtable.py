from pyairtable import Api, Base, Table

api = Api('apikey')
api.all('base_id', 'table_name')

base = Base('apikey', 'base_id')
base.all('table_name')

table = Table('apikey', 'base_id', 'table_name')
table.all()