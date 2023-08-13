#!/usr/bin/env python3
from Crypto.Util.number import *
import libnum
from math import sqrt
from z3 import *

N_a = 11854178668350132536998770600021775412418919136267711466659575504833480429106340292308672916005731985811172925720279068992464220293573546887342858910065901
e_a = 65537
d_a = 2454147980105506786425977989549345389561620074780357800626167210119179432413932079707729534686888191626633148799840568097408265451820012752747703117155329

N_b = 11854178668350132536998770600021775412418919136267711466659575504833480429106340292308672916005731985811172925720279068992464220293573546887342858910065901
e_b = 5
ct_b = 11221865015245352586827949926936479339872912906868036678060873700351121339721754353868819679643501748382626251386036804928304376365191637409698833040968724

assert N_a == N_b
d_b = Int('d_b')
phi = Int('phi')
s = Solver()
s.add(phi > int(pow(N_a, 1/2)))
s.add((d_a * e_a) % phi == 1)
s.add((d_b * e_b) % phi == 1)
print(s.check())
m = s.model()
print(m[phi].as_long())
print(long_to_bytes(pow(ct_b, m[d_b].as_long(), N_a)).decode())