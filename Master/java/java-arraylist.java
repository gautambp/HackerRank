// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-arraylist/problem
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine().trim());
        ArrayList<ArrayList> l = new ArrayList<ArrayList>();
        for (int i=0; i<n; i++) {
            ArrayList rl = new ArrayList<Integer>();
            l.add(i, rl);
            String[] t = s.nextLine().trim().split(" ");
            for (int j=0; j<t.length; j++) {
                rl.add(j, Integer.parseInt(t[j]));
            }
        }
        int q = Integer.parseInt(s.nextLine().trim());
        for (int j=0; j<q; j++) {
            String[] t = s.nextLine().trim().split(" ");
            int r = Integer.parseInt(t[0])-1;
            int c = Integer.parseInt(t[1]);
            if (r >= l.size() || c >= l.get(r).size())
                System.out.println("ERROR!");
            else
                System.out.println(l.get(r).get(c));
        }
    }
}

