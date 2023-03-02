result1 = []
result2 = []
result3 = []
result4 = []
initsize=0
k=0
#Specify dirsize in GB
dirsize=2.5
with open('datafile.txt', 'r') as f:
    for line in f:
	s = line.split(",", 1)[1]
        ad = float(s)
        initsize = float(ad) + float(initsize)
        print ("Init size is  " + str(initsize), " Value of K: " + str(k))
        if k == 0:
        	if initsize <= dirsize:
                	result1.append(line)
                else:
                	k=1
                        initsize=float(ad)
                        result2.append(line)
                        continue
        elif k == 1:
                if initsize <= dirsize:
                        result2.append(line)
                else:
                        k=2
                        initsize=float(ad)
			result3.append(line)
                        continue
        elif k == 2:
                if initsize <= dirsize:
                        result3.append(line)
                else:
                        k=3
                        initsize=float(ad)
                        result4.append(line)
                        continue
        else:
                if initsize <= dirsize:
                        result4.append(line)
print("Array1")
for i in result1      :
	print(i)
print ("Array2")
for j in result2:
        print(j)
print ("Array3")
for k in result3:
        print(k)
print ("Array4")
for l in result4:
        print(l)
