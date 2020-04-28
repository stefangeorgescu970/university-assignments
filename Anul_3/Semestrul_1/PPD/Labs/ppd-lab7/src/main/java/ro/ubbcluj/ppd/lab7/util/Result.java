package ro.ubbcluj.ppd.lab7.util;

public class Result {
    private boolean resultIsPresent;
    private int result;

    public Result(boolean resultIsPresent, int result) {
        this.resultIsPresent = resultIsPresent;
        this.result = result;
    }

    public boolean isResultPresent() {
        return resultIsPresent;
    }

    public int getResult() {
        return result;
    }
}
