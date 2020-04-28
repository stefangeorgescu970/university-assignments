package ro.ubbcluj.ppd.lab1.model;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Bill {
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