import pandas as pd

dict_medidas = {'idade': [15, 18, 25, 25, 40, 55, 58, 60, 80], 'altura': [160, 162, 165, 168, 172, 174, 174, 174, 176]}

print(dict_medidas)

df_medidas = pd.DataFrame.from_dict(dict_medidas)

print("Essas são as medidas")
print(df_medidas)

print("")
print("----------------------Medidas de Posição----------------------")
print(f"Essa é a média: {df_medidas["idade"].mean():.2f}")
print(f"Essa é a mediana: {df_medidas["idade"].median()}")
print(f"Essa é a moda: {df_medidas["idade"].mode()}")

print("")
print("----------------------Medidas de Disperção----------------------")
print(f"A variância é: {df_medidas['idade'].var():.2f}")
print(f"O desvio padrão é: {df_medidas['idade'].std():.2f}")
print(f"O coeficiente de variação é: {(df_medidas['idade'].std() / df_medidas['idade'].mean() * 100):.2f}")