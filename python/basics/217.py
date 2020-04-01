''' Given numbers A,B find A^B.
Input Size : 1 <= A <= 5 <= B <= 50
Sample Testcase :
INPUT
3 4
OUTPUT
81 '''


import math
A,B=map(int,input().split())
result=math.pow(A,B)
print(round(result))
