import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
//		int max = (int) Math.sqrt(n);
//		Queue<Integer> que = new LinkedList<>();
		ArrayList<Integer> list = new ArrayList<>();
		int sum = 0;
		int cnt = 0;
		for (int i=2;i<=n;i++) {
			if (isPrime(i)) {
				list.add(i);
			}
		}
		if (list.size() == 0) {
			System.out.println(cnt);
		} else {
			if (list.get(list.size()-1) == n) {
				cnt += 1;
			}
			
			for (int i=0;i<list.size()-1;i++) {
				sum = list.get(i);
				if (sum == n) {
					cnt += 1;
					continue;
				} else {
					while (sum < n) {
						for (int j=i+1;j<list.size();j++) {
							sum += list.get(j);
							if (sum == n) {
								cnt += 1;
								break;
							} else if (sum > n) {
								break;
							}
						}
					}
				}
			}
			System.out.println(cnt);
		}
	}
	
	public static boolean isPrime(int n) {
		if (n % 2 == 0) {
			if (n==2) {
				return true;
			} else {
				return false;
			}
		} else {
			for (int i=3; i <= Math.sqrt(n);i+=2) {
				if (n%i==0) {
					return false;
				}
			}
			return true;
		}
		
	}
}