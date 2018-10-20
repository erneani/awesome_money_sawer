import pandas as pd

dataset = pd.read_csv("./remuneracao.csv", sep=";", encoding="latin1")

print(dataset.loc[dataset['NOME']])
