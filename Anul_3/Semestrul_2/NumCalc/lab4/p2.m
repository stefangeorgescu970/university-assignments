x = [1 2 3 4 5];
f = [22 23 25 30 28];

resA = NF(2.5, x, f)

lambda = @(p) NF(p, x, f);
points = 1:0.01:5;
values = arrayfun(lambda, points);

plot(points, values, x, f, '*');
title('my nice plot');