A = [10 7 8 7;
    7 5 6 5;
    8 6 10 9;
    7 5 9 10];
B = [32 23 33 31]';

X = A\B
fprintf('Conditional number is %f\n', cond(A));

B2 = [32.1 22.9 33.1 30.9]';
X2 = A\B2

relativeError = norm(B-B2)./norm(B);
outputRelativeError = norm(X-X2)./norm(X);
totalError = outputRelativeError./relativeError;
fprintf('Relative error is %f\n',relativeError);
fprintf('Output Relative error is %f\n',outputRelativeError);
fprintf('Total error is %f\n',totalError);

A2 = [  10 7 8.1 7.2;
        7.08 5.04 6 5;
        8 5.98 9.89 9;
        6.99 4.99 9 9.98];
X3 = A2\B

relativeError2 = norm(A-A2)/norm(A);
outputRelativeError2 = norm(X-X3)/norm(X);
totalError2 = outputRelativeError2./relativeError2;
fprintf('Relative error is %f\n',relativeError2);
fprintf('Output Relative error is %f\n',outputRelativeError2);
fprintf('Total error is %f\n',totalError2);