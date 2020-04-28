points = linspace(0,6,13);
f = @(x) exp(sin(x));
pointsValues = arrayfun(f, points);

lambda = @(p) NF(p, points, pointsValues);
interval = 0:0.01:6;
valuesInterval = arrayfun(lambda, interval);

plot(interval, valuesInterval, points, pointsValues, '*')
title('exp (sin x) approximation');