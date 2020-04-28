function [] = erroare_eps()
n=1;
while n<25   
    disp(n)
    numar = power((pi/4),2*n+1);
    numi = factorial(2*n+3);
    disp(numar/numi);
    n=n+1;
end
end