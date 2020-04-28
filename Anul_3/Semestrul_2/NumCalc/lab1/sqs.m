function s = sqs(x)
s=1;
u=1;
n=1;
while s+u~=s
    s=s+u;
    n=n+1;
    u=u*x/(n+1);
end
disp(n)
end