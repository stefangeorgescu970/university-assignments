eps = 10 ^ -3;
point = 115;

x = [64 81 100 144 169 121];
f = [8 9 10 12 13 11];

n = length(x);


[rez, idx] = sort(abs(x - point));
x = x(idx);
f = f(idx);

% for i = 1:n-1
%     for j = i+1:n
%         if abs(x(i) - point) > abs(x(j) - point)  
%            x([i,j]) = x([j,i]);
%            f([i,j]) = f([j,i]);
%         end
%     end
% end

m = zeros(n,n);
m(:,1) = f;

for i = 2:n

    for j = 1:i-1
        m(i,j+1) = 1 / (x(i) - x(j)) * ( m(j,j) * (x(i) - point) - (m(i,j) * (x(j) - point)));
    end
    
    if abs(m(i,i) - m(i-1,i-1)) < eps 
       m(i,i)
       break
    end
    
end

m
