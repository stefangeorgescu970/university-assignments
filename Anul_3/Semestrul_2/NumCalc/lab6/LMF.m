function res = LMF(point, x, f)
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