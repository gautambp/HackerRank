// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-loops-ii/problem
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for (int j=0; j<n; j++) {
                int val = a;
                for (int k=0; k<=j; k++) {
                    val += (int)(b * Math.pow(2.0, k));
                }
                System.out.print(val);
                System.out.print(" ");
            }
            System.out.println("");
        }
        in.close();
    }
}

