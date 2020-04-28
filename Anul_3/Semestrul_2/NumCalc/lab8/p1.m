a = 1;
b = 1.5;
f = @(x) exp(-x.^2);

fprintf('Real integral: %f\n', integral(f, a, b));
fprintf('Rectangle formula: %f\n', rectangleInt(f, a, b));

points = linspace(1,1.5,100);

figure(1)
plot(points, f(points));
title('Rectangle formula');
hold on
plot([a,a,b,b,a],[0,f((a+b)/2),f((a+b)/2),0,0]);
hold off
grid on

n1 = 150;
fprintf('Repeated Rectangle for %d: %f\n',n1, repeatedRectangle(f,a,b,n1));
n2 = 500;
fprintf('Repeated Rectangle for %d: %f\n',n2, repeatedRectangle(f,a,b,n2));