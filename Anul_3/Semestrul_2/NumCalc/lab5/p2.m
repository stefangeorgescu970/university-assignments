x = [1 2];
f = [0 0.6931];
fder = [1 0.5];

lnAprox = HI(1.5, x, f, fder);

error = abs(log(1.5) - lnAprox);

error