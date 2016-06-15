# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn import datasets


# Exporting Users.csv from database
users_df = pd.read_csv('user.csv')
print(users_df.head())
          #Trying to set ID as primary key for pandas
          #users_df.set_index('ID',inplace=True)
          #print(users_df.head())
users_df=users_df.iloc[0:len(users_df),1:len(df.columns)]  # Truncates the original dataframe to drop ID column





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
          
 
