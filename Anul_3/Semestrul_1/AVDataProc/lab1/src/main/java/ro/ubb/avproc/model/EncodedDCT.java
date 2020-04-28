package ro.ubb.avproc.model;

import lombok.Data;
import ro.ubb.avproc.utils.EncodingUtils;
import ro.ubb.avproc.utils.MathUtils;

import java.util.ArrayList;
import java.util.List;


@Data
public class EncodedDCT {
    private List<EncodingBlock> yDctBlocks = new ArrayList<>();
    private List<EncodingBlock> uDctBlocks = new ArrayList<>();
    private List<EncodingBlock> vDctBlocks = new ArrayList<>();

    public EncodedDCT() {

    }

    public EncodedDCT(EncodedYUV encodedYUV) {
        int size = encodedYUV.getYBlocks().size();
        for (int i = 0; i < size; i++) {
            yDctBlocks.add(EncodingUtils.performForwardDCT(encodedYUV.getYBlocks().get(i)));
            uDctBlocks.add(EncodingUtils.performForwardDCT(encodedYUV.getUBlocks().get(i)));
            vDctBlocks.add(EncodingUtils.performForwardDCT(encodedYUV.getVBlocks().get(i)));
        }
    }

    public void applyQuantisation() {
        for (int i = 0; i < yDctBlocks.size(); i++) {
            MathUtils.applyQuantisation(yDctBlocks.get(i));
            MathUtils.applyQuantisation(uDctBlocks.get(i));
            MathUtils.applyQuantisation(vDctBlocks.get(i));
        }
    }

    public void applyDequantisation() {
        for (int i = 0; i < yDctBlocks.size(); i++) {
            MathUtils.applyDequantisation(yDctBlocks.get(i));
            MathUtils.applyDequantisation(uDctBlocks.get(i));
            MathUtils.applyDequantisation(vDctBlocks.get(i));
        }
    }
}
