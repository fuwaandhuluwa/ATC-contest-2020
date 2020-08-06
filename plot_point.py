import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

file = open(input("Filename:"))
all_lines = file.readlines()

line = file.readline()

x = []
y = []

for line in all_lines:
    line = line.strip("\n")
    x.append(int(line.split(',')[0]))
    y.append(int(line.split(',')[1]))

file.close()

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.grid(True)

plt.title('Points',fontsize=24)
plt.xlabel('X',fontsize=14)
plt.ylabel('Y',fontsize=14)


ax=plt.gca()
plt.show()
