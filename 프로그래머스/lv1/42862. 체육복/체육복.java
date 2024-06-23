/*
학생들의 번호는 체격 순
바로 앞번호나 뒷번호만 빌려줄 수 있음
최대한 많은 학생이 들어야 함
전체 학생 수 : n, 도난당한 학생들의 번호 배열 : lost, 여벌의 체육복 가져온 번호 : reserve
*/
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int cnt = 0;
        answer = n -lost.length;
        Arrays.sort(lost);
        Arrays.sort(reserve);
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (reserve[j]  == lost[i]) {
                    answer += 1;
                    reserve[j] = -1;
                    lost[i] = -1;
                    break;
                }
            }
        }
        
        
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (reserve[j] -1 == lost[i]) {
                    answer += 1;
                    reserve[j] = -1;
                    break;
                } else if (reserve[j] + 1 == lost[i]) {
                    answer += 1;
                    reserve[j] = -1;
                    break;
                }
            }
        }
        return answer;
    }
}