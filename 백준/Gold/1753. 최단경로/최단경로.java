import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {
    static int V, E;
    static int start;
    static ArrayList<int[]>[] adj;
    static int[] dist;
    static PriorityQueue<int[]> heap;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());

        adj = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int e = 0; e < E; e++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj[u].add(new int[]{w, v});
        }

        dist = new int[V + 1];
        heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        dijkstra(start);

        for (int i = 1; i <= V; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }
    }

    static void dijkstra(int start) {
        for (int i = 1; i <= V; i++) {
            dist[i] = Integer.MAX_VALUE;
        }

        dist[start] = 0;
        heap.offer(new int[]{0, start});

        while (!heap.isEmpty()) {
            int[] current = heap.poll();
            int nowWeight = current[0];
            int now = current[1];

            if (dist[now] < nowWeight) {
                continue;
            }

            for (int[] edge : adj[now]) {
                int nextWeight = edge[0] + nowWeight;
                int next = edge[1];
                if (nextWeight < dist[next]) {
                    dist[next] = nextWeight;
                    heap.offer(new int[]{nextWeight, next});
                }
            }
        }
    }
}