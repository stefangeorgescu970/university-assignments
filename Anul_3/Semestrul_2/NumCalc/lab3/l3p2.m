x = [81 100 121];
f = [9 10 11];
m = length(x);
point = 115;

Lmf(point, x, f)


function res = miu(i, x)
    prod = 1;
    m = length(x);
    current = x(i);
    for idx = 1:m
        if idx ~= i
            prod = prod * (current - x(idx));
        end
    end
    res = prod;
end

function res = A(i, x)
    res = 1 / miu(i, x);
end

function res = Lmf(point, x, f)
    m = length(x);
    numi = 0;
    numr = 0;
    
    for idx = 1:m
        numi = numi + (A(idx, x) * f(idx) / (point - x(idx)));
    end
    
    for idx = 1:m
        numr = numr + (A(idx, x) / (point - x(idx)));
    end
    
    res = numi / numr;
end