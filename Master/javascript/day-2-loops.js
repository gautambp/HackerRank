// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-2-loops/problem


/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    for (var i = 0; i < s.length; i++) {
        var ch = s.charAt(i);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            console.log(ch); 
    }
    for (var i = 0; i < s.length; i++) {
        var ch = s.charAt(i);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            continue;
        console.log(ch);
    }
}

