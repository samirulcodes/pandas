import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [25, 30, 35, 28],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Create a DataFrame from a dictionary
df = pd.DataFrame(data)
print(df)
print(type(df))


# adding new columns

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [25, 30, 35, 28]}
df = pd.DataFrame(data)
print("Before Adding Column")
print(df)
# Add a new column "City" with values
df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']
print("After Adding Column")
print(df)
