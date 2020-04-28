n = 4;
x = -1:0.01:1;
T0 = 1;
T1 = x;
plot(x,T0)
hold on
plot(x,T1)
for i=1:n
    T2 = 2.*x.*T1 - T0;
    plot(x, T2)    
    T0 = T1;
    T1 = T2;
end
hold off