class Solution {
    static int cnt = 0;
    static boolean[] visited;  
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        visited = new boolean[dungeons.length];
        answer = dfs(0, k, dungeons);
        return answer;
    }
    
    public int dfs(int depth, int fatigue, int[][] dungeons) {
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i] || fatigue < dungeons[i][0]) {
                continue;
            }
            visited[i] = true;
            dfs(depth+1, fatigue - dungeons[i][1], dungeons);
            visited[i] = false;
        }
        cnt = Math.max(cnt, depth);
        return cnt;
    }
}