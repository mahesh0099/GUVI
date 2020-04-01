'''Given a string S consisting of 2 words reverse the order of two words .
Input Size : |S| <= 10000000
Sample Testcase :
INPUT
hello world
OUTPUT
world hello'''




import java.util.Scanner;
public class Main {
  public static void stringReverse(String s)
  {
    String str[]=s.split(" ");
    String ans="";
    for(int i=str.length-1; i>=0;i--)
    {
      ans+=str[i]+" ";
    }
    System.out.println(ans);
  }
  
    public static void main(String[] args) {
      Scanner scanner= new Scanner(System.in);
      String input = scanner.nextLine();
      Main.stringReverse(input);
    }
}
