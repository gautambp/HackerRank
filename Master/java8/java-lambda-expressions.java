// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-lambda-expressions/problem


    public PerformOperation isOdd() {
        PerformOperation op = (int x)-> (x%2 != 0);
        return op; 
    }
    private static boolean checkPrime(int x) {
        for (int i=2; i<x; i++) {
            if (x%i == 0) return false;
        }
        return true;
    }
    private static boolean checkPalindrome(int x) {
        String xStr = String.valueOf(x);
        int len = xStr.length();
        for (int i=0; i<(int)len/2; i++)
            if (xStr.charAt(i) != xStr.charAt(len-i-1)) return false;
        return true;
    }
    public PerformOperation isPrime() {
        PerformOperation op = (int x)-> MyMath.checkPrime(x);
        return op; 
    }
    public PerformOperation isPalindrome() {
        PerformOperation op = (int x)-> MyMath.checkPalindrome(x);
        return op; 
    }
   // Write your code here
}

