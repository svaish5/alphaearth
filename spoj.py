print ("hello world !!")


i = int(input ())
while (i > 0):	
	
	if (i == 42):
		print (i)
		break
	else:
		print (i)
		i = int(input ())

		
a = int(input())
b = int(input())
print (a+b)


test = int(input())
while (test > 0):
	str = input()
	l = len(str)
	d = ""
	for i in range (0,int(l/2),2):
		d += str[i]
	print (d)
	test -= 1

	
test = int(input())
while (test > 0):
	temp = input().split(" ")
	row = temp[0]
	col = temp[1]
	d = ""
	for x in range (0,int(row)):
		for y in range (0,int(col)):
			if ( (x+y) % 2 == 0):
				d += '*'
			else:
				d += '.'
		print(d)
		d = ""
	print ("\n")
	test -= 1
	

test = int(input())
while (test > 0):
	temp = input().split(" ")
	row = int(temp[0])
	col = int(temp[1])
	d = ""
	for x in range (0,row):
		for y in range (0,col):
			if (x == 0):
				d += '*'
			elif x == row-1:
				d += '*'
			elif y == 0:
				d += '*'
			elif y == col-1:
				d += '*'
			else:
				d += '.'
		print (d)
		d = ""
	print ("\n")
	test -= 1

	
test = int(input())
while (test > 0):
	temp = input().split(" ")
	row = (int(temp[0]) * 3 ) + 1
	col = (int(temp[1]) * 3 ) + 1
	m = 1
	d = ""
	for x in range (0,row):
		for y in range (0,col):
			if (x == 0):
				d += '*'
			elif (x == row):
				d += '*'
			elif ( x % 3 == 0):
				d += '*'
			elif (y == 0):
				d += '*'
			elif (y == col):
				d += '*'
			elif (y == 3*m):
				d += '*'
				m += 1
			else:
				d += '.'
		print (d)
		d = ""
		m = 1
	print ("\n")
	test -= 1
	
	
test = int (input())
while (test > 0):
	temp = input().split(" ")
	line = int(temp[2])
	dot = int(temp[3])
	row = (int(temp[0]) + 1) + int(temp[0]) * line
	col = (int(temp[1]) + 1) + int(temp[1]) * dot
	d = ""
	m = line + 1
	n = dot + 1
	for x in range (0,row):
		for y in range (0,col):
			if (x == 0):
				d += '*'
			elif (x == row-1):
				d += '*'
			elif (y == 0):
				d += '*'
			elif (y == col-1):
				d += '*'
				elif ( x % m == 0 ):
				d += '*'
			elif ( y % n == 0 ):
				d += '*'
			else:
				d += '.'
		print (d)
		d = ""
	print ("\n")
	test -= 1

	
test = int(input())
while (test > 0):
	temp = input().split(" ")
	line = int(temp[2])
	row = int(temp[0]) + 1 + ( int(temp[0]) *  line)
	col = int(temp[1]) + 1 + ( int(temp[1]) *  line)
	d = ""
	m = line + 1
	print (row,col,line)
	back=1
	for x in range (0,row):
		for y in range (0,col):
			if (x == 0):
				d += '*'
			elif (x == row-1):
				d += '*'
			elif (x % m == 0):
				d += '*'
				if (y==col-1):
					if(back):
						back=0
					else:
						back=1
			elif ( y == 0):
				d += '*'
			elif (y == col-1):
				d += '*'
			else:
				if (back==1):
					d += '\\'
					back=0
				else :
					d += '/'
					back=1
		print(d)
		d = ""
	print ("\n")
	test -= 1

	
test = int(input())
while (test > 0):
	temp = input().split(" ")
	row = temp[0]
	col = temp[1]
	d = ""
	for x in range (0,int(row)):
		for y in range (0,int(col)):
			if ( (x+y) % 2 == 0):
				print('*',end="")
			else:
				print('.',end="")
		#print(d)
		d = ""
		print ("\r")
	test -= 1

	
temp = input().split(" ")
x = int(temp[0])
y = int(temp[1])
sum = 0
while (x<=y):
	for i in range (x,y+1):
		sum = sum + i*i
		x += 1
	print (sum)
	
	
def wow(n):
	for i in range (0,n+2):
		 if ( i ==0 ):
			print(W,end="")
		elif ( i==n+1):
			print(w)
		else:
			print(o)

n = int(input())
wow(n)




#SEQUENCES




n = int(input())
S = input().split(" ")
m = int(input())
Q = input().split(" ")
count = 0
for i in range (0,n):
	for j in range (0,m):
		if (S[i] == Q[j]):
			count = 0
			break
		else:
			count += 1
			continue
	if (count != 0):
		print(S[i],end=" ")
	count = 0
	
	
n = int(input())
S = input().split(" ")
m = int(input())
Q = input().split(" ")
for i in range (0,n):
	for j in range (0,m):
		if (S[i] != Q[j]):
			continue
		else:
			print(S[i],end=" ")
			
	
temp = input().split(" ")
n = int(temp[0])
x = int(temp[1])	
S = input().split(" ")
Q = input().split(" ")
for i in range (1,n+1):
	for j in range (max(1,i-x),min(n+1,i+x+1)):
		if (S[i-1] == Q[j-1]):
			print(i,end=" ")
			continue

			
n = int(input())
S = input().split(" ")
m = int(input())
Q = input().split(" ")
k = min(len(S),len(Q))
for i in range (0,k):
	if (S[i] == Q[i]):
		print (i+1,end=" ")

	
n = int (input())
S = input().split(" ")
l = len(S)
count = 0
a = []
for i in range (0,l-1):
	if (int(S[i]) > int(S[i+1])):
		a.append(1)
	else:
		a.append(0)
for j in range (0,l-2):
	if(a[j] >= a[j+1]):
		count = 0
	else:
		count = 1
		break
for k in range (0,l-1):		
	if(int(a[0]) == int(a[l-2])):
		count = 1
		break

if (count == 0):
	print("Yes")
else:
	print("No")
	
	
n = int(input())
S = input().split(" ")
m = int(input())
Q = input().split(" ")
Sum1 = 0
Sum2 = 0
for i in range(0,n):
	Sum1 = Sum1 + int(S[i])
for j in range (0,m):
	Sum2 = Sum2 + int(Q[j])
if (Sum2 < Sum1):
	for i in range(0,n):
		print (S[i],end=" ")
else:
	for j in range (0,m):
		print (Q[j],end=" ")	
	
	
n = int(input())
S = input().split(" ")
m = int(input())
Q = input().split(" ")
Sum1 = 0
Sum2 = 0
for i in range(0,n):
	Sum1 = Sum1 + int(S[i])
Sum1 = Sum1/n	
for j in range (0,m):
	Sum2 = Sum2 + int(Q[j])
Sum2 = Sum2/m
if (Sum2 < Sum1):
	for i in range(0,n):
		print (S[i],end=" ")
else:
	for j in range (0,m):
		print (Q[j],end=" ")
	
	
	
	
#XOR
	
	

	
A = input().split(" ")
if (A[0] == A[1]):
	print(0)
else:
	print(1)














	
	