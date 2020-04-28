maxIteration = 100;
maxErr = 10 ^(-4);
func = @(x) (x - 2) ^ 2 - log(x);

x = bisection(func, 1, 2, maxIteration, maxErr)