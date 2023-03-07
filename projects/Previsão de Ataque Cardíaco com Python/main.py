import pickle
import warnings

warnings.filterwarnings('ignore')

def get_features():
	print('-=- ATENDIMENTO MÉDICO -=-')
	print('# DETECÇÃO DE ATAQUE CARDÍACO\n')

	print('[1] Tipo de dor no peito, variável de (0-3)')
	f1 = int(input('? '))
	print('[2] O número de principais vasos coloridos por fluoroscopia (0-4)')
	f2 = int(input('? '))
	print('[3] Thal (0-2)')
	f3 = int(input('? '))
	print('[4] Depressão de ST induzida por exercício em relação ao repouso')
	f4 = int(input('? '))
	print('[5] Colesterol Sérico em mg/dl')
	f5 = int(input('? '))

	return f1, f2, f3, f4, f5

def start():
	with open('model.sav', 'rb') as f:
    		model = pickle.load(f)
	
	f1, f2, f3, f4, f5 = get_features()

	if model.predict([[f1, f2, f3, f4, f5]])[0]:
		print('POSSÍVEL ATAQUE CARDÍACO')
	else:
		print('NADA DETECTADO')	

if __name__ == '__main__':
	start()


