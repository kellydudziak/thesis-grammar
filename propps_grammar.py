from lark import Lark
import datetime as dt
import fin_strings, propp_strings

## creating terminal rules makes for prettier trees
## TODO: lark doesn't like infinite recursion
print(dt.datetime.now())
grammar = Lark(r"""
start: a | up | d | ef
a: "A" (a | b | c | up | ef)
b: "B" (c | up)
c: "C" (b | up | ef)
up: "up" (t | hi | d | ef | g)
d: "D" (d | ef)
ef: "EF" (ef | a | up | d | g | k | t | down | pr | rs | w)
g: "G" (ef | a | w | k)
hi: "HI" (hi | k | down | w)
k: "K" (k | t | down | w)
t: "T" (g | pr)
down: "down" (hi | ef | pr | w)?
pr: "Pr" (down | rs)
rs: "Rs" (rs | pr | ef | down | w)?
w: "W" down?

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

""", start='start')
print(dt.datetime.now())

d = fin_strings.prepless_dict
p = propp_strings.dict
for key in d:
    d_val = d[key].replace(" ","")
    p_val = p[key].replace(" ","")
    print(key + ", Fin: " + d_val +
          "\n   Propp: " + p_val)
    try:
        print("Finlayson: \n" + grammar.parse(d_val).pretty())
    except:
        print("Finlayson's not accepted.")
        
    try:
        print("Propp: \n" +grammar.parse(p_val).pretty())
    except:
        print("Propp's not accepted.\n")
