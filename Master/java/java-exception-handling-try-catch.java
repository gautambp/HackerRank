// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-exception-handling-try-catch/problem
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        String s1 = s.nextLine();
        String s2 = s.nextLine();
        try {
            int n1 = Integer.parseInt(s1);
            int n2 = Integer.parseInt(s2);
            int r = (int) (n1 / n2);
            System.out.println(r);
        } catch (NumberFormatException nfe) {
            System.out.println("java.util.InputMismatchException");
        } catch (ArithmeticException e) {
            System.out.println(e);
        }
    }
}

