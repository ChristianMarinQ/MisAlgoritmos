// Adaptado de GeeksforGeeks
package search.algorithms;

public class JumpSearch {
    public static int search(int[] arr, int target) {
        int n = arr.length;
        int step = (int)Math.floor(Math.sqrt(n));
        int prev = 0;

        while (prev < n && arr[Math.min(step, n) - 1] < target) {
            prev = step;
            step += (int)Math.floor(Math.sqrt(n));
            if (prev >= n) return -1;
        }

        for (int i = prev; i < Math.min(step, n); i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
}
