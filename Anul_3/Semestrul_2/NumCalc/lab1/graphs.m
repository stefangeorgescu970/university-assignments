x = 0:0.01:1;
y = exp(10*x.*(x-1)).*sin(12*pi*x);
z = 3 * exp(5 * x .^ 2 - 1) .* cos(12*pi*x);
hold on;
plot(x,y);
plot(x,z);