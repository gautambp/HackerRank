// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-4-create-a-rectangle-object/problem


/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    var r = new Object();
    r.length = a;
    r.width = b;
    r.area = a * b;
    r.perimeter = 2 * (a + b);
    return r;
}

