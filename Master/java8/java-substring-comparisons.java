// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-substring-comparisons/problem


    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        java.util.TreeSet<String> ts = new java.util.TreeSet<String>();
        for (int i=0; i<=s.length()-k; i++) {
            ts.add(s.substring(i, i+k));
        }
        
        return ts.first() + "\n" + ts.last();
    }

