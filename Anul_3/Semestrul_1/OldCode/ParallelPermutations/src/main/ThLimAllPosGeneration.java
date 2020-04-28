package main;

import java.util.*;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;
import java.util.stream.Collectors;

/**
 * Created by Sergiu on 01.02.2017.
 */
public class ThLimAllPosGeneration {
    public int[] generateAllPos(int n, int depthLimit) {
        return generateSpecificAllPos(null, n, 0, depthLimit - 1);
    }

    /**
     * n - number of elements in permutation
     * k - current position
     * */
    private int[] generateSpecificAllPos(int perm[], int n, int k, int depthLimit) {
        if (perm == null) {
            perm = new int[0];
        }
        if (n == k + 1) {
            //no more splitting
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            for (int i = 0; i < n; i++) {
                newPerm[k] = i;
                if (check(newPerm)) {
                    return newPerm;
                }
            }
            return null;
        }
        if (depthLimit <= 0) {
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            int result[];
            for (int i = 0; i < n; i++) {
                newPerm[k] = i;
                result = generateSpecificAllPos(newPerm, n, k + 1, depthLimit - 1);
                if (result != null) {
                    return result;
                }
            }
            return null;
        }
        List<FutureTask<int[]>> futures = new ArrayList<>();
        int i;
        for (i = 1; i < n; i++) {
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            newPerm[k] = i;
            FutureTask<int[]> future = new FutureTask<>(() -> generateSpecificAllPos(newPerm, n, k + 1, depthLimit - 1));
            futures.add(future);
            (new Thread(future)).start();
        }
        int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
        newPerm[k] = 0;
        int mainThResult[] = generateSpecificAllPos(newPerm, n, k + 1, depthLimit - 1);
        if (mainThResult != null) {
            return mainThResult;
        }
        List<int[]> results = futures.stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (InterruptedException | ExecutionException e) {
                        return null;
                    }
                })
                .filter(result -> result != null)
                .collect(Collectors.toList());
        if (results.size() > 0) {
            return results.get(0);
        }
        // nothing found
        return null;
    }

    private synchronized boolean check(int[] perm) {
        for (int i : perm) {
            System.out.print(i + " ");
        }
        System.out.println();
        if (perm.length > 1 && (perm[0] == 2) && (perm[1] == 1)) {
            return true;
        }
        return false;
    }
}
