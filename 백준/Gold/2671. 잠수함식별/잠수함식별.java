import java.util.ArrayList;
import java.util.Scanner;

public class Main {
public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	String s = sc.next();
	boolean check = s.matches("(100+1+|01)+");
	if (check) {
		System.out.println("SUBMARINE");
	} else {
		System.out.println("NOISE");
	}

}
}