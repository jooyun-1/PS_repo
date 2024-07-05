import java.util.*;

public class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        Deque<Integer> q = new LinkedList<>();
        
        // 우선순위 큐를 채웁니다.
        for (int priority : priorities) {
            q.add(priority);
        }
        
        int idx = location;
        while (q.size() > 1) {
            int tmp = q.poll();
            if (tmp < Collections.max(q)) {
                q.add(tmp);
                if (idx == 0) {
                    idx = q.size() - 1;
                } else {
                    idx--;
                }
            } else {
                if (idx == 0) {
                    return answer;
                } else {
                    answer++;
                    idx--;
                }
            }
        }
        
        return answer;
    }
}
