//  최소한의 객실 사용
//  한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소하고 다음 손님 가능
//  코니에게 필요한 최소 객실의 수

//  도착 + 10분
//  출발 시간 기준 append
import java.io.*;
import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int[][] time = new int[book_time.length][2];
        
        Arrays.sort(book_time, (o1, o2) -> {
            return Integer.parseInt(o1[0].substring(0,2)+o1[0].substring(3)) - Integer.parseInt(o2[0].substring(0,2)+o2[0].substring(3));
        });
        
        for (int i=0;i<time.length;i++) {
            time[i][0] = Integer.parseInt(book_time[i][0].substring(0,2))*60 + Integer.parseInt(book_time[i][0].substring(3));
            time[i][1] = Integer.parseInt(book_time[i][1].substring(0,2))*60 + Integer.parseInt(book_time[i][1].substring(3))+10;
            System.out.println(time[i][0] + " " + time[i][1]);
        }
        pq.offer(time[0][1]);
        for (int i=1;i<time.length;i++) {
            if(pq.peek() <= time[i][0]) {
                pq.poll();
            } 
            pq.offer(time[i][1]);
            answer = Math.max(pq.size(),answer);
            // System.out.println(pq.size());
        }
        
        return answer;
    }
}