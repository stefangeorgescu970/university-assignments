function x = newton(func, funcDer, initialApprox, maxIteration, precision)
    didFind = false;
    previousSolution = initialApprox;
    currentSolution = 0;
    for idx = 1:maxIteration
        
        currentSolution = previousSolution - func(previousSolution) / funcDer(previousSolution);

        if abs(previousSolution - currentSolution) < precision
            didFind = true;
            break
        end
        
        previousSolution = currentSolution;
    end
    
    if didFind 
        fprintf('FOUND NEWTON SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND NEWTON SOLUTION\n');
    end
    
    x = currentSolution;
end
