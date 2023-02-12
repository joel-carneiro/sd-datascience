import pandas as pd
from sqlalchemy import create_engine

def create_db(database, csv, table):
	# Criando a string para conexão com o banco de dados
	connection_string = f'mysql+mysqlconnector://root:thisissimple@localhost:3306/{database}'
	
	# Criando a conexão com o banco de dados
	engine = create_engine(connection_string)
	
	# Importando o arquivo csv
	df = pd.read_csv(csv)
	
	# Transferindo para o banco de dados
	df.to_sql(name = table, con = engine, if_exists='replace', index=False)


def start():
	# Extraindo dados do usuario
	database = input('DATABASE NAME ? ')
	csv = input('ARQUIVE NAME ? ')
	table = input('TABLE NAME ? ')
	
	# Executando a criação do banco de dados
	try:
		print('LOADING...')
		create_db(database, csv, table)
		print('SUCESS!')
	except:
		print('ERROR!')

if __name__ == '__main__':
	start()
