// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-static-initializer-block/problem


public static int B = 0;
public static int H = 0;
public static boolean flag = true;

static {
    try {
        Scanner s = new Scanner(System.in);
        B = s.nextInt();
        H = s.nextInt();
        if (B <= 0 || H <= 0) {
            flag = false;
            throw new Exception("Breadth and height must be positive");
        }
    } catch (Exception e) {
        System.out.println(e);
    }
}

