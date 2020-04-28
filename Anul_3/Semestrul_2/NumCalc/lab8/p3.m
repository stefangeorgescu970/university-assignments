a = 1;
b = 3;
f = @(x) (100./(x.^2)).*sin(10./x);
precision = 10^-4;
fprintf('Exercise 3: %f\n', integral(f,a,b));
fprintf('Adquad formula: %f\n', adquad(f,a,b,precision));
n1 = 50;
fprintf('Repeated Simpson %d: %f\n',n1,repeatedSimpson(f,a,b,n1));
n2 = 100;
fprintf('Repeated Simpson %d: %f\n',n2,repeatedSimpson(f,a,b,n2));

figure(2)
fplot(f,[1,3]);
title('Exercise 3');
grid on