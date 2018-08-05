from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute('Select * from Employee order by BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()


# Print head of DataFrame
print(df.head())
