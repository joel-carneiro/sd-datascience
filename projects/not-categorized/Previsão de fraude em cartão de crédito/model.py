import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import warnings

warnings.filterwarnings('ignore')

def start_model():

    df = pd.read_csv('/home/joel/Documentos/projects/not-categorized/Previsão de fraude em cartão de crédito/credit_card_balance')
    
    x = df[['distance_from_home', 'ratio_to_median_purchase_price', 'online_order']]
    y = df['fraud']
    
    dtc = DecisionTreeClassifier()
    
    dtc.fit(x, y)

    return dtc

def start_program():
    model = start_model()
    print('Por favor, diga em ordem a:')
    print('[1] A distância da casa ate onde a transação aconteceu.')
    print('[2] Razão entre a transação do preço de compra e o preço médio de compra.')
    print('[3] Se a transaçao e um pedido online')
    
    print('-=-' * 10)
    
    distance_from_home = input('[1] ? ')
    ratio_to_median_purchase_price = input('[2] ? ')
    online_order = input('[3] ? ')
    
    y_pred = model.predict([[distance_from_home,  ratio_to_median_purchase_price, online_order]])
    
    if y_pred == 1:
        print('CUIDADO, POSSIVELMENTE E UMA FRAUDE')
    else:
        print('Nao detectei nada de anormal')
        

if __name__ == '__main__':
    start_program()