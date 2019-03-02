// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-3-try-catch-and-finally/problem


/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try {
        let r = s.split('').reverse().join('');
        console.log(r)
    } catch (e) {
        console.log(e.message);
        console.log(s);
    }
}

