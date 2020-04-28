% isPerfSquare( NUMBER: int, CURRENT: in)
% isPerfSquare(i,i).
% isPerfSquare(Number, Current) =
% true, if number == current * current
% false, if numeber < current * current
% isPerfSquare(Number, Current + 1), number > current * current


isPerfSquare(NUMBER, CURRENT) :- NUMBER > CURRENT*CURRENT,
    NEWCURRENT is CURRENT + 1,
    isPerfSquare(NUMBER, NEWCURRENT).
isPerfSquare(NUMBER, CURRENT) :- NUMBER =:= CURRENT*CURRENT.
