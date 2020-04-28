findAll(L, R) :-
    findall(RO, findOne(L, RO), RI),
    sort(RI, R).
