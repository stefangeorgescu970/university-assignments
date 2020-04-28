function x = jacobiIterative(A, b, initialApprox, precision, maxIteration)
    didFind = false;
	n=length(initialApprox);
    previousSolution = initialApprox;
    currentSolution = zeros(1, n);
    for idx = 1:maxIteration
        for currentLine = 1:n
            sum = 0;
            for sumIdx = 1:n
                if sumIdx ~= currentLine 
                    sum = sum + A(currentLine, sumIdx) * previousSolution(sumIdx);
                end
            end
            
            currentSolution(currentLine) = (b(currentLine) - sum) / A(currentLine, currentLine);
            
        end
        
        if norm(currentSolution - previousSolution) < precision
            didFind = true;
            break
        end
        
        previousSolution = currentSolution;
    end
    
    if didFind 
        fprintf('FOUND IACOBI SOLUTION in %d iterations\n', idx);
    else
        fprintf('DID NOT FIND IACOBI SOLUTION\n');
    end
    
    x = currentSolution;
end
