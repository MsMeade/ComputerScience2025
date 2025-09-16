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

yearList=emissionsdf['Year'].tolist()
yearList.sort()
print(yearList)
print(statistics.mean(yearList))
print(yearList.count(2008))

for i in yearList:
    if i < 2007:
        yearList.remove(i)
print(yearList)

        
unique_values = []
for value in yearList:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = yearList.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]


print(frequencies)
print(max_frequency)
print(mode)
