import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
       int answer = 0;
        int nowTime = 0;
        int finish = 0; // 완료한 작업 수
        int total_time = 0;
        int beforeRequest = -1;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]); // 소요시간 기준으로 정렬

        while (finish < jobs.length) {
            // 현재 시간 기준 작업할 수 있는 작업 가져오기
            for (int[] job : jobs) {
                if (beforeRequest < job[0] && job[0] <= nowTime) {
                    heap.offer(new int[]{job[1], job[0]}); // 소요시간, 요청시간 순으로 추가
                }
            }

            // 작업 수행
            if (!heap.isEmpty()) {
                int[] nowWorking = heap.poll(); // 소요시간이 가장 작은 작업 꺼내기
                beforeRequest = nowTime;
                nowTime += nowWorking[0]; // 작업 끝난 시점으로 이동
                total_time += (nowTime - nowWorking[1]); // 작업 대기 및 완료 시간
                finish++;
            } else { // 수행할 작업이 없으면
                nowTime++;
            }
        }

        answer = total_time / jobs.length;
        return answer;
    }
}