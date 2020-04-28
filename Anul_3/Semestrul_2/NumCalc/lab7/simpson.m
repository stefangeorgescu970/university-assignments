function rez = simpson(func, a, b)
    rez = ((b - a) / 6) * (func(a) + func(b) + 4 * func((a + b) / 2));
end