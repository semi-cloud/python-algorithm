import java.util.*;
import java.io.*;

public class bj_21608 {
    private static int arr[][];
    private static Map<Integer, List<Integer>> map;
    private static int[] dx = {1, -1, 0, 0}, dy = {0, 0, -1, 1};
    private static int N;

    public static void main(String[] args) throws Exception {
        int res = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        map = new HashMap<>();

        for(int i = 0; i < Math.pow(N, 2); i++) {
            st = new StringTokenizer(br.readLine());
            int student = 0;
            List<Integer> friend = new ArrayList<>();
            for(int j = 0; j <= 4; j++) {
                if(j == 0) student = Integer.parseInt(st.nextToken());
                else friend.add(Integer.parseInt(st.nextToken()));
            }
            map.put(student, friend);

            List<List<Integer>> friends = getNearFriends(student);
            friends.sort((a, b) -> {    // 1. 인접 학생 개수 내림 차순 2. 비어 있는 칸 내림 차순 3. 행 번호 오름차순 2. 열 번호 오름차순
                if (a.get(0) != b.get(0)) return Integer.compare(b.get(0), a.get(0));
                else if (a.get(1) != b.get(1)) return Integer.compare(b.get(1), a.get(1));
                else if (a.get(2) != b.get(2)) return Integer.compare(a.get(2), b.get(2));
                else return Integer.compare(a.get(3), a.get(3));
            });

            int x = friends.get(0).get(2), y = friends.get(0).get(3);
            arr[x][y] = student;
        }

        for(int i = 0; i < N; i++) {   // 2. 학생 만족도 구하기
            for(int j = 0; j < N; j++) {
                int near = 0;
                for(int k = 0; k < 4; k ++) {
                    int nx = i + dx[k], ny = j + dy[k];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

                    if(map.get(arr[i][j]).contains(arr[nx][ny])) near += 1;
                }
                res += Math.pow(10, near) / 10;
            }
        }
        System.out.println(res);
    }

    public static List<List<Integer>> getNearFriends(int cur) {
        List<List<Integer>> nearList = new ArrayList<>();   // (x, y, 인접 친구 개수, 빈칸 개수)
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(arr[i][j] != 0) continue;
                int blank = 0, likeFriend = 0;

                for(int k = 0; k < 4; k++) {
                    int nx = i + dx[k], ny = j + dy[k];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                    if(arr[nx][ny] == 0) blank +=1;

                    if(map.get(cur).contains(arr[nx][ny])) likeFriend += 1;  // 현재 넣으려는 학생의 좋아하는 학생들 수 찾기
                }
                nearList.add(Arrays.asList(likeFriend, blank, i, j));
            }
        }
        return nearList;
    }
}