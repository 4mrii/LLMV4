import pandas as pd

# Read the CSV file with 'utf-8-sig' encoding
df = pd.read_csv('dictionaryDBP.csv', encoding='utf-8-sig')

# Modify the 'description' column
df['description'] = df['description'].apply(lambda x: x[x.index('Definisi :'):] if 'Definisi :' in x else x)

# Write the result to a new CSV file with 'utf-8-sig' encoding
df.to_csv('cleaned_V1.csv', index=False, encoding='utf-8-sig')
