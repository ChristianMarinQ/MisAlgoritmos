package search.utils;

public class Time {
    public static long measure(Runnable function) {
        long start = System.nanoTime();
        function.run();
        long end = System.nanoTime();
        return (end - start) / 1_000_000; // milliseconds
    }
}
