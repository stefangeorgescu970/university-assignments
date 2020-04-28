function val = NF(point, x, f) 

    n = length(x);
    m = zeros(n,n);
    m(:,1) = f;

    for j=2:n
        for i = 1:n-j+1
            m(i,j) = ( m(i+1, j-1) - m(i, j-1) )/ (x(i + j - 1) - x(i));
        end
    end

    sum = f(1);

    for i = 1:n - 1

        prod = 1;

        for j = 1:i
            prod = prod * (point - x(j));
        end

        prod = prod * m(1,i + 1);

        sum = sum + prod;
    end
    
    val = sum;

end

