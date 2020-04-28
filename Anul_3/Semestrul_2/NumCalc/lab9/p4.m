for n = 10:15
    k = 1:n;
    t1 = 1./k;
    fprintf('Vander 1 Cond for N = %d is %f = %f\n',n, cond(vander(t1)), cond(myVander(t1)));
end

for n = 10:15
   k = 1:n;
   t2 = -1 + ((2./n).*k);
   fprintf('Vander 2 Cond for N = %d is %f = %f\n',n, cond(vander(t2)), cond(myVander(t2)));
end