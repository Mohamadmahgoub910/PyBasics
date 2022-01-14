# itertools.product() in Python - Hacker Rank Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.product() in Python - Hacker Rank Solution START
from itertools import product
A = input().split()
A = list(map(int, A))
B = input().split()
B = list(map(int, B))
output = list(product(A, B))
for i in output:
    print(i, end=" ")
# itertools.product() in Python - Hacker Rank Solution END
