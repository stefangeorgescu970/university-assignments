function x = bisection(func, a, b, maxIteration, precision)
    didFind = false;
    
    if func(a) * func(b) <= 0
        for idx = 1:maxIteration

            c = (a + b) / 2;

            if func(a) * func(c) <= 0
                b = c;
            else
                a = c;
            end

            if abs(a - b) / abs(a) < precision
                didFind = true;
                break
            end
        end

        if didFind 
            fprintf('FOUND BISECTION SOLUTION in %d iterations\n', idx);
        else
            fprintf('DID NOT FIND BISECTION SOLUTION\n');
        end

        x = (a + b) / 2;
        
    else
        fprintf('INTERVAL HEADS NOT OK\n');
    end
end
