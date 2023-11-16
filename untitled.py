#In this project, we're going to do the following steps

#

import pandas as pd
import selenium

# Replace 'salaries-us.csv' 
file_path = 'salaries-us.csv'

# Use pandas to read the CSV file into a DataFrame
df = pd.read_csv(file_path)

df
