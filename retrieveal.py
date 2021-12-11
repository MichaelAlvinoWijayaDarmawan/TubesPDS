# -*- coding: utf-8 -*-
"""
Program Untuk melakukan penarikan data menjadi sebuah CSV yang kemudian untuk dianalisis

@author: Alvino, Yalvi Hidayat
"""

#import stuff
import pandas as pd
from plotnine import *
from plotnine.data import mpg
#import data from website
url = 'https://data.cityofnewyork.us/api/views/825b-niea/rows.csv?accessType=DOWNLOAD'

df_math = pd.read_csv(url).dropna()

#%%melakukan penyiapan data dengan melakukan data cleaning. In case ada data yang kotor atau data yang outliers

#Karena grades ada yang byukan angka (ALL GRADES) -- ALLGRADES PERLU DIPISAH KE TABEL TERSENDIRI
df_allGrades = df_math.loc[df_math['Grade'] == 'All Grades']

#generate tabel bukan all grades
df_nonAllGrades = df_math.loc[df_math['Grade'] != 'All Grades']

#create boxplot to see the distribution
( 
 ggplot(df_nonAllGrades, aes(x="Grade")) 
 + geom_bar()
)

