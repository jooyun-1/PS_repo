import java.util.*;

class Solution {
    Stack<Character> stack = new Stack<>();  
    
    boolean solution(String s) {
        boolean answer = true;
        for (int i=0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stack.push(s.charAt(i));
            } else {
                if (stack.size() > 0) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        if (stack.size() > 0) {
            return false;
        }
        return answer;
    }
}