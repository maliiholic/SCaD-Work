import numpy as np
import pandas as pd

# Create a NumPy array
data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("NumPy Array:\n", data)

# Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(data, columns=["A", "B", "C"])
print("\nPandas DataFrame:\n", df)

# Add a new column with row-wise sum
df["Sum"] = df.sum(axis=1)
print("\nDataFrame after adding Sum column:\n", df)

# Save to a CSV file
df.to_csv("data.csv", index=False)
print("\nData saved to data.csv!")

