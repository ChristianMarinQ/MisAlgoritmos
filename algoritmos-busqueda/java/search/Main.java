package search;

import java.io.*;
import java.util.*;
import search.algorithms.BinarySearch;
import search.algorithms.TernarySearch;
import search.algorithms.JumpSearch;
import search.utils.Time;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] sizes = {10000, 100000, 1000000};
        List<String[]> results = new ArrayList<>();
        new File("results").mkdirs();

        for (int size : sizes) {
            int[] arr = loadArray("data/data_" + size + ".txt");
            Arrays.sort(arr);
            int target = arr[new Random().nextInt(arr.length)];

            System.out.println("\nArray size: " + size);

            long binaryTime = Time.measure(() -> BinarySearch.search(arr, target));
            long ternaryTime = Time.measure(() -> TernarySearch.search(arr, target));
            long jumpTime = Time.measure(() -> JumpSearch.search(arr, target));

            System.out.println("Binary Search: " + binaryTime + " ms");
            System.out.println("Ternary Search: " + ternaryTime + " ms");
            System.out.println("Jump Search: " + jumpTime + " ms");

            results.add(new String[]{"Java", String.valueOf(size),
                    String.valueOf(binaryTime), String.valueOf(ternaryTime), String.valueOf(jumpTime)});
        }

        writeCSV(results, "results/results_java.csv");
        System.out.println("\n Resultados guaradados en resultados/results_java.csv");
    }

    private static int[] loadArray(String filePath) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            return br.lines().mapToInt(Integer::parseInt).toArray();
        }
    }

    private static void writeCSV(List<String[]> data, String path) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(path))) {
            writer.write("Language,Array Size,Binary,Ternary,Jump\n");
            for (String[] row : data) {
                writer.write(String.join(",", row));
                writer.newLine();
            }
        }
    }
}
