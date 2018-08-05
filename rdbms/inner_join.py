from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    rs = con.execute('Select Title, Name from Album Inner join Artist on Album.ArtistId = Artist.ArtistId')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()


print(df.head())
