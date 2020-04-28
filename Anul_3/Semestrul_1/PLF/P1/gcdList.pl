% gcdList(L: list, R: integer)
% gcdList(i,o)
% Find the Greatest Common Divisor of the elements of a list.
gcdList([], 0).
gcdList([H | T], R) :- gcdList(T, RT), gcd(H, RT, REZ), R is REZ.
