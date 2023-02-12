from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from pandas import DataFrame

def get_models():
    
    models = [
        LogisticRegression(),
        DecisionTreeClassifier(),
        KNeighborsClassifier(),
        LinearDiscriminantAnalysis(),
        GaussianNB(),
        SVC()
    ]
    
    return models

def test_models_recursively(x, y):
    models = get_models()
    
    accuracys = []
    precisions = []
    models_string = []

    for model in models:
        accuracy = cross_val_score(model, x, y, cv=10, scoring='accuracy')
        precision = cross_val_score(model, x, y, cv=10, scoring='precision')
        
        accuracys.append(accuracy.mean())
        precisions.append(precision.mean())
        models_string.append(str(model))
    
    return DataFrame({'model' : models_string, 'accuracy' : accuracys, 'precision' : precisions})
