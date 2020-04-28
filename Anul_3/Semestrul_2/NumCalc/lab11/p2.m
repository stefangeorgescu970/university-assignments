A = [3 1 1; -2 4 0; -1 2 -6];
b = [12 2 -5]';

initialSolution = [0 0 0];
precision = 10^-5;

% x = jacobiMatriceal(A, b, initialSolution, precision, 40)
% x = gaussSeidelMatriceal(A, b, initialSolution, precision, 40)
x = relaxationMatriceal(A, b, initialSolution, precision, 40, 1.1)
