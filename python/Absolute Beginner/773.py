''' You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2

Sample Output :
2 '''


num = int(input(""))
fact=1
if (num > 0):
    for i in range(1,num+1):
     fact=fact*i
print(fact)

