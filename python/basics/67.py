'''Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat '''

import java.util.Scanner;
public class Main {
 public static void main(String[] args) {
    	      Scanner scanner=new Scanner(System.in);
    	      String s=scanner.nextLine();
    	      char c[] = null;
    	      char c1[]=new char[s.length()];
    	      char temp;
    	      for(int i=0; i<s.length()-1;i=i+2)
    	      {  
    	       c=s.toCharArray();
    	       temp=c[i];
    	       c1[i]=c[i+1];
    	       c1[i+1]=temp;
    	      }
   
    	      System.out.print(c1);
    	    }
}
