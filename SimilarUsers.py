# Importing necessary libraries
import pandas as pd
import numpy as np
import Levenshtein as lv
from sklearn import datasets


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

#Calculated similarity for each entry in users_df with newUser_df
#and converted into a numeric dataframe to apply Machine Learning algorithms.
#Used fuzzywuzzy which is based on calculating Levenshtein distance between Strings.
#The similarity for already numeric categories (columns) were calculated based on Euclidean distance.
for col in users_df.columns:
      ans=num_cat.index(col) if col in num_cat else None
      if ans is None:
           print "This is a string category "+col #Debug Note
           users_df[col]=users_df.apply(lambda x:fuzz.ratio(str(x[col]),newUser_df[col].iat[0]),axis=1)
      else:
               print "This is a numerical category "+col #Debug Note
     


def toNumericalDataFrame(user_df)
     """Takes in as input a dataframe and converts all strigs present in df
        into numerical data so that Euclidean distance can be used as a metric
        for calculating similarity.
     """

def stringToNumber(str1)
     """Helper function to convert String to a unique number
     """
      # Converts the String to Uppercase
      STR1 = str1.upper()
      h = 0
      for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
      return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def remove_small_var_cols()

     """remove columns that have variance less than a certain threshold. Columns with small values wont contain significant information
     """
     for col in df.columns:
          
 
