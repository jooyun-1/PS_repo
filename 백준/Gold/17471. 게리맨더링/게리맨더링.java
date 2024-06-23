import java.util.*;

public class Main {

    static int N;
    static Map<Integer, Integer> human_num = new HashMap<>();
    static Map<Integer, List<Integer>> node = new HashMap<>();
    static List<Integer> visited;
    static boolean flag = false;
    static int minVal = Integer.MAX_VALUE;

    static int countVisited(List<Integer> visited) {
        int count = 0;
        for (int v : visited) {
            if (v == 1) {
                count++;
            }
        }
        return count;
    }

    static void dfs(int x, final List<Integer> arr) {
        visited.set(x, 1);

        if (countVisited(visited) == arr.size()) {
            flag = true;
            return;
        } else {
            for (int n : node.get(x)) {
                if (arr.contains(n) && visited.get(n) == 0) {
                    visited.set(n, 1);
                    dfs(n, arr);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();

        List<Integer> area = new ArrayList<>();
        for (int i = 0; i < N; ++i) {
            area.add(i + 1);
        }

        for (int i = 1; i <= N; ++i) {
            int num = scanner.nextInt();
            human_num.put(i, num);
        }

        for (int i = 1; i <= N; ++i) {
            int num = scanner.nextInt();
            List<Integer> temp = new ArrayList<>();
            for (int j = 0; j < num; ++j) {
                temp.add(scanner.nextInt());
            }
            node.put(i, temp);
        }

        for (int n = 1; n <= N; ++n) {
            List<List<Integer>> com = new ArrayList<>();
            for (int i = 0; i < (1 << N); ++i) {
                List<Integer> subset = new ArrayList<>();
                for (int j = 0; j < N; ++j) {
                    if ((i & (1 << j)) != 0) {
                        subset.add(area.get(j));
                    }
                }
                if (subset.size() == n) {
                    com.add(subset);
                }
            }

            for (List<Integer> c : com) {
                List<Integer> one = new ArrayList<>(c);
                List<Integer> two = new ArrayList<>();
                for (int a : area) {
                    if (!one.contains(a)) {
                        two.add(a);
                    }
                }

                visited = new ArrayList<>(Collections.nCopies(N + 1, 0));
                flag = false;
                dfs(one.get(0), one);

                if (flag) {
                    visited = new ArrayList<>(Collections.nCopies(N + 1, 0));
                    flag = false;
                    if (!two.isEmpty()) {
                        dfs(two.get(0), two);
                    }
                }

                if (flag) {
                    int cnt1 = 0, cnt2 = 0;
                    for (int o : one) {
                        cnt1 += human_num.get(o);
                    }
                    for (int t : two) {
                        cnt2 += human_num.get(t);
                    }
                    minVal = Math.min(minVal, Math.abs(cnt1 - cnt2));
                }
            }
        }

        if (minVal == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(minVal);
        }
    }
}