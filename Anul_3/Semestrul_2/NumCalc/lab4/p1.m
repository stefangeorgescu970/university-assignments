x = [1 1.5 2 3 4];
f = [0 0.17609 0.30103 0.47712 0.60206];

maxError = 0;

for i=10:35
    currentError = abs(log(i/10) - NF(i/10, x, f));
    if currentError > maxError 
        maxError = currentError;
    end
end

maxError