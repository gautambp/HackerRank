// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/day-4-count-objects/problem


/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    var cnt = 0;
    for (var i = 0; i < objects.length; i++) {
        if (objects[i].x == objects[i].y) cnt += 1;
    }
    return cnt;
}

