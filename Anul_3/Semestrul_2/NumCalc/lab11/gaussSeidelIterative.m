function x = gaussSeidelIterative(A, b, initialApprox, precision, maxIteration)
    didFind = false;
	n=length(initialApprox);
    previousSolution = initialApprox;
    currentSolution = zeros(1, n);
    for idx = 1:maxIteration
        for currentLine = 1:n
            sum1 = 0;
            for sumIdx = 1:currentLine-1
                sum1 = sum1 + A(currentLine, sumIdx) * currentSolution(sumIdx);
            end
            sum2 = 0;
            for sumIdx = currentLine + 1:n
                sum2 = sum2 + A(currentLine, sumIdx) * previousSolution(sumIdx);
            end
            
            currentSolution(currentLine) = (b(currentLine) - sum1 - sum2) / A(currentLine, currentLine);
            
        end
        
        if norm(currentSolution - previousSolution) < precision
            didFind = true;
            break
        end
        
        previousSolution = currentSolution;
    end
    
    if didFind 
        fprintf('FOUND GAUSS-SEIDEL SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND GAUSS-SEIDEL SOLUTION\n');
    end
    
    x = currentSolution;
end
