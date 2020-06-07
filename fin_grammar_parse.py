from lark import Lark
import fin_strings, propp_strings

## creating terminal rules makes for prettier trees
## TODO: lark doesn't like infinite recursion
grammar = Lark(r"""
tale : pi x | x
pi : ALPHA? BETA (GAMMA delta)? (epsilon ZETA)? (ETA THETA)?
delta : (D E? F?) | (D? E F?) | (D? E? F)
epsilon: M N
phi : (H I?) | (H? I)
x : move | move x
move : delta? A B? C? UP? delta? G? phi J? K? DOWN? PR? RS? O? L? epsilon? Q? Ex? T? U? W?


A: "A"
B: "B"
D: "D"
C: "C"
E: "E"
F: "F"
G: "G"
H: "H"
I: "I"
J: "J"
K: "K"
L: "L"
M: "M"
N: "N"
PR: "Pr"
RS: "Rs"
Q: "Q"
UP: "up"
DOWN: "down"
EX: "Ex"
T: "T"
U: "U"
W: "W"
O: "O"
ALPHA: "alpha"
BETA: "beta"
GAMMA: "gamma"
ZETA: "zeta"
ETA: "eta"
THETA: "theta"

""", start='tale', parser='earley')
d = fin_strings.prepless_dict
p = propp_strings.dict
for key in d:
    d_val = d[key].replace(" ","")
    p_val = p[key].replace(" ","")
    print(key + ", Fin: " + d_val +
          "\n   Propp: " + p_val)
    try:
        print(grammar.parse(d_val).pretty())
    except:
        print("Fin's string not accepted.")
        
    try:
        print(grammar.parse(p_val).pretty())
    except:
        print("Propp's string not accepted.\n")
