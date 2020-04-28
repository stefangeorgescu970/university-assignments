innerFunc = @(x,p,r) sqrt(1 - (p / r) * (p / r) * sin(x));

p = 75;
r = 110;

lambda = @(x) innerFunc(x, p, r);

fullFunc = @(p,r) 60 * r * repeatedTrapezium(lambda, 0, 2*pi, 10) / (r * r - p * p);

fullFunc(p,r)

