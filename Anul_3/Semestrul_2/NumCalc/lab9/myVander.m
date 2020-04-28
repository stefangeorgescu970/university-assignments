function y = myVander(t)
    n = length(t);
    v = zeros(n);
    v(1,:) = ones(1,n);
    for  i = 2:n
       v(i,:) = v(i-1,:).*t;
    end
    y = v';
end