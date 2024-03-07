import pandas
import statistics
#df - data frame common name for this variable
#Import csv data
spotifydf=pandas.read_csv('spotify-2023.csv',encoding='Latin1')

#This will print the data base
#print(df)

#Choose the data you want to work with
#print(spotifydf[['track_name', 'artist(s)_name','streams']])

#print specific rows:
#print(spotifydf.loc[10])

# print rows between with specific columns:
#print(spotifydf.loc[100:105],['track_name', 'artist(s)_name','streams'])

#Make any column into a list.
#trackNameList = spotifydf['track_name'].tolist()
#print(trackNameList)

#you are ready to analyse! e.g. sort
#trackNameList.sort()
#print(trackNameList)