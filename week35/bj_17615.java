import java.util.*;
import java.io.*;

public class bj_17615 {
    static String[] balls;
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        balls = new String[N];
        int i = 0;
        for(String ball: br.readLine().split("")) {
            balls[i] = ball;
            i += 1;
        }

        int red = 0, blue = 0 ;
        for(String ball: balls) {      // 각 색깔별로 전체 볼 개수 세기
            if(ball.equals("R")) red += 1;
            else blue += 1;
        }

        int res = Math.min(getMinSwitchCount("R", red), getMinSwitchCount("B", blue)); // 빨강, 파랑 구슬 이동 최소
        System.out.println(res);
    }

    public static int getMinSwitchCount(String color, int totalCnt) {
        int leftNear = 0, rightNear = 0;
        for(int i = 0; i < balls.length; i++) {    // 왼쪽에서부터 연속하는 볼 개수 찾기
            if(balls[i].equals(color)) leftNear += 1;
            else break;
        }

        for(int i = balls.length-1; i >= 0; i--) {  // 오른쪽에서부터 연속하는 볼 개수 찾기
            if(balls[i].equals(color)) rightNear += 1;
            else break;
        }
        return Math.min(totalCnt - leftNear, totalCnt - rightNear);  // 전체 볼 개수 - 양쪽 연속하는 볼 개수 = 이동해야 하는 볼 개수
    }
}