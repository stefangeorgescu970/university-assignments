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