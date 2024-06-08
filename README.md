# CNF-checker
 to find if a string can be accepted with the given CNF grammar

Chomsky normal form (CNF) :
            a context-free grammar can be converted to CNF with some technic


## Prerequisites
 1. python 3.11 or higher


## How to use
 1. need the grammar to be in a .txt file and have the following rules:
        A. the variables need to be a single letter capital Alphabet like "A" or "B"
        B. the first line should be Variables with a : and then the variables with " ," to separate them
        C. the next line should be Terminals with a : and then the terminals with " ," to separate them
        D. the next line should be Start_Var with a : and then the starting variable
        E. the next line needs to be Rules: (or be empty is doesn’t matter program skip this line)
        F. from now tile the end of the grammar file you should add your transition of grammar the in every line just 1 transition and the format of transition be like:
            S, TK
            K, a
        
        # For better understanding see grammar.txt

 2. run the program and type your string in the string field then click the Butten
