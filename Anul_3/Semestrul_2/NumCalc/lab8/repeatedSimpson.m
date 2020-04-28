function y = repeatedSimpson(f,a,b,n)
    points = linspace(a,b,n);
    sum2 = sum(f(points(2:n-1)));
    sum1 = sum((f(points(1:n-1)) + f(points(2:n)))./2);
    y = ((b-a)/(6*n))*(f(a)+f(b)+ 4 * sum1 + 2 * sum2);
end