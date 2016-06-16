# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn import datasets
import Levenshtein as lv
from fuzzywuzzy import fuzz

# Exporting Users.csv from database
users_df = pd.read_csv('user.csv')
print(users_df.head())
          #Trying to set ID as primary key for pandas
          #users_df.set_index('ID',inplace=True)
          #print(users_df.head())
users_df=users_df.iloc[0:len(users_df),1:len(users_df.columns)]  # Truncates the original dataframe to drop ID column

columns_to_drop=['object','name','password','image','token','bio','ts_deleted']

users_df=users_df.drop(columns_to_drop,axis=1)

#Create New User details whose similarity is to be observed
newUser_df = pd.read_csv('new_user.csv')

#List of numerical and categorical categories(columns)
num_cat=['zip','last_login','last_active','user_type','created']
str_cat=[]
for col in users_df.columns:
      ans=num_cat.index(col) if col in num_cat else None
      if ans is None:
##          print col
           print "This is a string category "+col #Debug Note
##           users_df[col].apply(lv.distance(,newUser_df[col]),axis=1)
           users_df[col]=users_df.apply(lambda x:fuzz.ratio(x[col],newUser_df[col]),axis=1)
  
      else:
               print "This is a numerical category "+col #Debug Note
               users_df[col]='Mohit'
