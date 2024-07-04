import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();
        int time = 0;
        int count = 0;
        
        while (progresses.length > 0) {
            if (progresses[0] + time * speeds[0] >= 100) {
                progresses = Arrays.copyOfRange(progresses, 1, progresses.length);
                speeds = Arrays.copyOfRange(speeds, 1, speeds.length);
                count++;
            } else {
                if (count > 0) {
                    answerList.add(count);
                    count = 0;
                }
                time++;
            }
        }
        answerList.add(count);
        
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
}
}