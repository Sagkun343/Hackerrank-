x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
z = int(input("Enter a number:"))
n = int(input("enter:"))
print([[i,j,k] for i in range (x+1) for j in range (y+1)for k in range (z+1) if (i+j+k) != n])

