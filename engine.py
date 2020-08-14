#Creating engine with postgres and sqlalchemy and storing the dataframe into database by using engine

# Importing required libraries
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Creating engine
engine = create_engine('postgresql+psycopg2://username:password@host/database_name')

# Create dataframe
x = pd.DataFrame({'Column1': [1, 2], 'Column2': [3, 4]})

# Store dataframe into database
x.to_sql(name='table_name', con=engine, index=False, if_exixts='append')

# Read table from database
x.read_sql_table('table_name', engine)

# Printing table
print(x)
