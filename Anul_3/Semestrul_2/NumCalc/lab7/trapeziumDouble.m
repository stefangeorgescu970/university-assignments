function rez = trapeziumDouble(f, a, b, c, d)

    t1 = (b - a) * (d - c) / 16;
    t2 = f(a, c) + f(a, d) + f(b, c) + f(b, d);
    t2 = t2 + 2 * (f((a + b) / 2, c) + f((a + b) / 2, d) + f(a, (c + d) / 2) + f(b, (c + d) / 2));
    t2 = t2 + 4 * f((a + b) / 2, (c + d) / 2);
    
    rez = t1 * t2;
end