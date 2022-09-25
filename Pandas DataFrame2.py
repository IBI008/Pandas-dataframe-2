#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas
import pandas as pd

# create a dataframe from a dictionary

data = {'Name': ['Shen Lee','Leon Buhle','Tracy Adams',
                 'Lebo Sinuka','Lauren Pierce','Monika Bond',
                'Natahs Allsop','Nicholas Winter',
                'Christopher Eckson','Siobhan Omalley'],
       'Annual': [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
       'Sick': [10, 8, 10, 9, 7, 10, 9, 10, 8, 5],
       'Personal': [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
       'Bonus': [3, 0, 0, 3, 3, 6, 0, 3, 6, 3]}
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns=['Name','Annual',
                                         'Sick','Personal','Bonus'],
                           index = row_labels)
leave_cycle.index.name = 'personnel_ID'

# View DataFrame
leave_cycle


# In[2]:


data = {'Name': ['Shen Lee','Leon Buhle','Tracy Adams',
                 'Lebo Sinuka','Lauren Pierce','Monika Bond',
                'Natahs Allsop','Nicholas Winter',
                'Christopher Eckson','Siobhan Omalley'],
       'Annual': [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
       'Sick': [10, 8, 10, 9, 7, 10, 9, 10, 8, 5],
       'Personal': [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
       'Bonus': [3, 0, 0, 3, 3, 6, 0, 3, 6, 3],
       'Total leave taken': [0, 3, 5, 10, 5, 8, 11, 9, 15, 5],
       'Total leave available': [38, 32, 30, 28, 33, 33, 24, 29, 26, 33],
       'Annual Total': [38, 35, 35, 38, 38, 41, 35, 38, 41, 38]}
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]
leave_cycle = pd.DataFrame(data, columns=['Name','Annual',
                                         'Sick','Personal','Bonus',
                                         'Total leave taken',
                                          'Total leave available'],
                           index = row_labels)
leave_cycle.index.name = 'Personal_ID'

# View DataFrame
leave_cycle


# In[ ]:




