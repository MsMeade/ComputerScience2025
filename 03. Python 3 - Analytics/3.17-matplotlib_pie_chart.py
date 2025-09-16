import matplotlib.pyplot as plt
numBS = [1, 2.5, 4, 3, 2.5, 2]
names = ["Joe Bloggs", "Mary Murphy",
"Claire Whelan", "Mike Fahey",
"Gillian Marks", "Arya Quille"]
plt.pie(numBS, labels=names)
plt.title("Brothers and Sisters")
plt.show()
