import pickle
from pandas import DataFrame
from pandas import read_csv

class HBO:
	def __init__(self, data_path, model_path):
		self.data = read_csv(data_path)
		with open(model_path, 'rb') as f:
			self.model = pickle.load(f)


	def recommend_titles(self, array):
		x = [int(g in array) for g in self.data.iloc[:, 4:-1].columns]
		print(self.model.predict([x]))


hbo = HBO('data/hbo_data.csv', 'models/hbomax_model.pickle')
hbo.recommend_titles(['fantasy', 'drama'])
