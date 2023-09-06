"""
conducting a basic level statistical analysis using pandas
"""
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
mean_age = df['Age'].mean()
print(f"Mean Age: {mean_age:.2f}")


