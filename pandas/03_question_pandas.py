import pandas as pd

# Step 1: Create a dummy dataset
data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 103, 102],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Charlie", "Bob"],
    "Age": [20, 21, 19, 22, 20, 21, 19, 21],
    "Gender": ["F", "M", "M", "M", "F", "M", "M", "M"],
    "Marks": [85, 90, 78, 88, 92, 75, 78, 90]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Step 2: Display the initial dataset
print("Initial Dataset:")
print(df)

# Step 3: Drop duplicate rows
df_cleaned = df.drop_duplicates()

# Step 4: Display the shape of the dataset
print("\nShape of the dataset (rows, columns):")
print(df_cleaned.shape)

# Step 5: Display info about the dataset
print("\nInformation about the dataset:")
df_cleaned.info()

# Step 6: Display statistical summary
print("\nStatistical Summary:")
print(df_cleaned.describe())

# Step 7: Display the cleaned dataset
print("\nCleaned Dataset:")
print(df_cleaned)
