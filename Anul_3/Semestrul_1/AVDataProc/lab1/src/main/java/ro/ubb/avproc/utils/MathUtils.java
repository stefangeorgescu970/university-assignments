package ro.ubb.avproc.utils;

import ro.ubb.avproc.model.EncodingBlock;

public class MathUtils {

    private static double[][] quantisationMatrix = new double[][]{
            {6, 4, 4, 6, 10, 16, 20, 24},
            {5, 5, 6, 8, 10, 23, 24, 22},
            {6, 5, 6, 10, 16, 23, 28, 22},
            {6, 7, 9, 12, 20, 35, 32, 25},
            {7, 9, 15, 22, 27, 44, 41, 31},
            {10, 14, 22, 26, 32, 42, 45, 37},
            {20, 26, 31, 35, 41, 48, 48, 40},
            {29, 37, 38, 39, 45, 40, 41, 40}
    };

    public static double alphaForDCT(double value) {
        if (value > 0) {
            return 1;
        }
        return 1 / Math.sqrt(2);
    }

    public static void applyQuantisation(EncodingBlock encodingBlock) {
        for (int currentLine = 0; currentLine < encodingBlock.getSize(); currentLine++) {
            for (int currentColumn = 0; currentColumn < encodingBlock.getSize(); currentColumn++) {
                encodingBlock.setValue(currentLine, currentColumn, new Double(Math.round(encodingBlock.getValues()[currentLine][currentColumn] / quantisationMatrix[currentLine][currentColumn])));
            }
        }
    }

    public static void applyDequantisation(EncodingBlock encodingBlock) {
        for (int currentLine = 0; currentLine < encodingBlock.getSize(); currentLine++) {
            for (int currentColumn = 0; currentColumn < encodingBlock.getSize(); currentColumn++) {
                encodingBlock.setValue(currentLine, currentColumn, encodingBlock.getValues()[currentLine][currentColumn] * quantisationMatrix[currentLine][currentColumn]);
            }
        }
    }

    public static int getSizeFromAmplitude(int amplitude) {
        amplitude = Math.abs(amplitude);
        for (int i = 0; ; i++) {
            if (Math.pow(2, i) > amplitude) {
                return i;
            }
        }
    }
}
