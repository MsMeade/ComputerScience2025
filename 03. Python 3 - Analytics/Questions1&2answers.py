#Question 1
import statistics
ages=[32,31,30,37,37,33]

minimum=min(ages)
print(minimum)

maximum=max(ages)
print(maximum)


mean= statistics.mean(ages)
print(mean)

mean2= sum(ages)/len(ages)
print(mean2)


#Question2
import statistics
List=[1,9,3,2,3,7,6,5,8,9,1,10]

minimum=min(List)
print(minimum)

maximum=max(List)
print(maximum)

mean= statistics.mean(List)
median = statistics.median(List)
mode= statistics.mode(List)
print(mean)
print(median)
print(mode)

#frequency
# Build up a list of unique values
unique_values = []
for value in List:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = List.count(value)
    frequencies.append(frequency)
print(frequencies)
