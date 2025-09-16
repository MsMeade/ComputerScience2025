#Import csv data
import statistics
import pandas
import matplotlib.pyplot as plt
carsdf=pandas.read_csv('Car.csv',encoding='Latin1')

#This will print the data base
#print(carsdf)
 
#Choose the data you want to work with
#print(carsdf[['Make','Model','Engine Size(L)']])

#print specific rows:
#print(carsdf.loc[10])

# print rows between with specific columns:
#print(carsdf.loc[100:105],['Make','Model','Engine Size(L)'])


#Make any column into a list.
#carModelList = carsdf['Model'].tolist()
#print(carModelList)

#you are ready to analyse! e.g. sort
#carModelList.sort()
#print(carModelList)