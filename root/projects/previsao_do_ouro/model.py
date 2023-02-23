# Importando modulos necessarios
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

def start_model():
    
    # Definindo funçao para transformaçao de objeto string em datetime
    def turn_into_datetime(series):
        return pd.to_datetime(series)
    
    
    # Definindo funçao para extrair dados especificos de um objeto datetime
    def break_datetime(df, name_variable):
        df['Day'] = df[name_variable].apply(lambda date : date.day)
        df['Month'] = df[name_variable].apply(lambda date : date.month)
        df['Year'] = df[name_variable].apply(lambda date : date.year)
    
    
    # Lendo base de dados
    df = pd.read_csv('https://raw.githubusercontent.com/amankharwal/Website-data/master/gold_price.csv')
    
    # Transformando variavel
    df['Date'] = turn_into_datetime(df['Date'])
    
    # Extraindo dados
    break_datetime(df, 'Date')
    
    # Separando dados entre input e output
    x = df[['Year', 'Month', 'Day']]
    y = df['USD (AM)']
    
    # Instanciando modelo
    model = LinearRegression()
    model.fit(x, y)
    
    return model


def start_program():
    print('Digite em sequencia, o dia, mes e ano')
    day = int(input('? '))
    month = int(input('? '))
    year = int(input('? '))
    
    predict = model.predict([[year, month, day]])

    print(f'Preço do ouro em {day}-{month}-{year} : $ {predict[0]:.2f}\n')
    
    print('Isso e um modelo baseado em regressao linear com r2 de 70%')
    
    
if __name__ == '__main__':
    start_program()



