// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-3-arrays/problem


/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var l1 = 0;
    var l2 = 0;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] > l1) {
            l2 = l1;
            l1 = nums[i];
        } else if (nums[i] > l2 && nums[i] < l1)
            l2 = nums[i];
    }
    return l2;
}

