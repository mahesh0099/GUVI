'''Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes'''


a, b, c = map(int, input().split())
def triangle(x, y, z):
        if (x + y > z) and (y + z > x) and (x + z > y):
            print("yes")
        else:
            print("no")

triangle(a, b, c)
