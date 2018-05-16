
# coding: utf-8

# In[1138]:


import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
import  plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='ekama0731', api_key='7tXR22tn4cwoY1sf8kZn')


# In[1139]:


glassdoor = pd.read_csv('./Desktop/glassdoor/glassdoor.csv')


# In[1140]:


# originally had city and state in job location as a string
# i split the city and state and created a new column for both values

glassdoor['city'] = glassdoor.job_location.str.split(',').str[0]
glassdoor['state'] = glassdoor.job_location.str.split(',').str[1]


# In[1141]:


# dropped job location bc i created a seperate city and state column
glassdoor = glassdoor.drop(columns = 'job_location')


# In[1142]:


# a few cities were represented as states, so I changed those cities to states
glassdoor['state'][glassdoor['state'] == ' Los Angeles'] = ' CA'


# In[1143]:


# with glassdoor, some companies had information about salaries, so the companies that didn't have information
# i changed any value to a none value 
glassdoor.salary_estimate[glassdoor.salary_estimate == "Error - NO SALARY INFORMATION"] = None
glassdoor.salary_low[glassdoor.salary_low == "Error - NO SALARY INFORMATION"] = None
glassdoor.salary_high[glassdoor.salary_high == "Error - NO SALARY INFORMATION"] = None


# In[1144]:


# company info was a large list of tuples
# to retrieve which industry the job posting was for, i had to create the parse funciton below

def parse(string):
    new_val = str(string).split("Industry")[-1].split(")")[0].replace(",","").replace("'", "").lstrip()
    if "[" in new_val:
        return None
    elif "Company" in new_val:
        return None
    else:
        return new_val

glassdoor["industry"] = glassdoor["company_info"].apply(parse)


# In[1145]:


# information was extracted and placed into column industry
glassdoor = glassdoor.drop(columns = 'company_info')


# In[1146]:


# with glassdoor, some companies had information about which industry the job was in, so the companies that didn't have this information
# i changed any value to a none value 
glassdoor['industry'][glassdoor.industry == 'Unknown'] = None
glassdoor['industry'][glassdoor.industry == 'nan'] = None
glassdoor['industry'][glassdoor.industry == ''] = None


# In[1147]:


# Converting any salary that's a string into a float
# Converting all salarys to salary per year
glassdoor['salary_estimate'] = glassdoor['salary_estimate'].str.replace(',','').astype(float)


# In[1148]:


glassdoor['salary_low'] = glassdoor['salary_low'].str.replace('$','')
glassdoor['salary_high'] = glassdoor['salary_high'].str.replace('$','')


# In[1149]:


# removing the K from my salaries and replacing it with '000' to represent thousands
glassdoor['salary_low'] = glassdoor['salary_low'].str.replace('k','000').astype(float)
glassdoor['salary_high'] = glassdoor['salary_high'].str.replace('k','000').astype(float)


# In[1150]:


def perYear(x):
    if x<100:
        return x*8*5*4*12
    else:
        return x
    
glassdoor['salary_estimate'] = glassdoor['salary_estimate'].apply(perYear)
glassdoor['salary_high'] = glassdoor['salary_high'].apply(perYear)
glassdoor['salary_low'] = glassdoor['salary_low'].apply(perYear)


# In[1151]:


# removing nan values 
glassdoor['salary_estimate'] = glassdoor.loc[:,'salary_estimate'].interpolate()
glassdoor['salary_high'] = glassdoor.loc[:,'salary_high'].interpolate()
glassdoor['salary_low'] = glassdoor.loc[:,'salary_low'].interpolate()
glassdoor['rating'] = glassdoor.loc[:, 'rating'].interpolate()


# In[1152]:


# removing single nan values
glassdoor = glassdoor.dropna(subset = ['job_title', 'salary_estimate', 'salary_low', 'salary_high'])


# In[1169]:


import wordcloud
from wordcloud import WordCloud

wc_titles = ''.join(glassdoor['job_title'])

wc1 = WordCloud().generate(wc_titles)
wc1.to_image()


# In[1170]:


glassdoor.to_csv('bathroom.csv')

