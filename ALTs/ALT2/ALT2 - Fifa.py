import pandas
import statistics
#df - data frame common name for this variable
#Import csv data
fifadf= pandas.read_csv('Fifa23.csv')

#This will print the data base
#print(fifadf)

#Choose the data you want to work with
#print(fifadf[['Position','Height', 'Value']])

#print specific rows:
#print(fifadf.loc[10])

# print rows between with specific columns:
#print(fifadf.loc[100:105],['Position','Height', 'Value'])


#Make any column into a list.
#clubList = fifadf['Club'].tolist()
#print(clubList)

#you are ready to analyse! e.g. mode
#modeClub=statistics.mode(clubList)
#print(modeClub)