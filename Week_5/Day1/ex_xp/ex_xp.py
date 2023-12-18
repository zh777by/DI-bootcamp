import pandas as pd

data = pd.Series([1, 3, 5, 7, 9])

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# df.head()
# ages = df['Age']
# df[df['Age'] > 30]
df.groupby('City').mean()

print(df)

