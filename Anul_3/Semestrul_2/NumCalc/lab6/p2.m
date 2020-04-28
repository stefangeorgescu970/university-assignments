x = 1:7;
fx = [13 15 20 14 15 13 10];
xsq = x .* x;

m = length(x) - 1;

a = ((m + 1) * sum(x .* fx) - sum(x) * sum(fx)) / ( (m + 1) * sum(xsq) - sum(x) * sum(x));

b = (sum(xsq) * sum(fx) - sum(x .* fx) * sum(x)) / ( (m + 1) * sum(xsq) - sum(x) * sum(x));

func = @(x) a * x + b;


point = 8;
valueAprpox = func(point);

points = 1:.01:7;
values = arrayfun(func, points);
plot(x, fx, '*', points, values);

fxapprx = arrayfun(func, x);
diffs = fx - fxapprx;
diffsSqr = diffs .* diffs;
eab = sqrt(sum(diffsSqr))
