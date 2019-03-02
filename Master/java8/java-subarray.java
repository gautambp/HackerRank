// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-subarray/problem

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        String s = scanner.nextLine();
        String[] numStr = s.split(" ");
        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = new Integer(numStr[i]).intValue();
        }
        scanner.close();

        int neg_sum_count = 0;
        for (int len=1; len<=n; len++) {
            for (int sub=0; sub<n-len+1; sub++) {
                int sum = 0;
                for (int i=sub; i<sub+len; i++) {
                    sum += arr[i];
                }
                if (sum < 0) neg_sum_count++;
            }
        }
        System.out.println(neg_sum_count);
    }
}

