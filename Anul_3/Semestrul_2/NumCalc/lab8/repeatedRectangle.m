function result = repeatedRectangle(f, a, b, n)
    points = linspace(a,b,n);
    result = (b-a)/n*sum(f(points(1:n)));
end