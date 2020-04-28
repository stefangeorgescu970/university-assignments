function [] = facto()
fact=1;
n=1;
while n<20    
    n=n+1;
    fact=fact*n;
    my_fact=3/fact;
    disp(n-1)
    disp(my_fact)
end
end