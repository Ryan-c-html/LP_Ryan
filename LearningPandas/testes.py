import pandas as pd

data = {'Novas': ['Greys Anatomy', 'Lost', 'Supernatural', 'The Big Bang Theory'],'Antigas': ['PLL', 'TVD', 'Friends', 'Game of Thrones']}

df = pd.DataFrame(data, index=['Muito Boas', 'Boas', 'Medias', 'Ruins'], columns=['Novas', 'Antigas'])

df.names = 'Series'
novos = df['Novas'][1]
boas = df.iloc[0, 1]

print(df)
print(f'\n Somente novos:\n', novos)
print(f'\n\nSeries boas:\n', boas)