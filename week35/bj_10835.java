// 탑 다운은 거꾸로 아래서부터 받은 값들 중에서 가장 최대값을 선택해나가고, 그러면 다시 루트로 올라왔을 때 최종 최대값이 나오겠지
// 따라서 sum 계산이 처음부터 이루어져서 내려가는게 아니라 아래 0에서부터 위로 올라오면서 최대값이 계산이 되어야함
// ex)               [3,2]
//     [2, 2]       [2, 4]       [3, 4]
// [5, 2] [5,1] [5, 4] [5, 1]  [2, 4] [2, 1]

import java.util.*;
import java.io.*;

public class bj_10835 {
    private static int[] a;
    private static int[] b;
    private static int dp[][];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        a = new int[N];
        b = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(solution(N, a, b));
    }

    public static int solution(int N, int[] a, int[] b) {
        dp = new int[N+1][N+1];
        for(int i = 0 ; i <= N; i++) {
            Arrays.fill(dp[i], -1);
        }
        return topDown(0, 0);
    }

    // 2. DP: 탑 다운(메모지에이션 : 상태 트리를 그려보면 왼쪽 카드와 오른쪽 카드의 경우의 수가 중복되어 나옴)
    public static int topDown(int left, int right) {  // 배열의 포인터
        if(dp[left][right] != -1) {     // 왼쪽 i번째 카드와 오른쪽 j번째 카드에서 점수 최대값
            return dp[left][right];
        }

        if(left >= a.length || right >= b.length) {   // 카드를 모두 소진한 경우 0에서 부터 올라오면서 최대값 계산 시작
            return 0;
        }

        if(b[right] < a[left]) {               // 오른쪽이 작다면 세가지 경우가 가능
            int l = topDown(left + 1, right);       // 왼쪽 버리는 경우
            int both = topDown(left + 1, right + 1);     // 둘다 버리는 경우
            int r = topDown(left, right + 1) + b[right];  // 오른쪽 버리는 경우
            dp[left][right] = Math.max(l, Math.max(both, r));
        } else {            // 아니라면 두 가지 경우
            dp[left][right] = Math.max(topDown(left + 1, right), topDown(left + 1, right + 1));
        }
        return dp[left][right];
    }

    // 3. 백트래킹
    // public void bt(int left, int right, int sum) {  // 배열의 포인터
    //     if(left >= a.length || right >= b.length) {
    //         res = Math.max(res, sum);
    //         return;
    //     }
    //     if(b[right] < a[left]) {
    //         topDown(left + 1, right, sum);
    //         topDown(left + 1, right + 1, sum);
    //         topDown(left, right + 1, sum + b[right]);
    //     } else {
    //         topDown(left + 1, right, sum);
    //         topDown(left + 1, right + 1, sum);
    //     }
    // }
}
