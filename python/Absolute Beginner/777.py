'''You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8

Sample Output :
31 '''




num=int(input(""))
if((num==1) or (num==3) or (num==5) or (num==12) or (num==10) or (num==8) or (num==7)):
    print("31")
elif(num==2):
    print("28")
elif((num==4) or (num==6) or (num==9) or (num==11)):
    print("30")
else:
    print("Error")

