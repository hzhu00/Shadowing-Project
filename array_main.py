from make_tp_array import *
from make_ta_array import *

impath = "C:\\Users\\haoze\\Desktop\\Images for experiment\\"
array = input("TP or TA?\n").upper()

if array == "TP":
    foilnum = int(input("How many foils? (5/10/15)\n"))
    arraynum = int(input("How many arrays for this foil number?\n"))
    for target in range(1, 5):
        tp = TParray(foilnum, arraynum, target, impath)
        tp.repeat_compose()
elif array == "TA":
    foilnum = int(input("How many foils? (6/11/16)\n"))
    arraynum = int(input("How many arrays for this foil number?\n"))
    ta = TAarray(foilnum, arraynum, impath)
    ta.repeat_compose()