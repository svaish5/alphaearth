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




#from __future__ import print_function
def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True
test = int(input())
while(test>0):
	temp = input().split(" ")
	a = (temp[0])
	b = (temp[1])
	if(is_int(a) and is_int(b)):
		print(int(a)+int(b))
	else:
		print( float(a)+float(b))

	test-=1
	
	
	
#from __future__ import print_function
import math

def SumOfOddFactors(n):
	sum = 1
	if (n % 2 == 0):
		return 0
	else:
		for factor in range (3,n+1):
			while(n % factor == 0):
				n = n/factor
				sum += factor
		if (n > 2):
			return 0
		else:
			return sum
n = int(input())
S = SumOfOddFactors(n)
print (S)

		
