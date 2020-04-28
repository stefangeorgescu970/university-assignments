package util;

import java.util.Arrays;

/**
 * Created by Sergiu on 14.11.2016.
 */
public class Utils {
    private Utils() {}

    public static int[] noLeadingZeros(int a[]) {
        if (a[a.length - 1] == 0) {
            int limit = a.length;
            while (limit > 1 && a[limit - 1] == 0) {
                limit--;
            }
            a = Arrays.copyOfRange(a, 0, limit);
        }
        return a;
    }

    public static void reverse(int a[]) {
        int lim = a.length / 2;
        int aux;
        for (int i = 0; i < lim; i++) {
            aux = a[i];
            a[i] = a[a.length - i - 1];
            a[a.length - i - 1] = aux;
        }
    }

    public static int[] moveCarries(int a[]) {
        int result[] = new int[a.length + numberOfDigits(a[a.length - 1])]; // int[a.len + noDigits(a.last()) - 1 + 1]
        int carry = 0;
        int i;
        for (i = 0; i < a.length; i++) {
            result[i] = a[i] + carry;
            carry = result[i] / 10;
            result[i] %= 10;
        }
        i = a.length;
        while (carry > 0) {
            result[i] = carry % 10;
            carry /= 10;
            i++;
        }
        return result;
    }

    private static int numberOfDigits(int a) {
        int noDigits = 0;
        while (a > 0) {
            noDigits++;
            a /= 10;
        }
        return Math.min(1, noDigits);
    }

    public static int[] moveNegativeCarries(int a[]) {
        int carry = 0;
        int i;
        for (i = 0; i < a.length; i++) {
            a[i] += carry;
            carry = 0;
            while (a[i] < 0) {
                a[i] += 10;
                carry--;
            }
        }
        return a;
    }

}
