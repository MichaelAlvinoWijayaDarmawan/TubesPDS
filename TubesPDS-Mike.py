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
df_allgrades_asian = df_allgrades[(df.Category == "Asian")]
df_allgrades_black = df_allgrades[(df_allgrades.Category == "Black")]
df_allgrades_hispanic = df_allgrades[(df_allgrades.Category == "Hispanic")]
df_allgrades_white = df_allgrades[(df_allgrades.Category == "White")]

#Boxplot
sns.boxplot(df_allgrades_asian.Category, df_allgrades_asian.Number_Tested)
sns.boxplot(df_allgrades_black.Category, df_allgrades_black.Number_Tested)
sns.boxplot(df_allgrades_hispanic.Category, df_allgrades_hispanic.Number_Tested)
sns.boxplot(df_allgrades_white.Category, df_allgrades_white.Number_Tested)
#All
sns.boxplot(df_allgrades.Category, df_allgrades.Number_Tested)
plt.title('All Grades per Year ~ Number Tested')
plt.xlabel('Category')
plt.ylabel('Number Tested')
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
df_grades_asian = df_grades[(df_grades.Category == "Asian")]

#Per Year
grades_2006_asian = df_grades_asian[(df_grades_asian.Year == 2006)]
grades_2007_asian = df_grades_asian[(df_grades_asian.Year == 2007)]
grades_2008_asian = df_grades_asian[(df_grades_asian.Year == 2008)]
grades_2009_asian = df_grades_asian[(df_grades_asian.Year == 2009)]
grades_2010_asian = df_grades_asian[(df_grades_asian.Year == 2010)]
grades_2011_asian = df_grades_asian[(df_grades_asian.Year == 2011)]

#Per Grade
grade_3 = df_grades_asian[(df_grades_asian.Grade == '3')]
grade_4 = df_grades_asian[(df_grades_asian.Grade == '4')]
grade_5 = df_grades_asian[(df_grades_asian.Grade == '5')]
grade_6 = df_grades_asian[(df_grades_asian.Grade == '6')]
grade_7 = df_grades_asian[(df_grades_asian.Grade == '7')]
grade_8 = df_grades_asian[(df_grades_asian.Grade == '8')]


#Lineplot Asian
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

#Lineplot All Grades Asian
plt.plot(df_allgrades_asian.Year, df_allgrades_asian.Mean_Scale_Score, label = "All Grades")
plt.title('All Grades per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.show()


#Barplot Grade Asian ~ Mean Scale Score
#Barplot Grade 3 Asian
plt.bar(grade_3.Year,grade_3.Mean_Scale_Score, label = "Grade 3")
plt.title('Grade 3 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot Grade 4 Asian
plt.bar(grade_4.Year,grade_4.Mean_Scale_Score, label = "Grade 4")
plt.title('Grade 4 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot Grade 5 Asian
plt.bar(grade_5.Year,grade_5.Mean_Scale_Score, label = "Grade 5")
plt.title('Grade 5 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot Grade 6 Asian
plt.bar(grade_6.Year,grade_6.Mean_Scale_Score, label = "Grade 6")
plt.title('Grade 6 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot Grade 7 Asian
plt.bar(grade_7.Year,grade_7.Mean_Scale_Score, label = "Grade 7")
plt.title('Grade 7 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot Grade 8 Asian
plt.bar(grade_8.Year,grade_8.Mean_Scale_Score, label = "Grade 8")
plt.title('Grade 8 per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((669, 720)) 
plt.show()

#Barplot All Grades Asian
plt.bar(df_allgrades_asian.Year,df_allgrades_asian.Mean_Scale_Score, label = "All Grades")
plt.title('All Grades per Year ~ Mean Scale Score ~ Asian')
plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.ylim((680, 708)) 
plt.show()

#Barplot AllGrades~AllCategory~AllYear~Mean
mean_category=pd.DataFrame(df_allgrades.groupby('Category')['Number_Tested'].mean())
mean_category = mean_category.assign(Cat=["Asian", "Black", "Hispanic", "White"])
for col in ['Cat']:
    mean_category[col] = mean_category[col].astype('category')
mean_category.dtypes

plt.bar(mean_category.Cat, mean_category.Number_Tested, label = "All Grades")
plt.title('All Grades~All Year per Category')
plt.xlabel('Category')
plt.ylabel('Mean Number Tested')
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Boxplot
sns.boxplot(df_grades_asian.Category=="Asian", df_grades.Level_4_P)
plt.title('All Grades per Year ~ Level_4_P')
plt.show()

#Lineplot Asian ~ Level 4
plt.plot(grades_2006_asian.Grade, grades_2006_asian.Level_4_P, label = "2006")
plt.plot(grades_2007_asian.Grade, grades_2007_asian.Level_4_P, label = "2007")
plt.plot(grades_2008_asian.Grade, grades_2008_asian.Level_4_P, label = "2008")
plt.plot(grades_2009_asian.Grade, grades_2009_asian.Level_4_P, label = "2009")
plt.plot(grades_2010_asian.Grade, grades_2010_asian.Level_4_P, label = "2010")
plt.plot(grades_2011_asian.Grade, grades_2011_asian.Level_4_P, label = "2011")
plt.legend()
plt.title('Grades per Year ~ Number Tested ~ Asian')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()


#Bar Plot  Asian ~ Level 4 & Number tested

plt.bar(grades_2006_asian.Grade,grades_2006_asian.Level_4_P, label = "2006")
plt.title('Grades ~ Level 4 ~ 2006')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2006_asian.Grade,grades_2006_asian.Number_Tested, label = "2006")
plt.title('Grades ~ Number Tested ~ 2006')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2006_asian.Grade, grades_2006_asian.Level_4_P, label = "2006")
plt.title('Grades ~ Level 4 ~ 2006')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2006_asian.Grade, grades_2006_asian.Number_Tested, label = "2006")
plt.title('Grades ~ Number Tested ~ 2006')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.bar(grades_2007_asian.Grade, grades_2007_asian.Level_4_P, label = "2007")
plt.title('Grades ~ Level 4 ~ 2007')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2007_asian.Grade,grades_2007_asian.Number_Tested, label = "2007")
plt.title('Grades ~ Number Tested ~ 2007')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2007_asian.Grade, grades_2007_asian.Level_4_P, label = "2007")
plt.title('Grades ~ Level 4 ~ 2007')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2007_asian.Grade, grades_2007_asian.Number_Tested, label = "2007")
plt.title('Grades ~ Number Tested ~ 2007')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.bar(grades_2008_asian.Grade, grades_2008_asian.Level_4_P, label = "2008")
plt.title('Grades ~ Level 4 ~ 2008')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2008_asian.Grade,grades_2008_asian.Number_Tested, label = "2008")
plt.title('Grades ~ Number Tested ~ 2008')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2008_asian.Grade, grades_2008_asian.Level_4_P, label = "2008")
plt.title('Grades ~ Level 4 ~ 2008')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2008_asian.Grade, grades_2008_asian.Number_Tested, label = "2008")
plt.title('Grades ~ Number Tested ~ 2008')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.bar(grades_2009_asian.Grade, grades_2009_asian.Level_4_P, label = "2009")
plt.title('Grades ~ Level 4 ~ 2009')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2009_asian.Grade,grades_2009_asian.Number_Tested, label = "2009")
plt.title('Grades ~ Number Tested ~ 2009')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2009_asian.Grade, grades_2009_asian.Level_4_P, label = "2009")
plt.title('Grades ~ Level 4 ~ 2009')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2009_asian.Grade, grades_2009_asian.Number_Tested, label = "2009")
plt.title('Grades ~ Number Tested ~ 2009')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.bar(grades_2010_asian.Grade, grades_2010_asian.Level_4_P, label = "2010")
plt.title('Grades ~ Level 4 ~ 2010')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2010_asian.Grade,grades_2010_asian.Number_Tested, label = "2010")
plt.title('Grades ~ Number Tested ~ 2010')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2010_asian.Grade, grades_2010_asian.Level_4_P, label = "2010")
plt.title('Grades ~ Level 4 ~ 2010')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2010_asian.Grade, grades_2010_asian.Number_Tested, label = "2010")
plt.title('Grades ~ Number Tested ~ 2010')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.bar(grades_2011_asian.Grade, grades_2011_asian.Level_4_P, label = "2011")
plt.title('Grades ~ Level 4 ~ 2011')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.ylim((20,70)) 
plt.show()

plt.bar(grades_2011_asian.Grade,grades_2011_asian.Number_Tested, label = "2011")
plt.title('Grades ~ Number Tested ~ 2011')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.ylim((9200,10500)) 
plt.show()

#Line Plot
plt.plot(grades_2011_asian.Grade, grades_2011_asian.Level_4_P, label = "2011")
plt.title('Grades ~ Level 4 ~ 2011')
plt.xlabel('Grade')
plt.ylabel('Level 4 Percentage')
plt.show()

plt.plot(grades_2011_asian.Grade, grades_2011_asian.Number_Tested, label = "2011")
plt.title('Grades ~ Number Tested ~ 2011')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()

#All grades

plt.plot(grade_3.Year, grade_3.Number_Tested, label = "Grade 3")
plt.plot(grade_4.Year, grade_4.Number_Tested, label = "Grade 4")
plt.plot(grade_5.Year, grade_5.Number_Tested, label = "Grade 5")
plt.plot(grade_6.Year, grade_6.Number_Tested, label = "Grade 6")
plt.plot(grade_7.Year, grade_7.Number_Tested, label = "Grade 7")
plt.plot(grade_8.Year, grade_8.Number_Tested, label = "Grade 8")
plt.legend()
plt.title('Grades ~ Number Tested ~ All Year')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()

plt.plot(grade_3.Year, grade_3.Level_4_P, label = "Grade 3")
plt.plot(grade_4.Year, grade_4.Level_4_P, label = "Grade 4")
plt.plot(grade_5.Year, grade_5.Level_4_P, label = "Grade 5")
plt.plot(grade_6.Year, grade_6.Level_4_P, label = "Grade 6")
plt.plot(grade_7.Year, grade_7.Level_4_P, label = "Grade 7")
plt.plot(grade_8.Year, grade_8.Level_4_P, label = "Grade 8")
plt.legend()
plt.title('Grades ~ Level_4_P ~ All Year')
plt.xlabel('Grade')
plt.ylabel('Level_4_P')
plt.show()


plt.plot(grade_3.Year, grade_3.Number_Tested, label = "Grade 3")
plt.legend()
plt.title('Grades ~ Number Tested ~ All Year')
plt.xlabel('Grade')
plt.ylabel('Number Tested')
plt.show()


plt.plot(grade_3.Year, grade_3.Level_4_P, label = "Grade 3")
plt.legend()
plt.title('Grades ~ Level_4_P ~ All Year')
plt.xlabel('Grade')
plt.ylabel('Level_4_P')
plt.show()
