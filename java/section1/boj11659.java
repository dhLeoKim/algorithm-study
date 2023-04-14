import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj11659 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11659.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        long[] arr = new long[N+1];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for(int i = 1; i < N+1; i++) {
            arr[i] = arr[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }

        for(int m = 0; m < M; m++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(arr[j] - arr[i-1]);
        }
    }
}
