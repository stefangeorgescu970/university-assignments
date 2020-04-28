% gcd(e1: integer, e2: integer, r: integer)
% gcd(i,i,o)
% Find the greatest common divisor of two elements.

gcd(0,0,0).
gcd(E1, 0, E1).
gcd(0, E2, E2).
gcd(E1, E2, R):- E1 > E2, E3 is E1 - E2, gcd(E3, E2, R).
gcd(E1, E2, R):- E2 > E1, E3 is E2 - E1, gcd(E1, E3, R).
gcd(E1, E2, R):- E1 =:= E2, R is E1.
