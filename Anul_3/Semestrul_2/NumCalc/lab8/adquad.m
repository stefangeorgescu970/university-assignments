function result = adquad(f, a, b, precision)
    i1 = simpsonInt(f,a,b);
    i2 = simpsonInt(f,a,(a+b)/2) + simpsonInt(f,(a+b)/2,b);
    previous = i1;
    result = i2;
    while abs(previous - result)>=15*precision
        previous = result;
        result = adquad(f,a,(a+b)/2,precision/2) + adquad(f, (a+b)/2, b, precision/2);
    end
end