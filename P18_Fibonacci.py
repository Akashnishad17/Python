
def fibonacci(n,a,b):
	if n==0:
		return;
	else:
		print(b)
		s = a + b
		a = b
		b = s
		fibonacci(n-1,a,b)


num = int(input("Enter the range: "))

fibonacci(num,0,1)