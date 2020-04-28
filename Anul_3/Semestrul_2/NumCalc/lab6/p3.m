temp = [0 10 20 30 40 60 80 100];
press = [0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];

polDegree2 = polyfit(temp, press, 2);
polDegree4 = polyfit(temp, press, 4);

point = 45;
value = 0.095848;

valueDegree2 = polyval(polDegree2, point);
valueDegree4 = polyval(polDegree4, point);

errorDegree2 = abs(value - valueDegree2)
errorDegree4 = abs(value - valueDegree4)


lambda = @(point) LMF(point, temp, press);


points = 0:.01:100;
poly1 = polyval(polDegree2, points);
poly2 = polyval(polDegree4, points);
poliLag = arrayfun(lambda, points);

plot(points, poly1, 'r', points, poly2, 'g', points, poliLag, 'b', temp, press, '*');
legend('degree 2', 'degree 4', 'lagrange', 'nodes');






