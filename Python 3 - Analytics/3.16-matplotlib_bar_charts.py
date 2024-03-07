import matplotlib.pyplot as plt
numBS = [1, 2.5, 4, 3, 2.5, 2]
names = ["Joe Bloggs","Mary Murphy",
"Claire Whelan","Mike Fahey",
"Gillian Marks", "Arya Quille"]
plt.bar(names, numBS)
#plt.scatter(names, numBS)
plt.title("Brothers and Sisters")
plt.xlabel("Student")
plt.ylabel("Num Brothers and Sisters")
plt.show()
