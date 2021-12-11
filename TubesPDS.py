import pandas as pd
import io
import requests

#Read Data
url = ''
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

#Explore Data