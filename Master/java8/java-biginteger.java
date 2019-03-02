// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-biginteger/problem
import java.util.*;
import java.math.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String aStr = scanner.nextLine();
        String bStr = scanner.nextLine();
        BigInteger a = new BigInteger(aStr);
        BigInteger b = new BigInteger(bStr);
        System.out.println(a.add(b));
        System.out.println(a.multiply(b));
        scanner.close();
    }
};
