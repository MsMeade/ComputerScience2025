import pandas
import statistics
#df - data frame common name for this variable
#Import csv data
emissionsdf = pandas.read_csv('emissions.csv')

#This will print the data base
#print(emissionsdf)

#Choose the data you want to work with
#print(emissionsdf[['Country','Year', 'Emissions.CO2']])

#print specific rows:
#print(emissionsdf.loc[10])

# print rows between with specific columns:
#print(emissionsdf.loc[100:105],['Country','Year', 'Emissions.CO2'])

#Make any column into a list.
#countryList = emissionsdf['Country'].tolist()
#print(countryList)

#you are ready to analyse! e.g. sort
#countryList.sort(reverse=True)
#print(countryList)