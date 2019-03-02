// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-3-throw/problem


/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    if (a > 0) return "YES";
    if (a < 0) throw Error("Negative Error");
    throw Error("Zero Error");
}

