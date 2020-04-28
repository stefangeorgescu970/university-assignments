function res = weirdFunc(x)
    temp = 1 + 1/2;
    
    for step = 0:x-1
       temp = 1 + 1 / temp; 
    end
    
    res = temp;
end