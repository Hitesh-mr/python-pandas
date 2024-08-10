import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
    'Age': [20, 22, 23, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)
