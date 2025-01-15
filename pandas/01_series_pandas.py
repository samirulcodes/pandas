import numpy as np
import pandas as pd

a=[1,2,3,4,5]
ser=pd.Series(a)
print(ser)
print(type(ser))

import pandas as pd
# Months in a year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
'October', 'November', 'December']
# Monthly sales data for a product (example data)
sales_data = [12000, 13500, 14200, 12800, 14000, 15500, 16200, 15800, 16500,
17800, 18500, 17200]
# Create a Pandas Series with months as the index
sales_series = pd.Series(sales_data, index=months, name='Monthly Sales (USD)')

print(sales_data)
print(sales_series)

# data=pd.read_csv("BlinkIT Grocery Data.csv")
# print(data)