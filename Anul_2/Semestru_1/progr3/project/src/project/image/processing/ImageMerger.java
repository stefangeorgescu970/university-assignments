package project.image.processing;

import javafx.util.Pair;
import project.image.domain.Image;
import project.image.domain.Pixel;
import project.image.repository.ImageRepository;

import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;

/**
 * Singleton that is used for merging two images.
 */
public class ImageMerger {

    /**
     * Part of the code that turns this class into a singleton.
     */
    public final static ImageMerger INSTANCE = new ImageMerger();

    private ImageMerger() { }

    /**
     * Resize an image by a given factor, while maintaining its aspect ratio.
     * @param image - the image you need to resize, instance of class Image.
     * @param resizeFactor - the resize factor, given as a Float.
     * @return - an object of type Image with new size.
     */
    private Image resizeImage(Image image, Float resizeFactor){
        BufferedImage before = image.getBufferedImage(true);

        int newWidth = (int)( before.getWidth() * resizeFactor );
        int newHeight = (int)( before.getHeight() * resizeFactor );

        BufferedImage after = new BufferedImage(newWidth, newHeight, BufferedImage.TYPE_INT_ARGB);

        AffineTransform at = new AffineTransform();
        at.scale(resizeFactor, resizeFactor);
        AffineTransformOp scaleOp = new AffineTransformOp(at, AffineTransformOp.TYPE_BILINEAR);
        after = scaleOp.filter(before, after);

        return new Image(after, image.getTitle());
    }

    /**
     * Resize an image to new given size
     * @param image the image to be resized
     * @param newHeight the new height
     * @param newWidth the new width
     * @return an image of class Image, with required new params
     */
    private Image resizeImage(Image image, int newHeight, int newWidth) {
        BufferedImage before = image.getBufferedImage(true);

        BufferedImage after = new BufferedImage(newWidth, newHeight, BufferedImage.TYPE_INT_ARGB);

        final Graphics2D graphics2D = after.createGraphics();
        graphics2D.setComposite(AlphaComposite.Src);
        graphics2D.drawImage(before, 0, 0, newWidth, newHeight, null);
        graphics2D.dispose();

        return new Image(after, image.getTitle());
    }

    /**
     * Resize one of the two images received as parameters such that they fit in width.
     * @param image1 - first image given as an Image object.
     * @param image2 - second image given as an Image object.
     * @return - a pair of two objects of type Image, the key being the smaller image, while the value being the bigger.
     */
    private Pair<Image, Image> makeImagesFit (Image image1, Image image2, FittingMethod fittingMethod) {


        if(fittingMethod == FittingMethod.PRESERVE_RATIO) {
            if(image1.getWidth() < image2.getWidth()) {
                image2 = this.resizeImage(image2, ((float) (image1.getWidth()) / (float) (image2.getWidth())));
            } else {
                image1 = this.resizeImage(image1, ((float)(image2.getWidth()) / (float)(image1.getWidth())));
            }

            if (image1.getHeight() > image2.getHeight()){
                return new Pair<>(image2, image1);
            }
            return new Pair<>(image1, image2);
        } else {
            return new Pair<>(image1, this.resizeImage(image2, image1.getHeight(), image1.getWidth()));
        }

    }

    /**
     * Produces a new pixel from given two others while applying a hard mix algorithm.
     * @param pixel1 - first pixel, given as an object of type Pixel.
     * @param pixel2 - second pixel, also given as an object of type Pixel.
     * @return - a new pixel, object of type Pixel, with properties set accordingly.
     */
    private Pixel hardMixPixelMerge(Pixel pixel1, Pixel pixel2) {
        Pixel outputPixel = new Pixel();

        if(pixel1.getAlphaChannel() != 0 && pixel2.getAlphaChannel() != 0) {

            outputPixel.setAlphaChannel(255);

            if(pixel1.getRedChannel() + pixel2.getRedChannel() >= 255)
                outputPixel.setRedChannel(255);
            else
                outputPixel.setRedChannel(0);

            if(pixel1.getBlueChannel() + pixel2.getBlueChannel() >= 255)
                outputPixel.setBlueChannel(255);
            else
                outputPixel.setBlueChannel(0);

            if(pixel1.getGreenChannel() + pixel2.getGreenChannel() >= 255)
                outputPixel.setGreenChannel(255);
            else
                outputPixel.setGreenChannel(0);

        } else if (pixel1.getAlphaChannel() == 0) {
            outputPixel = pixel2;
        } else {
            outputPixel = pixel1;
        }

        return outputPixel;
    }

    /**
     * Produces a new pixel from given two others by getting the color between the given two.
     * @param pixel1 - first pixel, given as an object of type Pixel.
     * @param pixel2 - second pixel, also given as an object of type Pixel.
     * @return - a new pixel, object of type Pixel, with properties set accordingly.
     */
    private Pixel normalPixelMerge (Pixel pixel1, Pixel pixel2) {
        Pixel outputPixel = new Pixel();

        if(pixel1.getAlphaChannel() != 0 && pixel2.getAlphaChannel() != 0) {

            outputPixel.setAlphaChannel(255);

            int resultRed = (pixel1.getRedChannel() + pixel2.getRedChannel()) / 2;
            int resultGreen = (pixel1.getGreenChannel() + pixel2.getGreenChannel()) / 2;
            int resultBlue = (pixel1.getBlueChannel() + pixel2.getBlueChannel()) / 2;

            outputPixel.setRedChannel(resultRed);
            outputPixel.setGreenChannel(resultGreen);
            outputPixel.setBlueChannel(resultBlue);

        } else if (pixel1.getAlphaChannel() == 0) {
            outputPixel = pixel2;
        } else {
            outputPixel = pixel1;
        }

        return outputPixel;
    }

    /**
     * Produces a new pixel from given two others while applying xor on each level.
     * @param pixel1 - first pixel, given as an object of type Pixel.
     * @param pixel2 - second pixel, also given as an object of type Pixel.
     * @return - a new pixel, object of type Pixel, with properties set accordingly.
     */
    private Pixel xorPixelMerge(Pixel pixel1, Pixel pixel2) {
        Pixel outputPixel = new Pixel();

        if(pixel1.getAlphaChannel() != 0 && pixel2.getAlphaChannel() != 0) {

            outputPixel.setAlphaChannel(255);

            outputPixel.setRedChannel(Math.abs(pixel1.getRedChannel() - pixel2.getRedChannel()));
            outputPixel.setGreenChannel(Math.abs(pixel1.getGreenChannel() - pixel2.getGreenChannel()));
            outputPixel.setBlueChannel(Math.abs(pixel1.getBlueChannel() - pixel2.getBlueChannel()));

        } else if (pixel1.getAlphaChannel() == 0) {
            outputPixel = pixel2;
        } else {
            outputPixel = pixel1;
        }

        return outputPixel;
    }


    /**
     * Produces a new pixel from given two others while applying or on each level.
     * @param pixel1 - first pixel, given as an object of type Pixel.
     * @param pixel2 - second pixel, also given as an object of type Pixel.
     * @return - a new pixel, object of type Pixel, with properties set accordingly.
     */
    private Pixel orPixelMerge(Pixel pixel1, Pixel pixel2) {
        Pixel outputPixel = new Pixel();

        if(pixel1.getAlphaChannel() != 0 && pixel2.getAlphaChannel() != 0) {

            outputPixel.setAlphaChannel(255);

            if(pixel1.getRedChannel() > pixel2.getRedChannel())
                outputPixel.setRedChannel(pixel1.getRedChannel());
            else
                outputPixel.setRedChannel(pixel2.getRedChannel());

            if(pixel1.getBlueChannel() > pixel2.getBlueChannel())
                outputPixel.setBlueChannel(pixel1.getBlueChannel());
            else
                outputPixel.setBlueChannel(pixel2.getBlueChannel());

            if(pixel1.getGreenChannel() > pixel2.getGreenChannel())
                outputPixel.setGreenChannel(pixel1.getGreenChannel());
            else
                outputPixel.setGreenChannel(pixel2.getGreenChannel());

        } else if (pixel1.getAlphaChannel() == 0) {
            outputPixel = pixel2;
        } else {
            outputPixel = pixel1;
        }

        return outputPixel;
    }

    /**
     * Produces a new pixel from given two others while applying and on each level.
     * @param pixel1 - first pixel, given as an object of type Pixel.
     * @param pixel2 - second pixel, also given as an object of type Pixel.
     * @return - a new pixel, object of type Pixel, with properties set accordingly.
     */
    private Pixel andPixelMerge(Pixel pixel1, Pixel pixel2) {
        Pixel outputPixel = new Pixel();

        if(pixel1.getAlphaChannel() != 0 && pixel2.getAlphaChannel() != 0) {

            outputPixel.setAlphaChannel(255);

            if(pixel1.getRedChannel() < pixel2.getRedChannel())
                outputPixel.setRedChannel(pixel1.getRedChannel());
            else
                outputPixel.setRedChannel(pixel2.getRedChannel());

            if(pixel1.getBlueChannel() < pixel2.getBlueChannel())
                outputPixel.setBlueChannel(pixel1.getBlueChannel());
            else
                outputPixel.setBlueChannel(pixel2.getBlueChannel());

            if(pixel1.getGreenChannel() < pixel2.getGreenChannel())
                outputPixel.setGreenChannel(pixel1.getGreenChannel());
            else
                outputPixel.setGreenChannel(pixel2.getGreenChannel());

        } else if (pixel1.getAlphaChannel() == 0) {
            outputPixel = pixel2;
        } else {
            outputPixel = pixel1;
        }

        return outputPixel;
    }


    /**
     * Merges two given pixels using a certain merge variant.
     * @param pixel1 - a pixel, object of type Pixel.
     * @param pixel2 - still a pixel, object of type (you guessed it) Pixel.
     * @param mergeVariant - value from enum MergeVariant.
     * @return - the new pixel obtained accordingly or a transparent pixel if merge variant is incorrect.
     */
    private Pixel mergePixels(Pixel pixel1, Pixel pixel2, MergeVariant mergeVariant){
        switch (mergeVariant) {
            case NORMAL: return this.normalPixelMerge(pixel1, pixel2);
            case HARD_MIX: return this.hardMixPixelMerge(pixel1, pixel2);
            case XOR: return this.xorPixelMerge(pixel1, pixel2);
            case OR: return this.orPixelMerge(pixel1, pixel2);
            case AND: return this.andPixelMerge(pixel1, pixel2);
            default: return new Pixel();
        }
    }

    /**
     * Merge to given images using a certain merge variant. Firstly resize them using the resize algorithm provided by
     * the singleton, then merges them.
     * @param image1 - first image, object of type Image.
     * @param image2 - second image, object still of type Image.
     * @param mergeVariant - value from enum MergeVariant.
     * @return - a new image, object of type Image, where each pixel is a combination of the two corresponding in the
     *           images given as parameters.
     */
    private Image mergeImages(Image image1, Image image2, MergeVariant mergeVariant, FittingMethod fittingMethod) {

        Pair<Image, Image> resizedImages = this.makeImagesFit(image1, image2, fittingMethod);
        Image smallerImage = resizedImages.getKey();
        Image biggerImage = resizedImages.getValue();

        Image result = new Image(biggerImage.getHeight(), biggerImage.getWidth());

        for(int i = 0; i < smallerImage.getWidth(); i++){
            for(int j=0;j < smallerImage.getHeight(); j++) {
                Pixel pixel1 = smallerImage.getPixel(i, j);
                Pixel pixel2 = biggerImage.getPixel(i, j);
                Pixel resultPixel = this.mergePixels(pixel1, pixel2, mergeVariant);
                result.setPixel(i,j,resultPixel);
            }
        }

        for(int i = 0; i < biggerImage.getWidth(); i++) {
            for (int j = smallerImage.getHeight() ; j < biggerImage.getHeight(); j++) {
                result.setPixel(i,j,biggerImage.getPixel(i,j));
            }
        }

        return result;
    }

    /**
     * Build a new Repo out of merged images.
     * @param repo1 The first repo of images.
     * @param repo2 The second repo of images.
     * @param mergeMethod The merge method to use on pixels.
     * @return the repo, filled with images. If one repo has only one image, it will merge that image with all form the other repo.
     */
    public ImageRepository mergeImageRepos(ImageRepository repo1, ImageRepository repo2, MergeVariant mergeMethod, FittingMethod fittingMethod) {
        ImageRepository mergedRepo = new ImageRepository();

        if(repo1.getImages().size() == 1) {
            for(Image image : repo2.getImages()){
                mergedRepo.addImage(this.mergeImages(repo1.getImages().get(0), image, mergeMethod, fittingMethod));
            }
            return mergedRepo;
        } else if(repo2.getImages().size() == 1) {
            for(Image image : repo1.getImages()){
                mergedRepo.addImage(this.mergeImages(repo2.getImages().get(0), image, mergeMethod, fittingMethod));
            }
            return mergedRepo;
        } else {
            int i = 0, j = 0;

            while(i < repo1.getImages().size() && j < repo2.getImages().size() ) {
                mergedRepo.addImage(this.mergeImages(repo1.getImages().get(i), repo2.getImages().get(j), mergeMethod, fittingMethod));
                i++;
                j++;
            }

            while (i < repo1.getImages().size()) {
                mergedRepo.addImage(repo1.getImages().get(i));
                i++;
            }

            while (j < repo2.getImages().size()){
                mergedRepo.addImage(repo2.getImages().get(j));
                j++;
            }

            return mergedRepo;
        }
    }
}
