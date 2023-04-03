import math

steps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def normalize(lst, rang):
    min_val = min(lst)
    max_val = max(lst)
    lst = [2*(x - min_val)/(max_val - min_val) - 1 for x in lst]
    if rang == 5:
        return [x * 5 for x in lst]
    elif rang == 10:
        return [(x + 1) * 5 for x in lst]

def rotate(lst, phase):
    return lst[-phase:] + lst[:-phase]

def amplitudeCalc(x, harm, char, rect, phase):
    fundamental = math.sin((2 * math.pi) * (x + phase) * .0625)
    harmonic1 = (1 / 2) * math.sin(2 * math.pi * 2 * (x + phase) * .0625)
    harmonic2 = (1 / (16 - char)) * math.sin(2 * math.pi * 3 * (x + phase) * .0625)
    harmonic3 = (1 / ((32 - char)) * 2) * math.sin(2 * math.pi * 3 * (x + phase) * .0625)
    rect_offset = abs(math.sin(2 * math.pi * x * .0625)) * rect
    harmonics = (harmonic1 + harmonic2 + harmonic3) * harm
    y = fundamental + harmonics + rect_offset
    return y

def generateSeq(harm, char, rect, phase, shift, rang):
    seq = list(map(lambda a: amplitudeCalc(a, harm, char, rect, phase), steps))
    seq = normalize(seq, rang)
    seq = rotate(seq, shift)
    return seq
