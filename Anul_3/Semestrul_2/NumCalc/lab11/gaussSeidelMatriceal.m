function x = gaussSeidelMatriceal(A, b, initialApprox, precision, maxIteration)
    n = length(initialApprox);

    D = diag(diag(A));
    L = tril(A, -1);
    U = triu(A, 1);
    
    didFind = false;

    previousSolution = initialApprox;
    currentSolution = zeros(1, n);
    
    for idx = 1:maxIteration 
        currentSolution = (inv(D + L) * (- U * previousSolution' + b))';
       
        if norm(currentSolution - previousSolution) < precision
            didFind = true;
            break
        end
        
        previousSolution = currentSolution;
    end
    
    if didFind 
        fprintf('FOUND GAUSS-SEIDEL MATRICEAL SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND GAUSS-SEIDEL MATRICEAL SOLUTION\n');
    end
    
    x = currentSolution;
end
