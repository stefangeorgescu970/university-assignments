package main;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Sergiu on 01.02.2017.
 */
public class Engine {
    public static void main(String args[]) {

//        List<Float> list = new ArrayList<>();
//
//        for(int i = 2; i <= 8; i ++) {
//            long start = System.currentTimeMillis();
//
//            int result[] = (new PermutationsGenerator()).generatePermutation(10, i);
//
//            // finding the time after the operation is executed
//            long end = System.currentTimeMillis();
//            //finding the time difference and converting it into seconds
//            float sec = (end - start) / 1000F; System.out.println(sec + " seconds");
//            list.add(sec);
//        }
//
//        for(int i = 2; i <= 8; i ++) {
//            System.out.println("Generating with " + i + " threads took " + list.get(i - 2) + " seconds.");
//        }


        int result[] = (new PermutationsGenerator()).generatePermutation(6, 2);
        System.out.println("result:");
        if (result == null) {
            System.out.println("null");
        } else {
            for (int i : result) {
                System.out.print(i + " ");
            }
        }
    }
}
