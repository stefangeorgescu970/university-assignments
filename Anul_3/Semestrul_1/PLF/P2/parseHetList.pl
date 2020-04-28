% parseHetList(L:list, R: list)
% parseHetList(L: input, R: output)


parseHetList([], []).

parseHetList([H | T], R) :- myIsList(H),
    consecSeq(H, RezH),
    parseHetList(T, RezT),
    R = [RezH | RezT].

parseHetList([H | T], R) :- \+ myIsList(H),
    parseHetList(T, RezT),
    R = [H | RezT].
