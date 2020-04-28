for n = 10:15
    fprintf('Hilbert Cond for N = %d is %f = %f\n',n,cond(hilb(n)), cond(myHilbert(n)));
end
