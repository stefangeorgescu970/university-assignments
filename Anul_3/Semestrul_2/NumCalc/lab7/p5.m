func = @(x) 1 / (4 + sin(20 * x));

repeatedSimpson(func, 0, pi, 30)