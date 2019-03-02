// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-string-reverse/problem
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        boolean is_palindrome = true;
        int a_len = A.length();
        for (int i=0; i<(int)a_len/2; i++) {
            if (A.charAt(i) != A.charAt(a_len-i-1)) {
                is_palindrome = false;
                break;
            }
        }
        if (is_palindrome) System.out.println("Yes");
        else System.out.println("No");
        
    }
}



