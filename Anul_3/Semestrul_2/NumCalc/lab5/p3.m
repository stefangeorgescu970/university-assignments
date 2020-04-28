points = linspace(-5,5,15);
f = @(x) sin(2 * x);
fder = @(x) 2 * cos (2 * x);

pointsValues = arrayfun(f, points);
pointsDerValues = arrayfun(fder, points);

lambda = @(p) HI(p, points, pointsValues, pointsDerValues);
interval = -5:0.01:5;
valuesInterval = arrayfun(lambda, interval);

plot(interval, valuesInterval, points, pointsValues, '*')

pause
plot(interval, arrayfun(f, interval));



title('(sin 2 * x) approximation');