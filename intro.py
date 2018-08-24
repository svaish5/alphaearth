print ("hello world !!")

if 5 > 2:
  print("Five is greater than two!")
#indentation error ; no recess
"""if 4 < 7
print("Four is less than 7!")"""		

print("example of indentation,comment and multiple docstring")

#variables

a = "python"
a = "python is "
b = "number 0"
c = "1"
d = 1
e = 9
print("variables")
print (a+b)
print (a+b+c)
print ( "parantheses is must; space for presentation")
print ("error when combine int and string")
#print (a+b+c+d)
print (d+e)
#print d+e
#print a+b
x = a+b+c
print (x)
print ("start-with & contain a-z A-Z 0-9 _ and are case sensitive")


#Numbers

a = -87
b = -22.600
c = -87.7e98
d = -5j
print (type(a))
print (type(b))
print (type(c))
print (type(d))

#Casting

a = int(2.8)
b = float(4)
c = str(2)
print (a)
print (b)
print (c)

#Strings

a = ' Hello, World !! '
print (a[1])
print (a[4:11])
print (a)
print (a.strip())
print (len(a))
print (a.lower())
print (a.upper())
print (a.replace ("World","People"))
print (a.split(","))

print ("enter name")
x = input()
print ("hello," +x)

#Lists

mylist = ["job","salary","anny"]
print (mylist)
mylist[1] = "my bday"
print (mylist)
 
 
 
 
#list constructor

mylist = list (("job","my bday","anny","salary"))
mylist.append("trip")
print (mylist)

mylist.remove("my bday")
print (mylist)
print(len(mylist))
print (mylist)

mylist.insert(1,"mybday")
print (mylist)

mylist.pop(1)
print (mylist)


x = mylist.index("anny")
print (x)

mylist.reverse()
print (mylist)

mylist.sort()
print (mylist)

y = mylist.count("salary")
print (y)

y = mylist.copy()
print (y)

mylist.extend("my bday")
print (mylist)

mylist.clear()
print (mylist)

#SPACES

a =45
print (a)
print ( a)
print ("a")
print (" a")
b = 36
print ( a, b)
print ( a, b,sep="")
print ( a, b,sep=" ")
print (str(a) + '' + str(b))




		#Shallow & Deep Copy


#print("regular reference")
#l1 = [1,2,3,4]
#l2 = l1
#print (l1,l2)
#l1.append(10)
#print (l1,l2)
#l2.append(11)
#print (l1,l2)
print("shallow copy,do affect nested object")
print('\r')
l1 = [[1,2],[3,4]]
import copy
l3 = copy.copy(l1)
print(l1,l3)
print('\r')
l3.append('A')
print(l1,l3)
print('\r')
l3[0][1]= 'A'
print(l1,l3)
print('\r')
l1[0][0]= 'Z'
print(l1,l3)
print('\r')	
#memoryview
id(l1)
#id(l2)
id(l3)
print("Deep copy, won't affect nested object")
print('\r')
l1 = [[1,2],[3,4]]
l4 = copy.deepcopy(l1)
print(l1,l4)
print('\r')
l4.append('B')
print(l1,l4)
print('\r')
l4[0][1]= 'B'
print(l1,l4)
print('\r')




			#File Handling

fh = open("demofle.txt","r") 
text = fh.read()
count =  sum(1 for character in text if character.isupper())
print(count)

#fh = open("demofle.txt","at")
#fh.write(" hi harsh !! how u doing ? This year Harsh enjoyed a lott,Harsh is doing great")
#fh = open("demofle.txt","rt")
#print(fh.read())
fh = open("demofle.txt","wt")
fh.write(" hi harsh !! how u doing ? This year Harsh enjoyed a lott,Harsh is doing great")
fh = open("demofle.txt","rt")
print(fh.read())

fh = open("demofle.txt","wt")
fh.write(" hi Harsh !! how u doing ? This year Harsh enjoyed a lott,Harsh is doing great")
fh = open("demofle.txt","rt")
print(fh.read())
with open ('demofle.txt','rt') as fh:
	f = fh.read().replace('Harsh','Harsha')
with open ('demofle.txt','wt') as fh:
	fh.write(f)
fh = open("demofle.txt","rt")
print(fh.read())






		# List files & folders in sub-dirs
		
import os
#list = os.listdir("C:\\dir")
#print(list)

def dirlist(path):
	for subdir in os.listdir(path):
		subdir = os.path.join(path,subdir)
		#if os.path.isdir(subdir):
		if os.path.isfile(subdir):
			print(subdir)
			#dirlist(subdir)
		else:
			print (subdir)
			dirlist(subdir)
list2 = dirlist("C:\\dir")
list3 = os.walk("C:\\dir")
print (list3)



		# DECORATOR
		
def my_decorator(item):
	def inner():
		print("before decorator")
		item()
		print("after decorator")
	return inner
	
@my_decorator	
def ordinary():
	print("Hello, i'm ordinary, to be decorated soon :)")

ordinary()
#pretty = my_decorator(ordinary)
#pretty()
		

		
		
		#TREE
		
class Node:
	def __init__(self,data):
		self.children = []
		self.data = data
	#def append(self,*args,**kwargs):
	#	self.children.append(*args,**kwargs)
	def PrintTree (self):
		print(self.data)
		for child in self.children:
			child.PrintTree()
root = Node(10)
child1 = Node(20)
#root.append(child1)
root.PrintTree()


class Node:
	def __init__(self,data):
		self.children = []
		self.data = data
	def __repr__(self):
		return "<Node '{}'>".format(self.data)
	def append(self,*args,**kwargs):
		self.children.append(*args,**kwargs)
		print(self.children)
	def PrintTree (self):
		print(self.data)
		print(self.children)
		for child in self.children:
			print(self.children)		
			child.PrintTree()
	def PrintTree2 (self):
		def gen(o):
			l = [o,]
			print(self.children)
			while l:
				print(self.children)
				oNext = l.pop(0)
				l.extend(oNext.children)
				yield oNext
		for oNode in gen(self):
			print(oNode)

root = Node(10)
child1 = Node(20)
child2 = Node(30)
child3 = Node(40)
child4 = Node(50)
root.append(child1)
child1.append(child2)
root.append(child3)
child1.append(child4)
root.PrintTree()
root.PrintTree2()	

class Node(object):
	def __init__(self,data):
		self.data = data
		self.child = []
	def append(self,*args,**kwargs):
		self.child.append(*args,**kwargs)
	def depth_first(self):
		print(self.data)
		for node in self.child:
			node.depth_first()
	def width_first(self):
		def gen(obj):
			l = [obj]
			while l:
				nextobj = l.pop(0)
				l.extend(nextobj.child)
				yield nextobj
		for node in gen(self):
			print(node.data)
		
Root = Node(100)
child1 = Node(10)
child2 = Node(20)
child3 = Node(30)
child4 = Node(40)
child5 = Node(50)
child6 = Node(60)
Root.append(child1)
child1.append(child2)
child1.append(child4)
child4.append(child6)
Root.append(child3)
child3.append(child5)
Root.depth_first()
Root.width_first()

			# GENERATOR & YIELD
			
class my:
	def _init_(self,data):
		self.data = data
		
	def sum(self):
		#print(self.data)
		summ = self.data
		yield summ
ob = my(20)
temp = ob.sum()
print(temp)

			
def fibonacci():
	curr = 1
	prev = 0
	num = 5
	while (num > 0 ):
		# Generator function contains yield statements
		yield prev
		prev,curr = curr, curr+prev
		num -= 1
for item in fibonacci():	
	print(item)
	
	
	
	# INHERITANCE
	
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()



# DICTIONARY
1
2
s 1
r 2
s 3
r 4
w 1

d 1
d 2
v 3
d 4
d 5 

test = int(input())
while (test > 0):
	num = int(input())
	arr = dict()
	for i in range (0,num):
		
		temp = input().split(" ")
		name = temp[0]
		tweet = temp[1]
		
		if name in arr.keys():
			arr[name] += 1
		else:
			arr[name] = 1
	

	max = -1
	for key in arr.keys():
		if max < arr[key]:
			max = arr[key]
			
	
	for key in arr.keys():
		if max == arr[key]:
			arr_name = key
			print(arr_name,max)
			
	
	test -= 1



# SORTING

scnd largest num

a = []
a = input().split(" ")
print(a)
l = len(a)
print (l)
a.sort()
print (a)
print (a[-2])	  

#Bubble sort

a = []
a = input().split(" ")
print(a)
l = len(a)
for i in range(0,l):
	for j in range(0,l-1-i):
		if a[j]>a[j+1]:
			a[j],a[j+1] =a[j+1],a[j]
		else:
			a[j],a[j+1] = a[j],a[j+1]
print(a)
print(a[-2])		

# WITHOUT SOTING

scnd largest num

a = []
a = input().split(" ")
print(a)
l = len(a)
max = -1
for i in range(0,l):
	if max < int(a[i]):
		if int(a[i]) > max:
			scnd_max = max
			max = int(a[i])
	else:
		if int(a[i]) > scnd_max:
			scnd_max = int(a[i])
print(scnd_max)
		
# CHECK CIRCULAR LINK LIST

class node:
	def __init__(self, dataval = None):
		self.dataval = dataval
		self.nextval = None
	
e1 = node('Mon')
e2 = node('Wed')
e3 = node('Tue')

e1.nextval = e3
e3.nextval = e2
#e2.nextval = e1

var = e1
while var:
	data = var.dataval
	print(data)
	var = var.nextval
	if var == e1:
		print('Circular Linked List')
		break

		# QUEUE

class Queue:
	def __init__(self):
		self.queue = []

	def addtoq(self,dataval):
# Insert method to add element
		if dataval not in self.queue:
			self.queue.append(dataval)
			return True
		return False
	def prnt(self):
		return self.queue
	
obj = Queue()
obj.addtoq("Mon")
obj.addtoq("Tue")
obj.addtoq("Wed")
print(obj.prnt())