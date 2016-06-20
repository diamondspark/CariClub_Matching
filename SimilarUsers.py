# Importing necessary libraries
import pandas as pd
import numpy as np
import Levenshtein as lv
from sklearn import preprocessing
from fuzzywuzzy import fuzz

#Function Definitions
def dateTimeDifference(dateTime1,dateTime2):
      '''Helper method to handle date and time difference between events
         for example differnce between 2 last logins
      '''
      return pd.Timestamp(dateTime2)-pd.Timestamp(dateTime1)

def numericalDifference(num1,num2):
      '''Helper method to calculate difference between 2 numerical categories
      '''
      return abs(num1-num2)

def scaledNormalize(val,minimum,range_):
      return 100*(val-minimum)/range_

def printData(data):
      'Helper method to print data'
      print data
      return

# Exporting databases
users_df = pd.read_csv('user.csv')
newUser_df = pd.read_csv('new_user.csv')
          #Trying to set ID as primary key for pandas
          #users_df.set_index('ID',inplace=True)
          #print(users_df.head())
users_df=users_df.iloc[0:len(users_df),1:len(users_df.columns)]  # Truncates the original dataframe to drop ID column

columns_to_drop=['Org authorized','Employed by partner']

users_df=users_df.drop(columns_to_drop,axis=1)
newUser_df=newUser_df.drop(columns_to_drop,axis=1)

#List of numerical,date and categorical categories(columns).
#Make keywords/interest as binart feature.
num_cat=['zip','Type']
date_cat=['created','dob','Updated at']
str_cat=['firstname','lastname','email','Organization','Job function','location','School 1','School 2','School 3','Past Organization1','Role at past organization 1','Past Organization2','Role at past organization 2','Past Organization3','Role at past organization 3','keyword1','keyword2','keyword3','keyword4','keyword5','keyword6']
#Calculated similarity for each entry in users_df with newUser_df
#and converted into a numeric dataframe to apply Machine Learning algorithms.
#Used fuzzywuzzy which is based on calculating Levenshtein distance between Strings.
#The similarity for already numeric categories (columns) were calculated based on Euclidean distance.
for col in users_df.columns:
      if col in str_cat:
           print "This is a string category "+col #Debug Note
           users_df[col]=users_df.apply(lambda x:fuzz.ratio(str(x[col]),newUser_df[col].iat[0]),axis=1)
      elif col in num_cat:
            print "This is a numerical category "+col #Debug Note
            users_df[col]=users_df.apply(lambda x:numericalDifference(x[col],newUser_df[col].iat[0]),axis=1)
            minimum= users_df[col].min()
            col_range= users_df[col].max()-users_df[col].min()
            if col_range==0:
                  users_df[col]=100
            else:
                 users_df[col]=users_df.apply(lambda x:scaledNormalize(x[col],minimum,col_range),axis=1)
      elif col in date_cat:
            print "This is a date category"+col # Debug Note
            users_df[col]=users_df.apply(lambda x:dateTimeDifference(newUser_df[col].iat[0],x[col]),axis=1)
                      


##
##def toNumericalDataFrame(user_df):
##     """Takes in as input a dataframe and converts all strigs present in df
##        into numerical data so that Euclidean distance can be used as a metric
##        for calculating similarity.
##     """
##
##def stringToNumber(str1):
##     """Helper function to convert String to a unique number
##     """
##      # Converts the String to Uppercase
##STR1 = str1.upper()
##h = 0
##for c in s:
##      h = (31 * h + ord(c)) & 0xFFFFFFFF
##return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000
##
##def remove_small_var_cols():
##
##     """remove columns that have variance less than a certain threshold. Columns with small values wont contain significant information
##     """
##     for col in df.columns:
          

