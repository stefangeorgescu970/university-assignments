axis([0 3 0 5])
[x, y] = ginput(10);

polDegree2 = polyfit(x, y, 2);

points = 0:.01:3;
valueDegree2 = polyval(polDegree2, points);


plot(x, y, '*', points, valueDegree2, 'r');
legend('selected points', 'polynomial of 2nd degree');