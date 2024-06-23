import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] visited = new int[N + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(N);
        
        while (!queue.isEmpty()) {
            int num = queue.poll();
            
            if (num == 1) {
                System.out.println(visited[num]);
                break;
            }
            
            if (num % 3 == 0) {
                int nextNum = num / 3;
                if (nextNum >= 0 && nextNum <= N && visited[nextNum] == 0) {
                    visited[nextNum] = visited[num] + 1;
                    queue.offer(nextNum);
                }
            }
            
            if (num % 2 == 0) {
                int nextNum = num / 2;
                if (nextNum >= 0 && nextNum <= N && visited[nextNum] == 0) {
                    visited[nextNum] = visited[num] + 1;
                    queue.offer(nextNum);
                }
            }
            
            int nextNum = num - 1;
            if (nextNum >= 0 && nextNum <= N && visited[nextNum] == 0) {
                visited[nextNum] = visited[num] + 1;
                queue.offer(nextNum);
            }
        }
        
    }
}