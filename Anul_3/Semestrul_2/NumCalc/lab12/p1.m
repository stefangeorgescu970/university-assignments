firstX = pi/4;
maxIteration = 100;
maxErr = 10 ^(-4);
func = @(x) cos(x) - x;
funcDer = @(x) -sin(x) - 1;

x = newton(func, funcDer, firstX, maxIteration, maxErr)