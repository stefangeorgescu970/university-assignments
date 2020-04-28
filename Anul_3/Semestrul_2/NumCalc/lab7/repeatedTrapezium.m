function rez = repeatedTrapezium(func, a, b, n)

    t1 = (b - a) / (2 * n);
    h = (b - a) / n;
    k = 1:n-1;
    x = (k .* h) + a;
    f = arrayfun(func, x);
    
    
    t2 = func(a) + func(b) + 2 * sum(f);
   
    rez = t1 * t2;
end