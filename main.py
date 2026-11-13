import workjob
from random import randint as rng
while True:
    match rng(0,9):
        case 0:
            prf=workjob.mathwork()
        case 1:
            prf=workjob.wordwork()
        case 2:
            prf=workjob.sequencework()
        case 3:
            prf=workjob.estimationwork()
        case 4:
            prf=workjob.attentionwork()
        case 5:
            prf=workjob.percentwork()
        case 6:
            prf=workjob.letterwork()
        case 7:
            prf=workjob.letterwork()
        case 8:
            prf=workjob.hexwork()
        case 9:
            prf=workjob.binarywork()
    if prf:
        print("Great Job!")
    else:
        print("FIRED!")