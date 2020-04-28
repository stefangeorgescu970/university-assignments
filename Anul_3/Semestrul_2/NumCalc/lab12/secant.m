function x = secant(func, x0, x1, maxIteration, precision)
    didFind = false;
    xkmin1 = x0;
    xk = x1;
    xkplus1 = 0;
    for idx = 1:maxIteration
        
        xkplus1 = xk - (((xk - xkmin1) * func(xk)) / (func(xk) - func(xkmin1)));

        if abs(xkplus1 - xk) < precision
            didFind = true;
            break
        end
        
        xkmin1 = xk;
        xk = xkplus1;
    end
    
    if didFind 
        fprintf('FOUND SECANT SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND SECANT SOLUTION\n');
    end
    
    x = xkplus1;
end
