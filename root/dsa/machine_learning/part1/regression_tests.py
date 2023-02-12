from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import ARDRegression
from sklearn.linear_model import SGDRegressor
from pandas import DataFrame

def get_models():

	# Função apenas para instanciar e listar os modelos, você pode adicionar mais aqui, porém
	# Certifique-se desse modelo ter o método "score()" caso contrário, você terá que alterar
	# O funcionamento da próxima função

    models = [
        LinearRegression(),
        Ridge(),
        Lasso(),
        ElasticNet(),
        KNeighborsRegressor(),
        DecisionTreeRegressor(),
        RandomForestRegressor(),
        GradientBoostingRegressor(),
        SVR(),
        MLPRegressor(),
        BayesianRidge(),
        HuberRegressor(),
        ARDRegression(),
        SGDRegressor()
    ]
    
    return models


# A função espera receber os dados de treino e teste
def get_model_results(x_train, x_test, y_train, y_test):
    
    # Instância todos os modelos
    models = get_models()
    
    # Listas vazias
    list_models = []
    list_scores = []
    
    # Irá treinar cada modelo e armazenar sua acurácia dentro de uma lista
    for model in models:
        model.fit(x_train, y_train)
        list_models.append(str(model))
        list_scores.append(model.score(x_test, y_test))

    # Retornará um dataframe pandas
    return DataFrame({'model' : list_models, 'score' : list_scores})