innerF = @(t) exp(-(t^2));

erf = @(x,n) (2 / sqrt(pi)) * repeatedSimpson(innerF, 0, x, n);

res4 = erf(0.5, 4);
res10 = erf(0.5, 10);

acr4 = abs(0.520499876 - res4)
acr10 = abs(0.520499876 - res10)
