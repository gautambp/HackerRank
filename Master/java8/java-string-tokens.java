// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-string-tokens/problem
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        String clean_s = s.trim();
        if (clean_s.length() > 0) {
            String[] tokens = clean_s.split("[ !,?._'@]+");
            System.out.println(tokens.length);
            for (int i=0; i<tokens.length; i++) System.out.println(tokens[i]);
        } else {
            System.out.println("0");
        }
       scan.close();
    }
}

