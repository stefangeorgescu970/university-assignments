function z = graphs4(x)
    z = []; 
    for elem = x
        if mod(elem,2)==0
            z = [z elem/2];
        else
            z = [z 3*elem+1];
        end 
    end
end