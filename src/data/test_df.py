import pandas as pd

# Creating a DataFrame using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
