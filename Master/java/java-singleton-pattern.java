// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-singleton-pattern/problem
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;


class Singleton{
    private static Singleton s = null;
    public String str;
    
    private Singleton() {
    }
    public static Singleton getSingleInstance() {
        if (s == null) s = new Singleton();
        return s;
    }
}