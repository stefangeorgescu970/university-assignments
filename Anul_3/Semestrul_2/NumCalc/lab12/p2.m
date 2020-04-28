x0 = 1;
x1 = 2;
maxIteration = 100;
maxErr = 10 ^(-4);
func = @(x) x^3 - x^2 - 1;

x = secant(func, x0, x1, maxIteration, maxErr)

x = falsePos(func, 1, 2, maxIteration, maxErr)