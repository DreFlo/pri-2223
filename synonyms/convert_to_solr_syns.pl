:- discontiguous(s/6).
:- discontiguous(s/4).

:- consult(wn_s).

:- initialization(main).

visit(_, KeyWord) :-
    write(synonyms, KeyWord),
    fail.
visit(SynSetCode, KeyWord) :-
    s(SynSetCode, _, Word, _, _, _),
    dif(Word, KeyWord),
    write(synonyms, ','), write(synonyms, Word),
    fail.
visit(_, _) :-
    write(synonyms, '\n').


visit_list([]).
visit_list([SynSetCode|Rest]) :-
    s(SynSetCode, _, KeyWord, _, _, _),
    visit(SynSetCode, KeyWord),
    visit_list(Rest).

main :-
    setof(SynSetCode, (A,B,C,D,E)^s(SynSetCode, A, B, C, D, E), Set),
    open('synonyms.txt', write, _, [alias(synonyms), encoding(utf8), close_on_abort(true)]),
    visit_list(Set),
    close(synonyms),
    halt.
    