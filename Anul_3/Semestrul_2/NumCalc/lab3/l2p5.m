x = [2 4 6 8];
f = [4 8 20 48];
n = length(x);
m = zeros(n,n);
m(:,1) = f;

for j=2:n
    for i = 1:n-j+1
        m(i,j) = ( m(i+1, j-1) - m(i, j-1) )/ (x(i + j - 1) - x(i));
    end
end


m
