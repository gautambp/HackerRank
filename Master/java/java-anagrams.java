// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-anagrams/problem


    static boolean isAnagram(String a, String b) {
        // Complete the function
        if (a.length() != b.length()) return false;
        a = a.toLowerCase();
        b = b.toLowerCase();
        for (int i=0; i<a.length(); i++) {
            b = b.replaceFirst(String.valueOf(a.charAt(i)), " ");
            //System.out.println(b);
        }
        if (b.trim().isEmpty()) return true;
        return false;
    }

