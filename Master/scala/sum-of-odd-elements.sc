// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/sum-of-odd-elements/problem
def f(arr:List[Int]):Int = {
    var arr_sum:Int = 0;
    for(i <- 0 until arr.length) {
        if (math.abs(arr(i)%2) == 1) {
            arr_sum = arr_sum + arr(i);
        }
    }
    return arr_sum;
}