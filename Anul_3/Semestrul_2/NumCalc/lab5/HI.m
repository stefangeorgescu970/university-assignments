function val = HI(point, x, f, fDer) 
    
    n = length(x);
    doubleX = zeros(1, 2 * n);
    doubleF = zeros(1, 2 * n);
    doubleFDer = zeros(1, 2 * n);
    
    for i=1:n
        doubleX(2 * i - 1) = x(i);
        doubleX(2 * i) = x(i);
        
        doubleF(2 * i - 1) = f(i);
        doubleF(2 * i) = f(i);
        
        doubleFDer(2 * i - 1) = fDer(i);
        doubleFDer(2 * i) = fDer(i);
    end
    
    n = length(doubleX);
     
    m = zeros(n,n);
    m(:,1) = doubleF;

    for j=2:n
        for i = 1:n-j+1
       
            if mod(i,2) == 1 && j == 2 
                m(i,j) = doubleFDer(i);
            else
                m(i,j) = ( m(i+1, j-1) - m(i, j-1) )/ (doubleX(i + j - 1) - doubleX(i));
            end
            
            
        end
    end

    sum = doubleF(1);

    for i = 1:n - 1

        prod = 1;

        for j = 1:i
            prod = prod * (point - doubleX(j));
        end

        prod = prod * m(1,i + 1);

        sum = sum + prod;
    end
    
    val = sum;

end

