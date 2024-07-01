class Solution {
    public int solution(int n) {
        int answer = 1;
        for(int i = 1; i <= n/2; i++) {
            int temp = i;
            for (int j = i + 1; temp < n; j++) {
                temp += j;
                if (temp == n) {
                    answer += 1;
                    break;
                }
            }
        }

        return answer;
    }
}