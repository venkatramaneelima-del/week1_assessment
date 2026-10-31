#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('timeit', 'sum(range(1000))')


# In[6]:


get_ipython().run_line_magic('time', 'df.describe()')


# In[ ]:


import pandas as pd

df = pd.read_csv("../data/employees.csv")

df.head()


# In[ ]:


import pandas as pd
from pathlib import Path

files = list(Path.cwd().rglob("employees.csv"))

print("Current location:", Path.cwd())
print("CSV files found:", files)


# In[7]:


import pandas as pd

df = pd.read_csv("../week1_assessment/data/employees.csv")

df.head()


# In[8]:


# 1. Check dataset information
df.info()

# 2. Check number of rows and columns
print("Shape:", df.shape)

# 3. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Statistical summary
print("\nStatistical Summary:")
df.describe()


# In[9]:


# Department-wise employee count

department_count = df["department"].value_counts()

print("Employees in each department:")
print(department_count)


# In[10]:


import matplotlib.pyplot as plt

department_count = df["department"].value_counts()

plt.figure(figsize=(8, 5))
department_count.plot(kind="bar")

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)

plt.savefig("../reports/department_chart.png")
plt.show()


# In[11]:


# Average salary by department chart

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)

plt.savefig("../reports/average_salary_chart.png")
plt.show()


# In[ ]:





# In[12]:


# City-wise employee count

city_count = df["city"].value_counts()

plt.figure(figsize=(8, 5))
city_count.plot(kind="bar")

plt.title("Employees by City")
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)

plt.savefig("../reports/city_employee_chart.png")
plt.show()


# In[13]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# 
