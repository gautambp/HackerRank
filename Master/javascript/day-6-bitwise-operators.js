// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-6-bitwise-operators/problem


function getMaxLessThanK(n, k) {
    var maxVal = 0;
    for (var i = 1; i <= n; i++) {
        for (var j = i+1; j <= n; j++) {
            let r = j & i;
            if (r < k && r > maxVal) maxVal = r;
        }
    }
    return maxVal;
}

