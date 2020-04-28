package ro.ubb.avproc.model;

import lombok.Data;
import ro.ubb.avproc.utils.EncodingUtils;

import java.util.ArrayList;
import java.util.List;

@Data
public class EncodedYUV {

    private List<EncodingBlock> yBlocks = new ArrayList<>();
    private List<EncodingBlock> uBlocks = new ArrayList<>();
    private List<EncodingBlock> vBlocks = new ArrayList<>();

    public void subsample() {
        for (int i = 0; i < uBlocks.size(); i++) {
            this.uBlocks.get(i).subsample();
            this.vBlocks.get(i).subsample();
        }
    }

    public void upsample() {
        for (int i = 0; i < uBlocks.size(); i++) {
            this.uBlocks.get(i).upsample();
            this.vBlocks.get(i).upsample();
        }
    }

    public EncodedYUV() {

    }

    public EncodedYUV(EncodedDCT encodedDCT) {
        int size = encodedDCT.getYDctBlocks().size();
        for (int i = 0; i < size; i++) {
            yBlocks.add(EncodingUtils.performInverseDCT(encodedDCT.getYDctBlocks().get(i)));
            uBlocks.add(EncodingUtils.performInverseDCT(encodedDCT.getUDctBlocks().get(i)));
            vBlocks.add(EncodingUtils.performInverseDCT(encodedDCT.getVDctBlocks().get(i)));
        }
    }
}
