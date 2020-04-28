axis([-1 5 -1 5])

func = @(x) 2 / (1 + x * x);

trapezium(func, 0, 1)

simpson(func, 0, 1)

A = [0 0];
B = [0 func(0)];
C = [1 func(1)];
D = [1, 0];  


points = -1:.01:2;
values = arrayfun(func, points);


plot([A(1) B(1)], [A(2) B(2)], 'r',[B(1) C(1)], [B(2) C(2)], 'r', [C(1) D(1)], [C(2) D(2)], 'r',[D(1) A(1)], [D(2) A(2)], 'r', points, values);