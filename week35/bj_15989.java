// 1 + 1 + 2 == 2 + 1 + 1 == 1 + 2 + 1 다 같은 걸로 인식 필요
// 현재 노드보다 작은 숫자는 볼 필요가 없지(앞서서 작은 숫자에서 먼저 경우의 수를 체크했을 것)
// 재귀 완탐 + 메모지에이션 + 백트래킹으로 해도 시간 초과

// 1 - n 까지 숫자별로 경우의 수 구하기
// 중복을 막기 위해 오름차순 형태로 더하기가 되도록 해야함(1 + 1 + 2(O), 2 + 1 + 1(X)) => 2차원 배열 사용
// dp[i][j] = dp[i-1][1] + .. dp[i-1][j-1] + dp[i-1][j]
// 1, 2, 3 세가지로만 구성할 수 있음

import java.io.*;

public class bj_15989 {
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        dp = new int[10001][10001];  // dp[i][j] = i번째 수를 만들 수 있는 수식 중에 j 숫자로 끝나는 수식 개수
        dp[1][1] = 1;
        dp[2][1] = 1;
        dp[2][2] = 1;
        dp[3][1] = 1;
        dp[3][2] = 1;
        dp[3][3] = 1;

        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            for(int i = 4; i <= 10000; i++) {
                dp[i][1] = dp[i-1][1];    // 중복 방지 위해 오름차순 형태의 수식만 체크
                dp[i][2] = dp[i-2][1] + dp[i-2][2];
                dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3];

                // for(int j = 1; j <= 3; j++) {   // 1, 2, 3 으로만 숫자 구성 가능
                //     for(int k = 1; k <= 3; k++) {
                //         dp[i][j] += dp[i-j][k];
                //     }
                // }
            }
            System.out.println(dp[N][1] + dp[N][2] + dp[N][3]);
        }
    }
}