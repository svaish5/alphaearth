from array import *

#T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

#for i in range (0,len(T)):
#	for j in range (0,len(T[i])):
#		print (T[i][j],end=" ")
#	print () 
	
#n = int(input())
#k= 'a'
#T = []
#for i in range (0,n):
#	T.append([])
#	for j in range (0,n):
#		if (ord(k)<=122):
#			T[i].append(k)
#			k=chr(ord(k)+1)
#		else:
#			k = 'a'
#			T[i].append(k)
#			k=chr(ord(k)+1)
#		print(T[i][j],end=" ")
#	print ("\r")
				
#n = int(input())
#k= 'a'
#T = []
#for i in range (0,n):
#	T.append([])
#	for j in range (0,n):
#		if (ord(k)<=122):
#		
#			T[i].append(k)
#		else:
#			k = 'a'
#			T[i].append(k)
#			k=chr(ord(k)+1)
#	
#for i in range (0,n):
#	T.append([])
#	if ( i % 2 == 0):
#		for j in range (0,n):
#			print(T[i][j],end=" ")
#	else:
#		for j in range (n-1,-1,-1):
#			print(T[i][j],end=" ")
#	print ("\r")

n = int(input())
T = []
for i in range (0,n):
	T.append([])
	for j in range (0,i+1):
		if ( j == 0):
			T[i].append(1)
		elif ( j == i):
			T[i].append(1)
		else:
			T[i].append(T[i-1][j-1]+T[i-1][j])
		#print(T[i][j],end=" ")
	#print ("\r")
for i  in range (0,n):
	T.append([])
	for j in range (0,i+1):
		print(T[i][j],end=" ")
	print ("\r")
	
#Proper pascal /_\
#n=int(input("Enter number of rows: "))
#a=[]
#for i in range(n):
#    a.append([])
#    a[i].append(1)
#    for j in range(1,i):
#        a[i].append(a[i-1][j-1]+a[i-1][j])
#    if(n!=0):
#        a[i].append(1)
#for i in range(n):
#    print("   "*(n-i),end=" ",sep=" ")
#    for j in range(0,i+1):
#        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
#    print()	


def hcf(a,b):
	if (a > b):
		max = a
		min = b
	else:
		max = b
		min = a
	if(min==0):
		return max
	else: 
		return hcf(min,max%min)
i = input().split(" ")
a = int(i[0])
b = int(i[1])
HCF = hcf(a,b)
print(HCF)
	
