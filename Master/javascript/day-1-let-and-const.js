// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-1-let-and-const/problem


const PI = Math.PI;

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    let rs = readLine();
    let r = parseFloat(rs);
    
    // Print the area of the circle:
    console.log(PI * r * r);
    
    // Print the perimeter of the circle:
    console.log(2 * PI * r);

