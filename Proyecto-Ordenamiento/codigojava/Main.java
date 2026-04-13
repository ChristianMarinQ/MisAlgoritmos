package codigojava;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String archivoDatos = "../Proyecto-Ordenamiento/datos/datos.txt";
        String archivoResultados = "../Proyecto-Ordenamiento/resultados/resultados_java.csv";
        new File("../Proyecto-Ordenamiento/resultados").mkdirs();

        int[] tamanos = {10_000, 100_000, 1_000_000};
        String[] algoritmos = {"Shaker", "DualPivotQuickSort", "Heap", "Merge", "Radix"};

        for (int n : tamanos) {
            int[] datos = leerDatos(archivoDatos, n);
            for (String algoritmo : algoritmos) {
                int[] copia = Arrays.copyOf(datos, datos.length);
                long inicio = System.nanoTime();

                switch (algoritmo) {
                    case "Shaker" -> AlgoritmosOrdenamiento.shakerSort(copia);
                    case "DualPivotQuickSort" -> AlgoritmosOrdenamiento.dualPivotQuickSort(copia);
                    case "Heap" -> AlgoritmosOrdenamiento.heapSort(copia);
                    case "Merge" -> AlgoritmosOrdenamiento.mergeSort(copia, 0, copia.length - 1);
                    case "Radix" -> AlgoritmosOrdenamiento.radixSort(copia);
                }

                long fin = System.nanoTime();
                double tiempo = (fin - inicio) / 1_000_000_000.0;
                guardarResultado(archivoResultados, algoritmo, n, tiempo);
                System.out.printf("%s (%d): %.3f s%n", algoritmo, n, tiempo);
            }
        }
        System.out.println("Resultados guardados en " + archivoResultados);
    }

    private static int[] leerDatos(String ruta, int n) throws IOException {
        int[] arr = new int[n];
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            for (int i = 0; i < n; i++)
                arr[i] = Integer.parseInt(br.readLine());
        }
        return arr;
    }

    private static void guardarResultado(String archivo, String algoritmo, int n, double tiempo) throws IOException {
        try (FileWriter fw = new FileWriter(archivo, true)) {
            fw.write(algoritmo + ",Java," + n + "," + tiempo + "\n");
        }
    }
}
