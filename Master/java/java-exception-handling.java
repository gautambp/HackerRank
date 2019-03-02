// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-exception-handling/problem

class MyCalculator {
    /*
    * Create the method long power(int, int) here.
    */
    public long power(int n, int p) throws Exception {
        if (n == 0 && p == 0) throw new Exception("n and p should not be zero.");
        if (n < 0 || p < 0) throw new Exception("n or p should not be negative.");
        int r = 1;
        for (int i=1; i<=p; i++) r *= n;
        return r;
    }
    
}

