import pandas as pd

# Fixed data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"],
    "Age": [20, 22, 19, 21, 23, 20, 22, 19, 21, 20],
    "Grade": [85, 78, 95, 67, 74, 88, 91, 82, 77, 90],
    "Attendance (%)": [92.5, 88.0, 96.5, 80.0, 85.5, 90.0, 93.0, 89.5, 84.0, 95.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
print(df)