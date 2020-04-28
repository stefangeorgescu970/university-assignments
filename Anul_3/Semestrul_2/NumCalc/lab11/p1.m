v = [3 3 3 3 3 3];
x = [-1 -1 -1 -1 -1 ];

A = diag(v, 0) + diag(x, 1) + diag(x , -1);

b = [2 1 1 1 1 2]';
initialSolution = [0 0 0 0 0 0];
precision = 10^-3;

% x = jacobiIterative(A, b, initialSolution, precision, 40)

% x = gaussSeidelIterative(A, b, initialSolution, precision, 40)

x = relaxationIterative(A, b, initialSolution, precision, 40, 1.1)