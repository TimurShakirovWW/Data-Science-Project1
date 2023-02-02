#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DataAnalyst.csv")
def clearSAl(salary): 
    salary = str(salary)
    res = salary.replace("(Glassdoor est.)", "")
    return res

a = "-1"
def check(salary):
    if a == salary:
        return ("$61K-$61K")
    return salary

def dropDollar(salary): #удаление символов в середине и в конце(K, $, -)    
    res1 = salary.replace("$", "")
    res2 = res1.replace("K", "000")
    data = res2.split("-") 
    data = list(map(int, data))
    data2 = (data[0] + data[-1]) / 2
    return data2


df["Salary Estimate"] = df["Salary Estimate"].apply(clearSAl)
df["Salary Estimate"] = df["Salary Estimate"].apply(check)
df["Salary Estimate"] = df["Salary Estimate"].apply(dropDollar)
#1
print(df["Salary Estimate"].max()) #150 000.0
#print(df["Location"].head())
#pieloc = df["Location"].value_counts().plot(kind = "pie")
temp = df[df['Salary Estimate'] >= 100000.0]['Location'].value_counts().plot(kind = "pie")
plt.show()
#print(temp.head(1000000))

#2
temp = df[df['Salary Estimate'] >= 100000.0]['Easy Apply'].value_counts().plot(kind = "pie")
plt.show()
#print(temp.head(1000000))

#3
def competitortolist(competitors):
    competitors = str(competitors)
    if competitors != "-1":
        return len(competitors.split(", "))
    return 0

df["CompetitorsLEN"] = df["Competitors"].apply(competitortolist)
temp = df[df['Salary Estimate'] >= 100000.0][df["CompetitorsLEN"] >= 0]
temp = df[df['Salary Estimate'] >= 100000.0]['CompetitorsLEN'].value_counts().plot(kind = "pie")
plt.show()
#print(len(temp))

#4
def findTitle(Title):
    Title = str(Title)
    Title = Title.lower()
    TitlefindSen = Title.find("senior")
    TitlefindMid = Title.find("mid")
    TitlefindJun = Title.find("jun")
    if TitlefindSen > -1:
        return "Senior"
    elif TitlefindMid > -1:
        return "Middle"
    elif TitlefindJun > -1:
        return "Junior"
    
df["NewTitle"] = df["Job Title"].apply(findTitle)

temp = df[df['Salary Estimate'] >= 100000.0]['NewTitle'].value_counts().plot(kind = "pie")
plt.show()

#5
temp = df[df['Salary Estimate'] >= 100000.0]['Rating'].value_counts().plot(kind = "pie")
plt.show()

print("ВЫВОД")
print("1 - зависит от местоположения. Города, в которых самая большая зп: New York., San francisco, CA., Chicago, IL., San jose, CA")
print("2 - Кнопка \"easy apply\" не влияет на ЗП.")
print("3 - Чем больше конкурентов у компании, где работает человек, тем меньше шансов получить ЗП выше $100к")
print("4 - ЗП data analyst зависит от комбинаций навыков")
print("5 - Чем выше рейтинг от работодателя , тем выше ЗП(-1 в круговой диаграмме - это неуказанный рейтинг)")


