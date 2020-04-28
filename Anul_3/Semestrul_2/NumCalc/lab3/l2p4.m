h = 0.25;
i = 0:6;
a = 1 + i.*h;
n = 7;
m = zeros(n,n);
f = @(x) sqrt(5*x.^2 + 1);
m(:,1) = f(a);
for j=2:n
   for i=1:n-j+1
      m(i,j) = m(i+1,j-1) - m(i, j-1); 
   end    
end
m