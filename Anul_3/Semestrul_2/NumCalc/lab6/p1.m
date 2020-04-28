nodes = [0 pi/2 pi 3*pi/2 2*pi];
nodeValues = sin(nodes);

value = pi / 4;
functionValue = sin(value)
splineValue = spline(nodes, nodeValues, value)
clampedSplineValue = spline(nodes, [1 nodeValues 1], value)


points = 0:.01:2*pi;
splinePoints = spline(nodes, nodeValues, points);


clampedSplinePoints = spline(nodes, [1 nodeValues 1], points);
plot(points, splinePoints, 'g', points, clampedSplinePoints, 'r', points, sin(points), 'b', nodes, nodeValues, '*');
legend('spline', 'clampedSpline', 'function', 'nodes');