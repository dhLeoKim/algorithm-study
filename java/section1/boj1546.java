import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class boj1546 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1546.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        long sum = 0;
        long max = 0;

        for (int i = 0; i < N; i++) {
            int temp = sc.nextInt();
            if (temp > max) max = temp;
            sum += temp;
        }

        System.out.println(sum*100.0/max/N);
    }
}
