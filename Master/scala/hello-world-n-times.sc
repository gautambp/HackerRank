// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/hello-world-n-times/problem
def f(n: Int) : Unit = { 
    if (n >= 1) {
        println("Hello World"); 
        f(n-1);
    }
}