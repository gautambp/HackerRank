// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-7-regular-expressions-i/problem


function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    var re = /^([aeiou]).*\1$/;
    
    /*
     * Do not remove the return statement
     */
    return re;
}
