#Import Library
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt

#Read Data
url = 'https://healthdata.gov/api/views/usvm-fdmd/rows.csv?accessType=DOWNLOAD'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))


# Checking the missing values
df.isnull().sum()

#Explore Data
