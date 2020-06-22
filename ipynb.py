#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install -c anaconda beautifulsoup4


# In[2]:


conda install -c anaconda beautifulsoup


# In[1]:


conda install -c anaconda lxml


# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas


# In[2]:


website_text = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(website_text,'xml')
table = soup.find('table',{'class':'wikitable sortable'})


# In[3]:


table_rows = table.find_all('tr')
data = []
for row in table_rows:
    td=[]
    for t in row.find_all('td'):
        td.append(t.text.strip())
    data.append(td)
df = pandas.DataFrame(data, columns=['PostalCode', 'Borough', 'Neighborhood'])


# In[4]:


df = df[~df['Borough'].isnull()]  # to filter out bad rows
df.drop(df[df.Borough == 'Not assigned'].index, inplace=True)
df.reset_index(drop=True, inplace=True)
df = df.groupby(['PostalCode','Borough'])['Neighborhood'].apply(lambda x: ','.join(x)).reset_index()
df['Neighborhood'].replace('Not assigned',df['Borough'],inplace=True)
df


# In[5]:


df.shape


# In[ ]:




