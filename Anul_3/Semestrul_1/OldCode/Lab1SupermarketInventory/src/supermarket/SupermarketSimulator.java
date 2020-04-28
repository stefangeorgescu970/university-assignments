package supermarket;

import java.util.*;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by Sergiu on 05.10.2016.
 */
public class SupermarketSimulator {
    private class Bill {
        private Map<Integer, Integer> productQuantities;
        private int totalPrice;

        public Bill() {
            productQuantities = new HashMap<>();
        }

        public void addProduct(int productType, int quantity, int unitPrice) {
            if (productQuantities.containsKey(productType)) {
                productQuantities.put(productType, productQuantities.get(productType) + quantity);
            } else {
                productQuantities.put(productType, quantity);
            }
            totalPrice += unitPrice * quantity;
        }

        public int getTotalPrice() {
            return totalPrice;
        }

        public Set<Map.Entry<Integer, Integer>> getProductQuantities() {
            return productQuantities.entrySet();
        }
    }

    private static final int MAX_NO_PRODUCT_TYPES = 100;
    private static final int MAX_QUANTITY = 10000;
    private static final int MAX_PRICE = 100;
    private static final int MAX_NO_THREADS = 10;
    private static final int MAX_NO_SHOPPING_TIMES = 10;
    private static final int MILLISECONDS_BETWEEN_INVENTORIES = 10;
    private static final int MILLISECONDS_BETWEEN_SHOP_TIMES = 10;

    private List<Object> productLocks;
    private List<ReentrantLock> shoppingLocks;

    private List<Integer> quantities;
    private List<Integer> prices;

    private List<Integer> initialQuantities;

    private List<Bill> bills;
    private int numberOfProductTypes;
    private int money;

    private int numberOfThreads;
    private List<Thread> threads;

    private Thread inventoryThread;


    public SupermarketSimulator() {
        productLocks = new ArrayList<>();
        shoppingLocks = new ArrayList<>();

        initialQuantities = new ArrayList<>();
        prices = new ArrayList<>();
        Random rng = new Random();

        numberOfProductTypes = rng.nextInt(MAX_NO_PRODUCT_TYPES) + 1;
        productLocks.addAll(Stream
                .generate(() -> new Object())
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));
        initialQuantities.addAll(Stream
                .generate(() -> rng.nextInt(MAX_QUANTITY) + 1)
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));
        prices.addAll(Stream
                .generate(() -> rng.nextInt(MAX_PRICE) + 1)
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));

//        System.out.println(initialQuantities);


        numberOfThreads = rng.nextInt(MAX_NO_THREADS) + 1;

        shoppingLocks.addAll(Stream
                .generate(() -> new ReentrantLock())
                .limit(numberOfThreads)
                .collect(Collectors.toList()));

    }

    private void shop(int threadId, int shopNumber) {
        Random rng = new Random();
        Bill bill = new Bill();
        int quantity;

        for (int productType = 0; productType < numberOfProductTypes; productType++) {
            //Check if we want this product
            if (rng.nextBoolean()) {
                //lock this product type
                synchronized (productLocks.get(productType)) {
                    if (quantities.get(productType) > 0) {
                        quantity = rng.nextInt(Math.min(quantities.get(productType), MAX_QUANTITY / 500)) + 1;
                        bill.addProduct(productType, quantity, prices.get(productType));
                        quantities.set(productType, quantities.get(productType) - quantity);

                        System.out.println("Thread #" + threadId + " in shop time #" + shopNumber
                                + " bought " + quantity + " products of type " + productType);
                    }
                }
            }
        }

        synchronized (bills) {
            bills.add(bill);
            money += bill.getTotalPrice();
        }

    }

    private void shopping(int threadId) {
        Random rng = new Random();

        int numberOfShoppingTimes = rng.nextInt(MAX_NO_SHOPPING_TIMES) + 1;

        for (int shoppingTime = 0; shoppingTime < numberOfShoppingTimes; shoppingTime++) {
            shoppingLocks.get(threadId).lock();
            shop(threadId, shoppingTime);
            shoppingLocks.get(threadId).unlock();
            try {
                Thread.sleep(MILLISECONDS_BETWEEN_SHOP_TIMES);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    private boolean makeInventory() {
        //prevent a new shopping time from starting
        for (ReentrantLock lock : shoppingLocks) {
            lock.lock();
        }

        List<Integer> totalQuantities = new ArrayList<>();
        totalQuantities.addAll(quantities);

        int totalMoney = 0;

        for (Bill bill : bills) {
            totalMoney += bill.getTotalPrice();
            for (Map.Entry<Integer, Integer> entry : bill.getProductQuantities()) {
                totalQuantities.set(entry.getKey(), entry.getValue() + totalQuantities.get(entry.getKey()));
            }
        }

//        System.out.println(quantities);
//        System.out.println(totalQuantities);

        boolean everythingGood = true;

        if (totalMoney != money) {
            System.out.println("INVENTORY: problem with total money");
            everythingGood = false;
        }

        for (int productType = 0; productType < numberOfProductTypes; productType++) {
            if (!totalQuantities.get(productType).equals(initialQuantities.get(productType))) {
                System.out.println("INVENTORY: problem with quantity of product type #" + productType
                        + ": " + totalQuantities.get(productType) + " != " + initialQuantities.get(productType));
                everythingGood = false;
            }
        }

        if (everythingGood) {
            System.out.println("INVENTORY: everything as expected");
        }

        for (ReentrantLock lock : shoppingLocks) {
            lock.unlock();
        }
        return everythingGood;
    }

    private class InventoryRunnable implements Runnable {
        private boolean stopped = false;

        @Override
        public void run() {
            while (!stopped) {
                try {
                    Thread.sleep(MILLISECONDS_BETWEEN_INVENTORIES);
                    makeInventory();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        public void kill() {
            stopped = true;
        }
    }

    public void run() {
        quantities = new ArrayList<>();
        bills = new ArrayList<>();
        threads = new ArrayList<>();

        quantities.addAll(initialQuantities);

        threads.addAll(IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadId -> new Thread(() -> {
                    shopping(threadId);
                }))
                .collect(Collectors.toList())
        );

        InventoryRunnable inventoryRunnable = new InventoryRunnable();

        inventoryThread = new Thread(inventoryRunnable);
        inventoryThread.start();

        threads.stream().forEach(thread -> thread.start());

        for (Thread thread: threads) {
            try {
                thread.join();
            } catch (InterruptedException ex) {
                System.out.println("Thread was interrupted");
            }
        }

        inventoryRunnable.kill();
        try {
            inventoryThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        makeInventory();
    }
}
