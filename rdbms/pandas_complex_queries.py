from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query('Select * from Employee where EmployeeId >= 6 order by BirthDate', engine)

print(df.head())

