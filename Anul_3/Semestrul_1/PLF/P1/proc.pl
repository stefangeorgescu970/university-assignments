proc([],1).
proc([H|T],R):-mod(H,2)=:=0,
    proc(T, RT),
    R is RT*H.

proc([H|T],R):-mod(H,2)=\=0,
    proc(T, RT),
    R is RT.

