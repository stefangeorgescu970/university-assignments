t = -1:0.01:1;
T1 = @(t) cos(acos(t));
T2 = @(t) cos(2*acos(t));
T3 = @(t) cos(3*acos(t));

fplot(T1,[-1,1])
hold on
fplot(T2,[-1,1])
fplot(T3,[-1,1])
hold off
