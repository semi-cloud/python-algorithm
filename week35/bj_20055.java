import java.util.*;
import java.io.*;

public class bj_20055 {
    static int N, K;
    static int turn = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N*2];
        for(int i = 0; i < N * 2; i++) {
            arr[i] = Integer.parseInt(st.nextToken());   // 내구도 배열
        }

        int zero = 0;    // 내구도가 0인 칸의 개수, 벨트 위에 올라가 있는 로봇 개수
        int upIdx = 0, downIdx = N-1;    // 직접 배열을 회전 시키지 않고, 올리는 위치와 내리는 위치 인덱스만 회전하도록 변경
        Queue<Integer> q = new LinkedList<>();
        boolean[] visit = new boolean[2 * N];

        while(zero < K) {
            upIdx = ((upIdx - 1) + arr.length) % arr.length;   // 실제 벨트는 가만히 냅두고, 올리는 위치와 내리는 위치를 이동
            downIdx = ((downIdx - 1) + arr.length) % arr.length;

            int size = q.size();        // 큐 사이즈를 따로 안빼두면 계속 바뀜
            for(int i = 0; i < size; i++) {     // 1-2. 내리는 위치가 이동하면서 큐에 있는 로봇들이 해당 자리로 가는지 체크
                int cur = q.poll();
                visit[cur] = false;
                if(cur == downIdx) continue;        // 벨트가 이동하면서 로봇이 내리는 위치로 갔는지 확인

                int next = (cur + 1) % arr.length;
                if(!visit[next] && arr[next] > 0) {   // 로봇이 없으며, 내구도가 1 이상 남아 있는 경우만 다음 칸으로 이동
                    arr[next] -= 1;
                    if(arr[next] == 0) zero += 1;
                    if(next != downIdx) {
                        q.offer(next);  // 내리는 위치가 아닌 경우에만 다음으로 이동
                        visit[next] = true;
                    }
                } else {
                    visit[cur] = true;
                    q.offer(cur);      // 이동하지 못한다면 원래 위치를 큐에 추가
                }
            }

            // 3. 로봇 올리기
            if(!visit[upIdx] && arr[upIdx] > 0) {
                visit[upIdx] = true;
                q.offer(upIdx);     // 큐에 새로운 로봇을 추가하고 해당 칸 내구도 -1
                arr[upIdx] -= 1;
                if(arr[upIdx] == 0) zero += 1;
            }
            turn += 1;
        }
        System.out.println(turn);
    }
}