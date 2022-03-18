def py(n):
	k = 2*n - 2
	for i in range(0,n):
		for j in range(0,k):
			print(end=" ")
		k = k - 2
		if j != i:
			print (i+1, end=" ")
		for j in range (0,i):
			print ("0 ", end="")
		print("\r")
n=5
py(n)
