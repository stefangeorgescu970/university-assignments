function rez = repeatedSimpson(func, a, b, n)

    t1 = (b - a) / (6 * n);
    h = (b - a) / n;
    k = 0:n;
    maxlen = length(k);
    x = (k .* h) + a;
    
    part1 = x(1:maxlen-1);
    part2 = x(2:maxlen);
    
    xMean = (part1 + part2) / 2;
    
    f1 = arrayfun(func, xMean);
    s1 = sum(f1);
    
    f2 = arrayfun(func, x(2:n-1));
    s2 = sum(f2);

    t2 = func(a) + func(b) + 4 * s1 + 2 * s2;
   
    rez = t1 * t2;
end