package ro.ubb.avproc.utils;

import ro.ubb.avproc.model.*;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.IntBuffer;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class EncodingUtils {

    public static int width;
    public static int height;

    public static EncodedYUV getEncodedYUV(ImageYUV imageYUV) {
        EncodedYUV encodedYUV = new EncodedYUV();
        SeparatedImageYUV separatedImageYUV = new SeparatedImageYUV(imageYUV);

        for (int originX = 0; originX < imageYUV.getHeight(); originX += 8) {
            for (int originY = 0; originY < imageYUV.getWidth(); originY += 8) {
                EncodingBlock encodingBlockY = new EncodingBlock(8, originX, originY);
                encodingBlockY.setEncodingBlockType(EncodingBlockType.Y);

                EncodingBlock encodingBlockU = new EncodingBlock(8, originX, originY);
                encodingBlockU.setEncodingBlockType(EncodingBlockType.U);

                EncodingBlock encodingBlockV = new EncodingBlock(8, originX, originY);
                encodingBlockV.setEncodingBlockType(EncodingBlockType.V);

                for (int currentLine = originX; currentLine < originX + 8; currentLine++) {
                    for (int currentColumn = originY; currentColumn < originY + 8; currentColumn++) {
                        encodingBlockY.setValue(currentLine - originX,
                                currentColumn - originY,
                                separatedImageYUV.getYComponents()[currentLine][currentColumn]);

                        encodingBlockU.setValue(currentLine - originX,
                                currentColumn - originY,
                                separatedImageYUV.getUComponents()[currentLine][currentColumn]);

                        encodingBlockV.setValue(currentLine - originX,
                                currentColumn - originY,
                                separatedImageYUV.getVComponents()[currentLine][currentColumn]);
                    }
                }

                encodedYUV.getYBlocks().add(encodingBlockY);
                encodedYUV.getUBlocks().add(encodingBlockU);
                encodedYUV.getVBlocks().add(encodingBlockV);
            }
        }

        return encodedYUV;
    }

    public static SeparatedImageYUV decodeYUV(EncodedYUV encodedYUV, int height, int width) {
        SeparatedImageYUV separatedImageYUV = new SeparatedImageYUV(height, width);

        for (int index = 0; index < encodedYUV.getYBlocks().size(); index++) {
            EncodingBlock yBlock = encodedYUV.getYBlocks().get(index);
            EncodingBlock uBlock = encodedYUV.getUBlocks().get(index);
            EncodingBlock vBlock = encodedYUV.getVBlocks().get(index);

            int originX = yBlock.getImageOriginX();
            int originY = yBlock.getImageOriginY();

            for (int currentLine = originX; currentLine < originX + yBlock.getSize(); currentLine++) {
                for (int currentColumn = originY; currentColumn < originY + yBlock.getSize(); currentColumn++) {
                    separatedImageYUV.getYComponents()[currentLine][currentColumn]
                            = yBlock.getValues()[currentLine - originX][currentColumn - originY];

                    separatedImageYUV.getUComponents()[currentLine][currentColumn]
                            = uBlock.getValues()[currentLine - originX][currentColumn - originY];

                    separatedImageYUV.getVComponents()[currentLine][currentColumn]
                            = vBlock.getValues()[currentLine - originX][currentColumn - originY];
                }
            }
        }

        return separatedImageYUV;
    }

    public static EncodingBlock performForwardDCT(EncodingBlock encodedYUVBlock) {
        EncodingBlock middleEncodingBlock = new EncodingBlock(encodedYUVBlock.getSize(), encodedYUVBlock.getImageOriginX(), encodedYUVBlock.getImageOriginY());

        for (int currentLine = 0; currentLine < encodedYUVBlock.getSize(); currentLine++) {
            for (int currentColumn = 0; currentColumn < encodedYUVBlock.getSize(); currentColumn++) {
                middleEncodingBlock.setValue(currentLine, currentColumn, encodedYUVBlock.getValues()[currentLine][currentColumn] - 128);
            }
        }

        EncodingBlock finalEncodingBlock = new EncodingBlock(encodedYUVBlock.getSize(), encodedYUVBlock.getImageOriginX(), encodedYUVBlock.getImageOriginY());


        for (int currentLineFinal = 0; currentLineFinal < encodedYUVBlock.getSize(); currentLineFinal++) {
            for (int currentColumnFinal = 0; currentColumnFinal < encodedYUVBlock.getSize(); currentColumnFinal++) {

                double initialCoefficient = MathUtils.alphaForDCT(currentLineFinal) * MathUtils.alphaForDCT(currentColumnFinal) / 4;

                double totalSum = 0;

                for (int currentLine = 0; currentLine < encodedYUVBlock.getSize(); currentLine++) {
                    for (int currentColumn = 0; currentColumn < encodedYUVBlock.getSize(); currentColumn++) {
                        double cos1 = Math.cos((2 * currentLine + 1) * Math.PI * currentLineFinal / 16);
                        double cos2 = Math.cos((2 * currentColumn + 1) * Math.PI * currentColumnFinal / 16);
                        totalSum += middleEncodingBlock.getValues()[currentLine][currentColumn] * cos1 * cos2;
                    }
                }

                finalEncodingBlock.setValue(currentLineFinal, currentColumnFinal, totalSum * initialCoefficient);
            }
        }

        return finalEncodingBlock;
    }

    public static EncodingBlock performInverseDCT(EncodingBlock encodedDCTBlock) {
        EncodingBlock result = new EncodingBlock(encodedDCTBlock.getSize(), encodedDCTBlock.getImageOriginX(), encodedDCTBlock.getImageOriginY());


        for (int currentLineFinal = 0; currentLineFinal < encodedDCTBlock.getSize(); currentLineFinal++) {
            for (int currentColumnFinal = 0; currentColumnFinal < encodedDCTBlock.getSize(); currentColumnFinal++) {

                double totalSum = 0;

                for (int currentLine = 0; currentLine < encodedDCTBlock.getSize(); currentLine++) {
                    for (int currentColumn = 0; currentColumn < encodedDCTBlock.getSize(); currentColumn++) {
                        double coefficient = MathUtils.alphaForDCT(currentLine) * MathUtils.alphaForDCT(currentColumn);


                        double cos1 = Math.cos((2 * currentLineFinal + 1) * Math.PI * currentLine / 16);
                        double cos2 = Math.cos((2 * currentColumnFinal + 1) * Math.PI * currentColumn / 16);
                        totalSum += encodedDCTBlock.getValues()[currentLine][currentColumn] * cos1 * cos2 * coefficient;
                    }
                }

                result.setValue(currentLineFinal, currentColumnFinal, totalSum / 4);
            }
        }


        for (int currentLine = 0; currentLine < result.getSize(); currentLine++) {
            for (int currentColumn = 0; currentColumn < result.getSize(); currentColumn++) {
                result.setValue(currentLine, currentColumn, result.getValues()[currentLine][currentColumn] + 128);
            }
        }

        return result;
    }

    public static int[] encodeIntArray(int[] coefficients) {
        List<Integer> integerList = new ArrayList<>();

        int dcCoefficient = coefficients[0];
        integerList.add(MathUtils.getSizeFromAmplitude(dcCoefficient));
        integerList.add(dcCoefficient);

        int numberOfPreviousZeros = 0;

        for (int i = 1; i < coefficients.length; i++) {
            if (coefficients[i] == 0) {
                numberOfPreviousZeros++;
                continue;
            }

            integerList.add(numberOfPreviousZeros);
            integerList.add(MathUtils.getSizeFromAmplitude(coefficients[i]));
            integerList.add(coefficients[i]);
            numberOfPreviousZeros = 0;
        }

        integerList.add(0);
        integerList.add(0);

        int[] ret = new int[integerList.size()];
        Iterator<Integer> iterator = integerList.iterator();

        for (int i = 0; i < ret.length; i++) {
            ret[i] = iterator.next();
        }

        return ret;
    }

    public static byte[] encodeToByteArray(EncodedDCT encodedDCT) throws IOException {
        int numberOfBlocks = encodedDCT.getYDctBlocks().size();
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        DataOutputStream dataOutputStream = new DataOutputStream(byteArrayOutputStream);

        for (int i = 0; i < numberOfBlocks; i++) {
            int[] intsY = encodedDCT.getYDctBlocks().get(i).getIntegerZigzagTraversal();
            int[] intsCb = encodedDCT.getUDctBlocks().get(i).getIntegerZigzagTraversal();
            int[] intsCr = encodedDCT.getVDctBlocks().get(i).getIntegerZigzagTraversal();

            int[] convertedIntsY = encodeIntArray(intsY);
            int[] convertedIntsCb = encodeIntArray(intsCb);
            int[] convertedIntsCr = encodeIntArray(intsCr);

            for (int j = 0; j < convertedIntsY.length; j++) dataOutputStream.writeInt(convertedIntsY[j]);
            for (int j = 0; j < convertedIntsCb.length; j++) dataOutputStream.writeInt(convertedIntsCb[j]);
            for (int j = 0; j < convertedIntsCr.length; j++) dataOutputStream.writeInt(convertedIntsCr[j]);
        }

        return byteArrayOutputStream.toByteArray();
    }

    private static int createCurrentBuffer(int[] array, int[] currentBuffer, int currentPosition) {
        int currentBufferPosition = 0, amplitude, numberOfPreviousZeros;

        currentPosition++; // skip size from dc coefficient

        currentBuffer[currentBufferPosition++] = array[currentPosition++]; // add array of dc coefficient

        for (int i = 1; i <= 63; i++) {
            if (array[currentPosition] == 0 && array[currentPosition + 1] == 0) { // if we reached the end
                for (int index = currentBufferPosition; index < currentBuffer.length; index++) { // add zeros
                    currentBuffer[index] = 0;
                }
                return currentPosition + 2;
            }

            // read the parts of the tuple we need
            numberOfPreviousZeros = array[currentPosition++];
            currentPosition++;
            amplitude = array[currentPosition++];

            for (int index = 0; index < numberOfPreviousZeros; index++) { // add trailing zeros
                currentBuffer[currentBufferPosition++] = 0;
            }

            currentBuffer[currentBufferPosition++] = amplitude;
        }

        return currentPosition;
    }

    public static EncodedDCT decodeFromByteArray(byte[] bytes) {
        EncodedDCT encodedDCT = new EncodedDCT();

        IntBuffer intBuf = ByteBuffer.wrap(bytes)
                .order(ByteOrder.BIG_ENDIAN)
                .asIntBuffer();
        int[] array = new int[intBuf.remaining()];
        intBuf.get(array);

        int currentPosition = 0;
        int currentXOrigin = 0;
        int currentYOrigin = 0;

        while (currentPosition < array.length) {

            int[] currentBuffer = new int[64];

            currentPosition = createCurrentBuffer(array, currentBuffer, currentPosition);
            EncodingBlock encodingBlockDCTy = new EncodingBlock(currentBuffer, currentXOrigin, currentYOrigin);

            currentBuffer = new int[64];
            currentPosition = createCurrentBuffer(array, currentBuffer, currentPosition);
            EncodingBlock encodingBlockDCTb = new EncodingBlock(currentBuffer, currentXOrigin, currentYOrigin);

            currentBuffer = new int[64];
            currentPosition = createCurrentBuffer(array, currentBuffer, currentPosition);
            EncodingBlock encodingBlockDCTr = new EncodingBlock(currentBuffer, currentXOrigin, currentYOrigin);

            encodedDCT.getYDctBlocks().add(encodingBlockDCTy);
            encodedDCT.getUDctBlocks().add(encodingBlockDCTb);
            encodedDCT.getVDctBlocks().add(encodingBlockDCTr);

            currentYOrigin += 8;
            if (currentYOrigin >= width) {
                currentYOrigin = 0;
                currentXOrigin += 8;
            }
        }

        return encodedDCT;
    }
}
