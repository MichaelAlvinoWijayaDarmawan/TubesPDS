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
df.columns = [c.replace('#', 'H') for c in df.columns]
df.columns = [c.replace('%', 'P') for c in df.columns]


#Check Data Type
df.dtypes

#Change Data Type
for col in ['Grade', 'Year', 'Category']:
    df[col] = df[col].astype('category')


# Check Null
df.isnull().sum()

#Explore Data----------------------------------------------------------------------------------
#Grade - Category (All Grades, All Category) ~ Number Tested, Year~~~~~~~~~~~~~~~~~~~~~~

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
#All
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


#Grade - Category (All Grades, All Category)  ~ Mean Scale Score, Year~~~~~~~~~~~~~~~~~

#Boxplot
sns.boxplot(df_allgrades_asian.Category, df_allgrades_asian.Mean_Scale_Score)
sns.boxplot(df_allgrades_black.Category, df_allgrades_black.Mean_Scale_Score)
sns.boxplot(df_allgrades_hispanic.Category, df_allgrades_hispanic.Mean_Scale_Score)
sns.boxplot(df_allgrades_white.Category, df_allgrades_white.Mean_Scale_Score)
#All
sns.boxplot(df_allgrades.Category, df_allgrades.Mean_Scale_Score)
plt.title('All Grades per Year ~ Mean Scale Score')
plt.show()

#Lineplot
plt.plot(df_allgrades_asian.Year, df_allgrades_asian.Mean_Scale_Score, label = "Asian")
plt.plot(df_allgrades_black.Year, df_allgrades_black.Mean_Scale_Score, label = "Black")
plt.plot(df_allgrades_hispanic.Year, df_allgrades_hispanic.Mean_Scale_Score, label = "Hispanic")
plt.plot(df_allgrades_white.Year, df_allgrades_white.Mean_Scale_Score, label = "White")
plt.legend()
plt.title('All Grades per Year ~ Mean Scale Score')
plt.xlabel('Year')
plt.ylabel('Number Tested')
plt.show()

#Grade - Category (Grades, Category Asian)  ~ Mean Scale Score,Year~~~~~~~~~~~~~~~~~~~~~~~
df_grades = df[(df.Grade != "All Grades")]
df_grades_asian = df_grades[(df.Category == "Asian")]

#Lineplot Asian
grades_2006_asian = df_grades_asian[(df_grades_asian.Year == 2006)]
grades_2007_asian = df_grades_asian[(df_grades_asian.Year == 2007)]
grades_2008_asian = df_grades_asian[(df_grades_asian.Year == 2008)]
grades_2009_asian = df_grades_asian[(df_grades_asian.Year == 2009)]
grades_2010_asian = df_grades_asian[(df_grades_asian.Year == 2010)]
grades_2011_asian = df_grades_asian[(df_grades_asian.Year == 2011)]

plt.plot(grades_2006_asian.Grade, grades_2006_asian.Mean_Scale_Score, label = "2006")
plt.plot(grades_2007_asian.Grade, grades_2007_asian.Mean_Scale_Score, label = "2007")
plt.plot(grades_2008_asian.Grade, grades_2008_asian.Mean_Scale_Score, label = "2008")
plt.plot(grades_2009_asian.Grade, grades_2009_asian.Mean_Scale_Score, label = "2009")
plt.plot(grades_2010_asian.Grade, grades_2010_asian.Mean_Scale_Score, label = "2010")
plt.plot(grades_2011_asian.Grade, grades_2011_asian.Mean_Scale_Score, label = "2011")

plt.legend()
plt.title('Grades per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Grade')
plt.ylabel('Mean Scale Score')
plt.show()



