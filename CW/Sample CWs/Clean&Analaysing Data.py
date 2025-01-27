import csv
import statistics
import pygal

#BR1a&b
file = open("rawdata.csv","r") 		#read in csv data
records = list(csv.reader(file)) 	#make a list of the records
file.close() 						#close the file

for record in records:
    record[4]=(round(float(record[4]),1))	#round the index 4 of each record to 1 decimal place
    record[3]=record[3].replace("Millimetres","mm") #replace the string "Millimeters" in record index with "mm" 
    #record[1]=record[1].split(" ") #this is used to split up items in a list... not relevent for this project

malin_list=[]			#open a new list for malin
valentia_list=[]		#open a new list for valentia
mullingar_list=[]		#open a new list for mullingar


for i in range(1,390,3):				#put every 3rd record in malin list (start at 1)
    malin_list.append((records[i]))
print(malin_list)

for i in range(2,390,3):
    valentia_list.append((records[i])) #put every 3rd record in valentia list (start at 2)
print(valentia_list)
  
for i in range(3,390,3):
    mullingar_list.append((records[i])) #put every 3rd record in mullingar list (start at 3)
print(mullingar_list)

#------------------------------------------------------------------------------------------------------------------------#

file = open("cleandata.csv","a",newline="") #make a new csv file for all of my clean data
db = csv.writer(file)

for record in malin_list: #add in all of the malin records
    db.writerow(record)

for record in valentia_list: #add in all of the valentia records
    db.writerow(record)

for record in mullingar_list: #add in all of the mullingar records
    db.writerow(record)

file.close() #close file

#----------------------------------------------------------------------------------------------------------#

file = open("cleandata.csv","r")
records = list(csv.reader(file))
file.close()
#for record in records:
#    print(record)

# print("Year & Month\t Location \t Percipitation Amount \t Unit of Measure")
# print("-------------------------------------------------------------------")
# for record in records:
#     print(record[1],"\t\t", record[2],"\t\t", record[4], "\t",record[3])

# ----------------------------------------------------------------------------------------------------#

#Below I am making a list of all of the years and months in "date_list" and percipitation levels in each of the other three lists.
#record[4] corresponds to the 5th column in the csv file.

date_list=[]
for record in malin_list:
    date_list.append(str(record[1]))

malin_percip= []
for record in malin_list:
    malin_percip.append(float(record[4]))
print(malin_percip)

valentia_percip= []
for record in valentia_list:
    valentia_percip.append(float(record[4]))
print(valentia_percip)

mullingar_percip= []
for record in mullingar_list:
    mullingar_percip.append(float(record[4]))
print(mullingar_percip)

# print(len(date_list))
# print(len(mullingar_percip))
# print(len(malin_percip))
# print(len(valentia_percip))


#Below I am making a list of the total percipitation levels by adding the three percipitation values in each list.

total_percip=[]
for i in range(0,129):
    total_percip.append(float((mullingar_percip[i])+(valentia_percip[i])+(malin_percip[i])))
print(total_percip)


#------------------------------------------------------------------------------------------------------------------#
#BR2a,b & c

# Find the maximum value in the  mullingar list
mull_max = (max(mullingar_percip))
mull_max_index=(mullingar_percip.index(max(mullingar_percip)))
print("Maximum percipitation in Mullingar:", mull_max)
print("This occurred in ",date_list[mull_max_index])

# Find the minimum value in the valentia list
val_min = (min(valentia_percip))
val_min_index=(valentia_percip.index(max(valentia_percip)))
print("Minimum percipitation in Valentia:", val_min)
print("This occurred in ",date_list[val_min_index])


# Calculate the range for Malin (max - min) 
malin_range = (max(malin_percip) - min(malin_percip))
print("Range of percipitation in malin was:", malin_range, "mm")

# Calculate the mean (average) of the total Percipitations
mean_percip = sum(total_percip) / len(total_percip)
print("the average percipitation was:", mean_percip)

# Calculate the median of the total Percipitations
median_percip = statistics.median(total_percip)
print("Median percipitation:", median_percip)

# Calculate the mode of the total Percipitations
mode_percip = statistics.mode(total_percip)
print("Mode percip:", mode_percip)

#-----------------------------------------------------------------------------------------------------------------------------------------#

# Bar Chart
bar_chart = pygal.Bar()
bar_chart.title = 'Mullingar Percipitation 2023 - 2024'   #title of the graph
bar_chart.x_title='Month & Year'						#title of the x-axis
bar_chart.y_title= 'Percipitation (mm)'					#title of the y-axis
for i in range(107,129):								# I picked this range to incorperate the 2023 and 2024 readings only.
    bar_chart.add(date_list[i], mullingar_percip[i])
bar_chart
bar_chart.render_to_file('bar_chart.svg')  # Save Bar Chart as SVG
 
# Line Graph
line_chart = pygal.Line()
line_chart.title = 'Malin Head Percipitation'
line_chart.x_labels = date_list
line_chart.add('Values', malin_percip)
line_chart.render_to_file('line_chart.svg')  # Save Line Graph as SVG


# Scatter Plot- DOESNT MAKE SENSE FOR THIS DATA
# scatter_plot = pygal.XY(stroke=True)
# scatter_plot.title = 'Malin vs Valentia'
# # (x, y) pairs
# scatter_data = list(zip(malin_percip, valentia_percip))
# scatter_plot.add('Data Points', scatter_data)
# scatter_plot.render_to_file('scatter_plot.svg')  # Save Scatter Plot as SVG

# Pie Chart
pie_chart = pygal.Pie()
pie_chart.title = 'Pie chart of percipitation Oct 2024'
pie_chart.add('Malin Percipitation', malin_percip[129])
pie_chart.add('Mullingar Percipitation', mullingar_percip[128])
pie_chart.add('Valentia Percipitation', valentia_percip[129])
pie_chart.render_to_file('pie_chart.svg')  # Save Pie Chart as SVG
