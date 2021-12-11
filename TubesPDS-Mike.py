#Import Library
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import seaborn as sns

#Read Data
url = 'https://data.cityofnewyork.us/api/views/825b-niea/rows.csv?accessType=DOWNLOAD'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
df.columns = [c.replace(' ', '_') for c in df.columns]

# Checking the missing values
df.isnull().sum()

#Explore Data
#Grade - Category (All Grades, All Category)

df_allgrades = df[(df.Grade == "All Grades")]
df_allgrades_asian = df[(df.Grade == "All Grades") & (df.Category == "Asian")]
df_allgrades_black = df[(df.Grade == "All Grades") & (df.Category == "Black")]
df_allgrades_hispanic = df[(df.Grade == "All Grades") & (df.Category == "Hispanic")]
df_allgrades_white = df[(df.Grade == "All Grades") & (df.Category == "White")]

#Boxplot
sns.boxplot(df_allgrades_asian.Category, df_allgrades_asian.Number_Tested)
sns.boxplot(df_allgrades_black.Category, df_allgrades_black.Number_Tested)
sns.boxplot(df_allgrades_hispanic.Category, df_allgrades_hispanic.Number_Tested)
sns.boxplot(df_allgrades_white.Category, df_allgrades_white.Number_Tested)

sns.boxplot(df_allgrades.Category, df_allgrades.Number_Tested)
plt.title('All Grades per Year ~ Number Tested')
plt.show()

#Lineplot
plt.plot(df_allgrades_asian.Year, df_allgrades_asian.Number_Tested, label = "Asian")
plt.plot(df_allgrades_black.Year, df_allgrades_black.Number_Tested, label = "Black")
plt.plot(df_allgrades_hispanic.Year, df_allgrades_hispanic.Number_Tested, label = "Hispanic")
plt.plot(df_allgrades_white.Year, df_allgrades_white.Number_Tested, label = "White")
plt.legend()
plt.title('All Grades per Year ~ Number Tested')
plt.xlabel('Year')
plt.ylabel('Number Tested')
plt.show()

#

#Grade - Category (All Grades, Year)
