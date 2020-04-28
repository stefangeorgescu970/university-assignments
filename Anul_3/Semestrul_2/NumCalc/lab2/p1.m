x = linspace(0,1,100);

l1 = [1 0] ;
y1 = polyval(l1, x);
l2 = [3/2 0 -1/2];
y2 = polyval(l2, x);
l3 = [5/2 0 -3/2 0];
y3 = polyval(l3, x);
l4 = [35/8 0 -15/4 3/8];
y4 = polyval(l4, x);

subplot(2, 2, 1)
plot(x, y1)
subplot(2, 2, 2)
plot(x, y2)
subplot(2, 2, 3)
plot(x, y3)
subplot(2, 2, 4)
plot(x, y4)