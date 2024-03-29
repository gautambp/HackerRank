// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-5-inheritance/problem


/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */
Rectangle.prototype.area = function () {
    return this.w * this.h;
}

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle {
    constructor(s) {
        super(s, s);
    }
}

