// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-5-arrow-functions/problem


/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    return nums.map(function (n) { 
        if (n % 2 == 0) return n * 2;
        return n * 3;
    })
}

