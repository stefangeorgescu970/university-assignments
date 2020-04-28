package main;

import java.util.*;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;
import java.util.stream.Collectors;

/**
 * Created by Sergiu on 01.02.2017.
 */
public class PermutationsGenerator {
    public int[] generatePermutation(int n, int numberOfThreads) {
        return generateSpecificPermutation(null, n, 0, numberOfThreads);
    }

    /**
     * n - number of elements in permutation
     * k - current position
     * */
    private int[] generateSpecificPermutation(int perm[], int n, int k, int numberOfThreads) {
//        int newPerm[];
        if (perm == null) {
            perm = new int[0];
        }
        int[] finalPerm = perm;
//        newPerm = Arrays.copyOfRange(perm, 0, k + 1);
        Set<Integer> used = new HashSet<Integer>(){{ for (int i : finalPerm) add(i); }};
        if (n == k + 1) {
            //no more splitting
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            for (int i = 0; i < n; i++) {
                if (!used.contains(i)) {
                    newPerm[k] = i;
                    if (check(newPerm)) {
                        return newPerm;
                    }
                }
            }
            return null;
        }
        int noRemainingValues = n - k;
        List<FutureTask<int[]>> futures = new ArrayList<>();
        if (numberOfThreads <= noRemainingValues) {//n - k = number of remaining possibilities
            int size = noRemainingValues / numberOfThreads;
            int index = 0;
            for (; index < n; index++) {
                if (!used.contains(index)) {
                    size--;
                    if (size <=0) {
                        index++;
                        break;
                    }
                }
            }
            int limitForFirst = index;
            for (int thId = 1; thId < numberOfThreads; thId++) {
                size = (noRemainingValues * (thId + 1)) / numberOfThreads - (noRemainingValues * thId) / numberOfThreads;
                int oldIndex = index;
                for (; index < n; index++) {
                    if (!used.contains(index)) {
                        size--;
                        if (size <=0) {
                            index++;
                            break;
                        }
                    }
                }
                int lastIndex = index;
                int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
                FutureTask<int[]> future = new FutureTask<>(()-> generateInRange(newPerm, n, k, used, oldIndex, lastIndex));
                futures.add(future);
                (new Thread(future)).start();
                if (index >= n) {
                    break;
                }
            }
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            int result[] = generateInRange(newPerm, n, k, used, 0, limitForFirst);
            if (result != null) {
                return result;
            }
        } else {
            int index = 1;
            int firstValue = 0;
            int i;
            for (i = 0; i < n; i++) {
                if (!used.contains(i)) {
                    firstValue = i;
                    i++;
                    break;
                }
            }
            for (; i < n; i++) {
                if (!used.contains(i)) {
                    int size = numberOfThreads * (index + 1) / noRemainingValues - numberOfThreads * index / noRemainingValues;
                    int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
                    newPerm[k] = i;
                    FutureTask<int[]> future = new FutureTask<>(() -> generateSpecificPermutation(newPerm, n, k + 1, size));
                    futures.add(future);
                    (new Thread(future)).start();
                    index++;
                }
            }
            int newPerm[] = Arrays.copyOfRange(perm, 0, k + 1);
            newPerm[k] = firstValue;
            int size = numberOfThreads / noRemainingValues;
            int result[] = generateSpecificPermutation(newPerm, n, k + 1, size);
            if (result != null) {
                return result;
            }
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

    private int[] generateInRange(int perm[], int n, int k, Set<Integer> used, int start, int end) {
        for (int i = start; i < end; i++) {
            if (!used.contains(i)) {
                perm[k] = i;
                int result[] = generateSpecificPermutation(perm, n, k + 1, 1);
                if (result != null) {
                    return result;
                }
            }
        }
        return null;
    }

    private synchronized boolean check(int[] perm) {
        for (int i : perm) {
            System.out.print(i + " ");
        }
        System.out.println();
        if ((perm[0] == 5) && (perm[1] == 4)) {
            return true;
        }
        return false;
    }
}
