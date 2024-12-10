import matplotlib.pyplot as plt
numBS = [1, 2.5, 4, 3, 2.5, 2]
ages = [17, 18, 16, 18, 17, 17]
names = ["Joe Bloggs", "Mary Murphy",
"Claire Whelan", "Mike Fahey",
"Gillian Marks", "Arya Quille"]
plt.plot(names, numBS)
plt.plot(ages)
plt.legend(["Num Brothers and Sisters",
"Age"])
plt.title("Brothers and Sisters")
plt.xlabel("Student")
plt.ylabel("Num Brothers and Sisters")
plt.show()
