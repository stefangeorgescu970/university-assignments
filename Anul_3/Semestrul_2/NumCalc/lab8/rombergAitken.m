function result = rombergAitken(f, a, b, n, precision)
    mat = zeros(n);
    for i = 1:n
        mat(i,1) = repeatedTrapezium(f, a, b, i);
    end
    
    mat(2,2) = 2 * mat(1,1) - mat(2,1);
    
    i = 2;
    while abs(mat(i,i) - mat(i-1,i-1)) > precision && i < n
        i = i + 1;
        
        for j = 2 : i
            numerator = (4 ^ -j) * mat(i-1,j-1) - mat(i, j-1);
            denominator = (4 ^ -j) - 1;
            mat(i, j) = numerator / denominator;
        end
    end
    if i == n
        fprintf('Precision is not reached for %f\',n);
    end
    
    result = mat(i, i);
end