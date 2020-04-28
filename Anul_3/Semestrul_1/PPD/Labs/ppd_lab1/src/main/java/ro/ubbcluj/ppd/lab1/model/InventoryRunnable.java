package ro.ubbcluj.ppd.lab1.model;


public class InventoryRunnable implements Runnable {
    private boolean stopped = false;
    private SupermarketSimulator supermarketSimulator;

    InventoryRunnable(SupermarketSimulator supermarketSimulator) {
        this.supermarketSimulator = supermarketSimulator;
    }

    @Override
    public void run() {
        while (!stopped) {
            try {
                Thread.sleep(Constants.MILLISECONDS_BETWEEN_INVENTORIES);
                supermarketSimulator.makeInventory();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void kill() {
        stopped = true;
    }
}