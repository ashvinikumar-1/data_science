from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query('Select * from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId '
                       'where Milliseconds < 250000 ', engine)
print(df.head())