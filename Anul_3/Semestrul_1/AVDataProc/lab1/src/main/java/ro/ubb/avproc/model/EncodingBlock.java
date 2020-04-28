package ro.ubb.avproc.model;

import lombok.Data;
import ro.ubb.avproc.utils.MathUtils;

@Data
public class EncodingBlock {

    Integer size;
    Double[][] values;
    Integer imageOriginX;
    Integer imageOriginY;
    private EncodingBlockType encodingBlockType;

    public EncodingBlock(int size, int originX, int originY) {
        this.size = size;
        this.imageOriginX = originX;
        this.imageOriginY = originY;
        this.values = new Double[size][size];
    }

    public EncodingBlock(int[] intArray, int imageOriginX, int imageOriginY) {
        size =  (int) Math.sqrt(intArray.length);
        this.imageOriginX = imageOriginX;
        this.imageOriginY = imageOriginY;
        values = new Double[size][size];
        int currentPosition = 0;

        for (int i = 0; i < 2 * size - 1; i++) {
            if (i % 2 == 1) {
                // down left
                int x = i < size ? 0 : i - size + 1;
                int y = i < size ? i : size - 1;
                while (x < size && y >= 0) {
                    values[x++][y--] = (double) intArray[currentPosition ++];
                }
            } else {
                // up right
                int x = i < size ? i : size - 1;
                int y = i < size ? 0 : i - size + 1;
                while (x >= 0 && y < size) {
                    values[x--][y++] = (double) intArray[currentPosition ++];
                }
            }
        }
    }

    public void setValue(int width, int height, Double value) {
        this.values[width][height] = value;
    }

    public void subsample() {
        Double[][] newValues = new Double[this.size / 2][this.size / 2];

        for (int originX = 0; originX < this.size / 2; originX++) {
            for (int originY = 0; originY < this.size / 2; originY++) {

                Double totalValue = 0d;

                for (int currentWidth = originX * 2; currentWidth < originX * 2 + 2; currentWidth++) {
                    for (int currentHeight = originY * 2; currentHeight < originY * 2 + 2; currentHeight++) {
                        totalValue += this.values[currentWidth][currentHeight];
                    }
                }
                newValues[originX][originY] = totalValue / 4;
            }
        }

        this.values = newValues;
        this.size /= 2;
    }

    public void upsample() {
        Double[][] newValues = new Double[this.size * 2][this.size * 2];

        for (int originX = 0; originX < this.size; originX++) {
            for (int originY = 0; originY < this.size; originY++) {

                Double value = this.values[originX][originY];

                int newFrameOriginX = originX * 2;
                int newFrameOriginY = originY * 2;

                for (int currentLine = newFrameOriginX; currentLine < newFrameOriginX + 2; currentLine++) {
                    for (int currentColumn = newFrameOriginY; currentColumn < newFrameOriginY + 2; currentColumn++) {
                        newValues[currentLine][currentColumn] = value;
                    }
                }

            }
        }

        this.values = newValues;
        this.size *= 2;
    }

    public int[] getIntegerZigzagTraversal() {
        int[] result = new int[size * size];
        int t = 0;

        for (int i = 0; i < 2 * size - 1; i++) {
            if (i % 2 == 1) {
                // down left
                int x = i < size ? 0 : i - size + 1;
                int y = i < size ? i : size - 1;
                while (x < size && y >= 0) {
                    result[t++] = values[x++][y--].intValue();
                }
            } else {
                // up right
                int x = i < size ? i : size - 1;
                int y = i < size ? 0 : i - size + 1;
                while (x >= 0 && y < size) {
                    result[t++] = values[x--][y++].intValue();
                }
            }
        }

        return result;
    }
}
