a = 0;
b = 1;
epsilon = 10^-4;
f = @(x) 2./(1 + x.^2);
fprintf('Exercise 2: %f\n',integral(f,a,b)); 
fprintf('Romberg formula 2: %f\n',romberg(f,a,b, epsilon));
n = 150;
fprintf('Romberg formula 5: %f\n',rombergAitken(f,a,b,n, epsilon)); 