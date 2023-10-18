import pandas as pd
#Change the path to the downloaded file
xlsx = '2020_jaarboek_941_4eccf4d8b6.xlsx'
df = pd.read_excel(xlsx)

#from txt to NaN, so it is all numeric
df['totaal fosfor'] = pd.to_numeric(df['totaal fosfor'], errors='coerce')

column1 = 'totaal fosfor'

min_value = df[column1].min()
max_value = df[column1].max()

print(f"Minimum value in {column1} : {min_value}")
print(f"Maximum value in {column1} : {max_value}")
