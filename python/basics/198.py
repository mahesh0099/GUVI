'''Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes '''


import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
      Scanner s =new Scanner(System.in);
      int side1=s.nextInt();
      int side2=s.nextInt();
      int side3=s.nextInt();
    if(side1==side2 && side2==side3) 
    {
        System.out.println("no");
    }
    else if(side1==side2 || side1==side3 || side2==side3) 
    {
        System.out.println("no");
    }
    else 
    {
        System.out.println("yes");
    }
    }
}
