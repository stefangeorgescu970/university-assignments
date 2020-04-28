function x = falsePos(func, a, b, maxIteration, precision)
    didFind = false;
    
    if func(a) * func(b) < 0
        for idx = 1:maxIteration
            c = (a * func(b) - b * func(a)) / (func(b) - func(a));

            if func(a) * func(c) <= 0
                b = c;
            else
                a = c;
            end

            if abs(func(a))< precision
                didFind = true;
                break
            end
        end

        if didFind 
            fprintf('FOUND FALSE POSITION SOLUTION in %d iterations\n', idx);
        else
            fprintf('DID NOT FIND FALSE POSITION SOLUTION\n');
        end

        x = a;
        
    else
        fprintf('INTERVAL HEADS NOT OK\n');
    end
end
