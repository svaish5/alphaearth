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
