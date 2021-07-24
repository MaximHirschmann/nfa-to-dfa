# nfa-to-dfa
Gives a table of the tranformation of a nfa (nondeterministic finite automaton) to a dfa (deterministic finite automaton)

For example to represent this nfa:

![alt text](https://github.com/MaximHirschmann/nfa-to-dfa/blob/main/example-nfa.JPG)

Edit the following lines in the .py file

```
alphabet = ["a", "b"]

states = ["q0", "q1", "q2", "q3"]

startingStates = ["q1", "q2"]

endingStates = ["q3"]

transitions = """
    q0, a -> q2
    q1, a -> q0, q2
    q2, a -> q1, q3
    q3, b -> q1, q3
"""
```

and run the file with
```
python main.py
```

Above example prints:
```
                                                       a                                                 b
------------------------------------------------------------------------------------------------------------------------------------------------------
S    {'q1', 'q2'}                                 {'q0', 'q1', 'q2', 'q3'}                          {}                                                s0
F    {'q0', 'q1', 'q2', 'q3'}                     {'q0', 'q1', 'q2', 'q3'}                          {'q1', 'q3'}                                      s1
     {}                                           {}                                                {}                                                s2
F    {'q1', 'q3'}                                 {'q0', 'q2'}                                      {'q1', 'q3'}                                      s3
     {'q0', 'q2'}                                 {'q1', 'q2', 'q3'}                                {}                                                s4
F    {'q1', 'q2', 'q3'}                           {'q0', 'q1', 'q2', 'q3'}                          {'q1', 'q3'}                                      s5
```
