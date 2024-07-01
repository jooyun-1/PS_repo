class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean flag = false;
        int next_num = n + 1;
        String s = Integer.toBinaryString(n);
        while(true) {
            String next_s = Integer.toBinaryString(next_num);
            int cnt1 = 0;
            int cnt2 = 0;

            for(int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '1') {
                    cnt1 += 1;
                }
            }
            for(int i = 0; i < next_s.length(); i++) {
                if (next_s.charAt(i) == '1') {
                    cnt2 += 1;
                }
            }
            if (cnt1 == cnt2) {
                answer = next_num;
                break;
            } else {
                next_num += 1;
            }
        }
        return answer;
    }
}