import matplotlib.pyplot as plt 

x=[]
y=[]
file = open(input("fileName:"))
all_lines = file.readlines()

line = file.readline()
i = 0

for line in all_lines:
    line = line.strip("\n")
    line = line.split(";")
    x=[]
    y=[]
    j = 0
    for point in line:
        x.append(int(point.split(',')[1]))
        y.append(int(point.split(',')[0]))
        j += 1

    num = ''
    if j == 1:
        i += 1
        num = str(i)
        plt.text(x[0], y[0], num,ha='center', va='center', fontsize=8, bbox=dict(boxstyle="square",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))
    
    plt.plot(x,y)
    plt.scatter(x,y)
        


file.close()
ax = plt.gca()
ax.invert_yaxis()
ax.xaxis.set_ticks_position('top')
plt.title('Points',fontsize=24)
plt.xlabel('Y',fontsize=14)
plt.ylabel('X',fontsize=14)


plt.grid(True)
plt.show()
