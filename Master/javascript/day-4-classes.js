// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-4-classes/problem
/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */

class Polygon {
    constructor(arr) {
        this.p = 0;
        for (var i = 0; i < arr.length; i++)
            this.p += arr[i];
    }
    perimeter() {
        return this.p;
    }
}

