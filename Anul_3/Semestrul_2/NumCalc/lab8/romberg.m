function result = romberg(f, a, b, precision)
    h = b-a;

    previous = h/2 * (f(a) + f(b));             
    current = 1/2 * previous + h/2 * f(a + h/2); 
    
    k = 2;
    while abs(current - previous) > precision
        previous = current;
        
        start = h * 1/2^k;
        step = 2 * h * 1/2^k;
        finish = (1 - 1/2^k) * h;
        x = start : step : finish;
        x = x + a; 
        
        current = 1/2 * previous + (h / 2^k) * sum(f(x));
        
        k = k + 1;
    end
    result = current;
end