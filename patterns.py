n = int (input())
def fun1(n):
	num = 1
	for i in range (1,n+1):
		for j in  range (1,i+1):
			print ( num , end="")
			num += 1
		num = 1
		print ("\r")
		
fun1(n)

n = int	(input())
def fun2(n):
	num = 1
	k = 2*n - 2
	for i in range (1,n+1):
		for j in range (0,k):
			print (end=" ")
		k -= 2
		for j in range (1,i+1):
			print ("*" , end=" ")
			num += 1
		print ("\r")
		num = 1
fun2(n)


n = int (input())
def fun2a(n):
	for i in range (0,n):
		m = 1
		for j in range (0,n-i-1):
			print (end=" ")
		for j in range (0,i+1):
			print (m,end="")
			m += 1
		print ("\r")	
fun2a(n)



n = int (input())
def fun2b(n):
	for i in range (0,n):
		m = i+1
		for j in range (0,n-i-1):
			print (end=" ")
		for j in range (0,i+1):
			print ("*",end="")
			m -= 1
		print ("\r")	
fun2b(n)

	
test = int(input())
while ( test > 0):
	temp = input().split(" ")
	r = int(temp[0])
	c = int(temp[1])
	row = int(temp[2])
	col = int(temp[3])
	for i in range (0,r):
		for j in range (0,c):
			if (i == row-1):
				print('*',end="")
			elif (j == col-1):
				print ('*',end="")
			else:
				print('.',end="")
		print("\r")
	test -= 1	
	
	
test = int(input())
while (test >0):
	temp = input().split(" ")
	r = int(temp[0])
	c = int(temp[1])
	ro = int(temp[2])
	row = ro - 1
	co = int(temp[3])
	col = co - 1
	#print (row)
	m = 0
	n = c - 1
	k = 0
	l = col+2
	T = []
	for i in range(0,r):
		T.append([])
		for j in range(0,c):
			#if ((i == row) and (j == col)):
				#T[i].append("*")#print("*",end="")
			#elif ((i != row) and (j != col)):
			if (row != col):
				if (( i == k) and (j == l)):
					T[i].append("*")#print("*",end="")
					k += 1
					l -= 1
				elif ( j-i == 2 ):
					T[i].append("*")#print("*",end="")
				else:
					T[i].append(".")#print (".",end = "")
			elif (row == col):
				if ((i == m) and (j == n)):
					T[i].append("*")#print("*",end="")
					m += 1
					n -= 1
				elif ( i-j == 0 ):
					T[i].append("*")#print("*",end="")
				else:
					T[i].append(".")#print (".",end = "")
			else:
				T[i].append(".")#print (".",end = "")
			print(T[i][j],end="")
		print("\r")
	#print(r,c,ro,row,co,col,i,j,k,l)
	test -= 1
#THE END