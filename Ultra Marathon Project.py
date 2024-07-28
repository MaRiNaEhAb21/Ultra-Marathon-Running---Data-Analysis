#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


df=pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


#clean up data


# In[8]:


df[df['Event distance/length']== '50mi']


# In[9]:


df[df['Event distance/length'].isin(['50mi','50km'])]


# In[10]:


df[(df['Event distance/length'].isin(['km','50mi']))& (df['Year of event']==2020)]


# In[11]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA']


# In[12]:


df2 = df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[13]:


df2.head(10)


# In[14]:


df2['Event name']=df2['Event name'].str.split('(').str.get(0)


# In[15]:


df2.head()


# In[16]:


df2.shape


# In[17]:


df2['athlete_age']=2020-df['Athlete year of birth']


# In[18]:


df2['Athlete performance']=df2['Athlete performance'].str.split(' ').str.get(0)


# In[19]:


df2.head()


# In[20]:


#drop columns(country,club,age category,yearof birth)


# In[21]:


df2=df2.drop(['Athlete club','Athlete country','Athlete age category','Athlete year of birth'],axis=1)


# In[22]:


df2.head()


# In[23]:


#check foe null values


# In[24]:


df2.isna().sum()


# In[25]:


df2[df2['athlete_age'].isna()==1]


# In[26]:


df2=df2.dropna()


# In[27]:


df2.isna().sum()


# In[28]:


#check for duplicates


# In[29]:


df2[df2.duplicated()==True]


# In[30]:


#reset index


# In[31]:


df2.reset_index(drop = True)


# In[32]:


#fix data types


# In[33]:


df2.dtypes


# In[34]:


df2['athlete_age']= df2['athlete_age'].astype(int)


# In[38]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[39]:


df2.dtypes


# In[ ]:


#rename columns


# In[43]:


df2 = df2.rename(columns={
    'Year of event': 'year',
    'Event dates': 'race_day',
    'Event name': 'race_name',
    'Event distance/length': 'race_length',
    'Event number of finishers': 'race_number_of_finishers',
    'Athlete performance': 'athlete_performance',
    'Athlete gender': 'athlete_gender',
    'Athlete average speed': 'athlete_average_speed',
    'Athlete ID': 'athlete_id',
    'athlete_age': 'athlete_age'
})


# In[48]:


df2.head()


# In[50]:


df3 = df2[['year','race_day','race_name','race_length','race_number_of_finishers','athlete_performance','athlete_gender','athlete_average_speed','athlete_id','athlete_age']]


# In[55]:


df3.head()


# In[56]:


df3['race_name'].value_counts()


# In[ ]:


#charts


# In[58]:


sns.histplot(df3['race_length'])


# In[93]:


race_gend=pd.crosstab(index=df3['race_length'],columns=df3['athlete_gender'])
race_gend


# In[94]:


race_gend.plot(kind='bar',title='Race length wise Gender Distribution',ylabel='Count',xlabel='Race Length')


# In[62]:


sns.displot(df3[df3['race_length']=='50mi']['athlete_average_speed'])


# In[95]:


sns.violinplot(data = df3 , x = 'race_length' , y = 'athlete_average_speed', hue='athlete_gender',split=True,)


# In[71]:


sns.lmplot(data=df3 , x='athlete_age',y='athlete_average_speed',hue='athlete_gender')


# In[ ]:


#some analysis on data set


# In[70]:


df3.groupby(['race_length','athlete_gender'])['athlete_average_speed'].mean()


# In[83]:


df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean', 'count']).sort_values(by='mean', ascending=False).query('count > 10')


# In[90]:


df3['race_name'].value_counts().head(10).plot(kind='bar',title='No of Participants',xlabel='Event Name',ylabel='Participant number',figsize=(10,6),color='lightblue')


# In[ ]:




