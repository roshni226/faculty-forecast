#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import numpy as np
import pickle


# ### Importing Original data of past retirements

# In[122]:


odf=pd.read_csv('data.csv')


# In[123]:


odf


# ### Feature Engineering for regression fitting

# In[124]:


df=odf.drop(['Unnamed: 0', 'FacultyId', 'Name'], axis=1)


# #### Splitting into features and dependent

# In[125]:


x1 = df.iloc[:, :-2]
x1['EndMonth']= odf['EndMonth']
y = df.iloc[:, 6]  # Dependent variable


# ### Encoding

# In[126]:


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
x1['DesignationEC'] = label_encoder.fit_transform(x1['Designation'])
x1['AreaOfSpecializationEC'] = label_encoder.fit_transform(x1['AreaOfSpecialization'])
x1['GenderEC'] = label_encoder.fit_transform(x1['Gender'])
x1['AppointmentTypeEC'] = label_encoder.fit_transform(x1['AppointmentType'])


# In[127]:


x=x1.drop(['Gender','Designation','AreaOfSpecialization','AppointmentType','EndMonth'],axis=1)


# ### Data Splitting for training and testing

# In[128]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Assume you have features 'x' and target variable 'y'
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


# #### Linear regression model

# In[158]:


# Create a linear regression model
regressor = LinearRegression()

# Fit the model to the training data
regressor.fit(X_train, y_train)

#Make pickle file of our model
pickle.dump(regressor,open("model.pkl","wb"))

# Make predictions on the testing data
y_pred = regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)


# ### Mean standard error in our prediction model

# In[130]:


mse


# #### Converting predicted values into whole numbers ( as they represent years)

# In[131]:


import math
y_pred1=[]
for i in y_pred:
    y_pred1.append(math.floor(i))


# In[132]:


from sklearn.metrics import accuracy_score

# Assuming you have predicted values y_pred and true values y_test
accuracy = accuracy_score(y_test, y_pred1)
accuracy


# ## Using our model

# In[133]:


ndf=pd.read_csv('dataForPrediction.csv')


# In[134]:


ndf


# In[135]:


x2=ndf.drop(['Unnamed: 0', 'FacultyId', 'Name'], axis=1)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
#x2['EndMonthEC'] = label_encoder.fit_transform(x2['EndMonth'])
x2['DesignationEC'] = label_encoder.fit_transform(x2['Designation'])
x2['AreaOfSpecializationEC'] = label_encoder.fit_transform(x2['AreaOfSpecialization'])
x2['GenderEC'] = label_encoder.fit_transform(x2['Gender'])
x2['AppointmentTypeEC'] = label_encoder.fit_transform(x2['AppointmentType'])
y=x2.drop(['Gender','Designation','AreaOfSpecialization','AppointmentType'],axis=1)


# In[148]:


final_pred = regressor.predict(y)
final_pred1=[]
for i in final_pred:
    final_pred1.append(math.floor(i))


# ### Final Predicted Years

# In[137]:


final_pred1


# ### Return count of potential vacancies in 2024

# In[138]:


curr_year =2024
vacancies=0
for i in final_pred1:
    if i == 2024:
        vacancies+=1
print(vacancies)


# In[139]:


ndf['EndYearPred']= final_pred1


# In[140]:


ndf


# In[141]:


ndf['Vacancies']= vacancies


# In[142]:


ndf


# In[150]:


ndf = ndf.drop('Vacancies', axis=1)
ndf


# In[151]:


vacancies = ndf.pivot_table(index=['EndYearPred','Designation'], columns='AreaOfSpecialization', aggfunc='size', fill_value=0)


# In[155]:


newdf=print(vacancies)


# In[ ]:





# In[ ]:





# In[ ]:




