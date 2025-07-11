r1=int(input("enter the first row :"))
c1=int(input("enter the first column:"))
r2=int(input("enter the second row :"))
c2=int(input("enter the second column:"))
if c1!=r2:
	print("matric multiplication not possible")
else:
	print("matrix a")
	A=[]
	for i in range(r1):
		row=list(map(int,input().split()))
		A.append(row)
			
	print("matrix B")
	B=[]
	for i in range(r2):
		row=list(map(int,input().split()))
		B.append(row)
		
	result=[]
	print("result matrix")
	for i in range (r1):
		row=[]
		for j in range(c2):
			s=0
			for k in range(c1):
				s=s+A[i][k]*B[k][j]
			row.append(s)
		result.append(row)
	for row in result :
		print(*row)

