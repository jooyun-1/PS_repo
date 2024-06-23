import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		ArrayDeque<Integer> que=new ArrayDeque<>();
		StringBuilder sb=new StringBuilder();
		
		for(int i=0;i<N;i++) {
			String s=sc.next();
			
			switch(s) {
				case "push_front":
					int x=sc.nextInt();
					que.addFirst(x);
					break;
				case "push_back":
					int a=sc.nextInt();
					que.addLast(a);
					break;
				case "pop_front":
					if(!que.isEmpty()) {
						sb.append(que.pollFirst()+"\n");
					}else {
						sb.append("-1"+"\n");
					}
					break;
				case "pop_back":
					if(!que.isEmpty()) {
						sb.append(que.pollLast()+"\n");
					}else {
						sb.append("-1"+"\n");
					}
					break;
				case "size":
					sb.append(que.size()+"\n");
					break;
				case "empty":
					if(que.isEmpty()) {
						sb.append("1"+"\n");
						
					}else {
						sb.append("0"+"\n");
					}
					break;
				case "front":
					if(!que.isEmpty()) {
						sb.append(que.peekFirst()+"\n");
					}else {
						sb.append("-1"+"\n");
					}
					break;
				case "back":
					if(!que.isEmpty()) {
						sb.append(que.peekLast()+"\n");
					}else {
						sb.append("-1"+"\n");
					}
					break;
				default:
					break;
			}
		}
		System.out.println(sb.toString());
	}
}