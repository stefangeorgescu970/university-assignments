package ro.ubb.avproc;

import ro.ubb.avproc.model.*;
import ro.ubb.avproc.utils.EncodingUtils;
import ro.ubb.avproc.utils.FileUtils;

import java.io.IOException;

public class Runner {
    public static void main(String[] args) {
        try {
            // Lab 1 encoding

            ImageRGB image = FileUtils.readImageFromFile("nt-P3.ppm");

            EncodingUtils.width = image.getWidth();
            EncodingUtils.height = image.getHeight();

            ImageYUV imageYUV = new ImageYUV(image);
            EncodedYUV encodedYUV = EncodingUtils.getEncodedYUV(imageYUV);
            encodedYUV.subsample();
            encodedYUV.upsample();


            // Lab 2 encoding

            EncodedDCT encodedDCT = new EncodedDCT(encodedYUV);
            encodedDCT.applyQuantisation();

            // Lab 3 encoding

            byte[] byteArray = EncodingUtils.encodeToByteArray(encodedDCT);

            // Lab 3 decoding

            EncodedDCT encodedDCTFromBytes = EncodingUtils.decodeFromByteArray(byteArray);


            // Lab 2 decoding

            encodedDCTFromBytes.applyDequantisation();
            EncodedYUV newEncodedYUV = new EncodedYUV(encodedDCTFromBytes);

            // Lab 1 decoding

            SeparatedImageYUV separatedImageYUV = EncodingUtils.decodeYUV(newEncodedYUV, image.getHeight(), image.getWidth());
            ImageYUV afterProcessImageYUV = new ImageYUV(separatedImageYUV);
            ImageRGB afterProcessImageRGB = new ImageRGB(afterProcessImageYUV);
            afterProcessImageRGB.setMaximumChannelValue(image.getMaximumChannelValue());
            FileUtils.dumpImageToFile(afterProcessImageRGB, "processedDog.ppm");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
