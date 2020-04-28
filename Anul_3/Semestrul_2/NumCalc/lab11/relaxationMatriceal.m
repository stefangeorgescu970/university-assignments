function x = relaxationMatriceal(A, b, initialApprox, precision, maxIteration, omega)
    n = length(initialApprox);

    D = diag(diag(A));
    L = tril(A, -1);
    U = triu(A, 1);
    
    didFind = false;

    previousSolution = initialApprox;
    currentSolution = zeros(1, n);
    
    for idx = 1:maxIteration 
        currentSolution = (inv(D + omega * L) * (((1 - omega)*D - omega * U) * previousSolution' + omega * b))';
       
        if norm(currentSolution - previousSolution) < precision
            didFind = true;
            break
        end
        
        previousSolution = currentSolution;
    end
    
    if didFind 
        fprintf('FOUND RELAXATION MATRICEAL SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND RELAXATION MATRICEAL SOLUTION\n');
    end
    
    x = currentSolution;
end
