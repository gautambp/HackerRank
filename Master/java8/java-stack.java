// @author: Gautam Patel
// Problem Description URL: https://www.hackerrank.com/challenges/java-stack/problem
import java.util.*;
class Solution{
	
    private static boolean isBalanced(String s, int idx, Stack<Character> p) {
        if (idx >= s.length()) {
            return p.isEmpty();
        }
        char c = s.charAt(idx);
        if (c == '{' || c == '(' || c == '[') {
            p.push(c);
        } else if (c == '}' || c == ')' || c == ']') {
            if (p.isEmpty()) return false;
            char item = p.pop();
            if (c == '}' && item != '{') return false;
            if (c == ')' && item != '(') return false;
            if (c == ']' && item != '[') return false;
        }
        idx++;
        return isBalanced(s, idx, p);
    }
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input=sc.next();
            //Complete the code
            System.out.println(isBalanced(input, 0, new Stack<Character>()));
		}
		
	}
}



