import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[0] == o2[0]) return o1[1]-o2[1];
				return o1[0] - o2[0];
			}
			
		});
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			int num = sc.nextInt();
			if (num != 0) {
				pq.offer(new int[]{Math.abs(num), num});
			
			}
			if (pq.size() > 0) {
				if (num == 0) {
					list.add(pq.poll()[1]);
				}
			}
			else if (pq.size() == 0) {
				list.add(0);
			}
		}
		for (int ans : list) {
			System.out.println(ans);
		}
	}
}