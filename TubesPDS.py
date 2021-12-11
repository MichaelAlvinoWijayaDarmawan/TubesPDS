#Import Library
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt

#Read Data
url = 'https://data.cityofnewyork.us/api/views/825b-niea/rows.csv?accessType=DOWNLOAD'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

# Checking the missing values
df.isnull().sum()

#melakukan penyiapan data dengan melakukan data cleaning. In case ada data yang kotor atau data yang outliers
#Karena grades ada yang byukan angka (ALL GRADES) -- ALLGRADES PERLU DIPISAH KE TABEL TERSENDIRI
df_allGrades = df.loc[df['Grade'] == 'All Grades']

#generate tabel bukan all grades
df_nonAllGrades = df.loc[df['Grade'] != 'All Grades']