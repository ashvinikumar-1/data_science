# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
url1 = 'https://raw.githubusercontent.com/johnashu/datacamp/master/dob_job_application_filings_subset.csv'
# Save file locally
urlretrieve(url1, 'wdob_job_application_filings_subset.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('dob_job_application_filings_subset.csv', sep=',')
print(df.head())