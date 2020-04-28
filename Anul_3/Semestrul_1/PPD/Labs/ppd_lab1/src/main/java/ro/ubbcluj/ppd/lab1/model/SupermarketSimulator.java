package ro.ubbcluj.ppd.lab1.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Created by Stefan on 14.10.2018.
 */
public class SupermarketSimulator {

    // Lists for locks, first for locking an object, second one for locking a shopping process.
    private List<Object> productLocks;
    private List<ReentrantLock> shoppingLocks;

    // Representation of products.
    private List<Integer> quantities;
    private List<Integer> prices;
    private List<Integer> initialQuantities;
    private int numberOfProductTypes;

    // Representation of bills.
    private List<Bill> bills;
    private int money;

    // Threads in app.
    private int numberOfThreads;
    private List<Thread> threads;
    private Thread inventoryThread;


    public SupermarketSimulator() {
        productLocks = new ArrayList<>();
        shoppingLocks = new ArrayList<>();

        initialQuantities = new ArrayList<>();
        prices = new ArrayList<>();
        Random rng = new Random();

        numberOfProductTypes = rng.nextInt(Constants.MAXIMUM_NUMBER_OF_PRODUCT_TYPES) + 1;

        productLocks.addAll(Stream
                .generate(Object::new)
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));

        initialQuantities.addAll(Stream
                .generate(() -> rng.nextInt(Constants.MAX_QUANTITY) + 1)
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));

        prices.addAll(Stream
                .generate(() -> rng.nextInt(Constants.MAX_PRICE) + 1)
                .limit(numberOfProductTypes)
                .collect(Collectors.toList()));

        System.out.println(initialQuantities);

        numberOfThreads = rng.nextInt(Constants.MAX_NO_THREADS) + 1;

        shoppingLocks.addAll(Stream
                .generate(ReentrantLock::new)
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

                        // Divide a big number by 500 to improve randomness.
                        quantity = rng.nextInt(Math.min(quantities.get(productType), Constants.MAX_QUANTITY / 500)) + 1;
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

        // Decide how many times this thread will shop.
        int numberOfShoppingTimes = rng.nextInt(Constants.MAX_NO_SHOPPING_TIMES) + 1;

        for (int shoppingTime = 0; shoppingTime < numberOfShoppingTimes; shoppingTime++) {

            shoppingLocks.get(threadId).lock();
            shop(threadId, shoppingTime);
            shoppingLocks.get(threadId).unlock();

            try {
                Thread.sleep(Constants.MILLISECONDS_BETWEEN_SHOP_TIMES);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public boolean makeInventory() {
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

    public void run() {
        quantities = new ArrayList<>();
        bills = new ArrayList<>();
        threads = new ArrayList<>();

        quantities.addAll(initialQuantities);

        threads.addAll(IntStream
                .range(0, numberOfThreads)
                .mapToObj(threadId -> new Thread(() -> shopping(threadId)))
                .collect(Collectors.toList())
        );

        InventoryRunnable inventoryRunnable = new InventoryRunnable(this);
        inventoryThread = new Thread(inventoryRunnable);

        inventoryThread.start();
        threads.forEach(Thread::start);

        for (Thread thread : threads) {
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
