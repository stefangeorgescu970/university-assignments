A1 = [400 -201; -800 401];
B1 = [200 -200]';
X1 = A1\B1

A2 = [401 -201; -800 401];
B2 = B1;
X2 = A2\B2

fprintf('Conditioning number is %f\n', cond(A1));