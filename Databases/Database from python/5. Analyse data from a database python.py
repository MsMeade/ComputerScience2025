import csv
import statistics
import matplotlib.pyplot as plt

file = open("patients.csv","r")
records = list(csv.reader(file))
file.close()

name_list=[]
for record in records:
    name_list.append(str(record[1]))

age_list= []
for record in records:
    age_list.append(float(record[4]))
print(age_list)

# Sort the age_list in ascending order
age_list.sort()
print("Sorted list:", age_list)

# Find the maximum value in the age_list
max_age = (max(age_list))
print("Maximum age:", max_age)

# Find the minimum value in the age_list
min_age = (min(age_list))
print("Minimum age:", min_age)

# Calculate the range (max - min) of the age_list
age_range = (max_age - min_age)
print("Range of ages:", age_range)

# Calculate the mean (average) of the age_list
mean_age = sum(age_list) / len(age_list)
print("Mean age:", mean_age)

# Calculate the median of the age_list
median_age = statistics.median(age_list)
print("Median age:", median_age)

# Calculate the mode of the age_list
try:
    mode_age = statistics.mode(age_list)
    print("Mode age:", mode_age)
except statistics.StatisticsError:
    print("No unique mode in the list")

# Create a bar chart of the age_list
plt.bar(name_list, age_list)
plt.title('Age & Name Bar Plot')
plt.xlabel('Name')
plt.ylabel('Age')
plt.grid(True)
plt.show()