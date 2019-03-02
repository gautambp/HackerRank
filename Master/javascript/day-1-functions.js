// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-1-functions/problem

/*
 * Create the function factorial here
 */
function factorial(n) {
    var f = 1;
    for (var i = 1; i <= n; i++)
        f *= i;
    return f;
}

