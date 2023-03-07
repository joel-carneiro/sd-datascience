import pickle

def welcome():
    print('=-=' * 13)
    print('> PREVISÃO DE CUSTO PARA PLANO DE SAÚDE')
    print('=-=' * 13)


def question(text):
    print(text)
    return input('? ')


def generate_params():
    age = int(question(text='Qual sua idade?'))
    sex = question(text='Insira seu sexo, [M/F]')
    smoker = question(text='Você fuma? [S/N]')
    bmi = question(text='Qual seu indice de massa corporal? (IMC)')
    childrens = question(text='Você possui quantos filhos?')
    region = question(text='Sua região [NORTE/NORDESTE/SUL/CENTRO-OESTE/SUDESTE]')

    return {"Idade" : age, "Sexo" : sex, "Fumante" : smoker,
    "IMC" : bmi, "Número de Filhos" : childrens, "Região" : region}


def load_model():
    with open('WHSmodel.pkl', 'rb') as f:
        model = pickle.load(f)
    
    return model


def generate_value(model):
    model.predict()
    pass


def app():
    generate_value()


if __name__ == '__main__':
    app()