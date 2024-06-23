import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n+1];
		Deque<Integer> deq = new LinkedList<>();
		for (int i = 1; i < n+1; i++) {
			deq.add(i);
		}
		
		while (deq.size() > 1) {
			deq.pop();
			int top = deq.pollFirst();
			deq.add(top);
		}
		
		System.out.println(deq.getFirst());
	}
}