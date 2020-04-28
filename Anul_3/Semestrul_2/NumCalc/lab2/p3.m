t = 1;
s = 1;
n = 6;
x0 = 0;
x = -1:0.01:3;
p = 1;
plot(x,t)
hold on
for i=1:n
   k = p * i;
   s = t + (x-x0).^i/k ;
   plot(x, s)
   hold on
   t = s;
   p = k;
end    
hold off