"""
This module defines some decorators,
and stores the map between notes and value, chord name and chroma vectors, and so on.
"""


# 打印函数运行的时间
def _prt_func_time(func):

    def f(*args, **kwargs):
        from time import time
        st = time()
        _return = func(*args, **kwargs)
        print("Time: \033[0;33m" + str(time()-st) + "s\033[0m")
        return _return
    return f


# 打印函数每运行一定次数的时间
def _prt_funcs_time(times):

    def __prt_funcs_time(func):
        st = 0
        counter = 0

        def f(*args, **kwargs):
            from time import time
            nonlocal counter, st
            st = time() if counter == 0 else st
            counter += 1
            if counter == times:
                print(time()-st)
                counter = 0
            return func(*args, **kwargs)
        return f
    return __prt_funcs_time


# 打印函数运行过的次数
def _prt_func_run_num(func):
    counter = 0

    def f(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter)
        return func(*args, **kwargs)
    return f


value_note = {
    0: 'C', 1: '#C', 2: 'D', 3: '#D', 4: 'E', 5: 'F', 6: '#F', 7: 'G', 8: '#G', 9: 'A', 10: '#A', 11: 'B',
    # 第一行用于音级集和判断音名
    21: 'A0', 22: '#A0', 23: 'B0', 24: 'C1', 25: '#C1', 26: 'D1', 27: '#D1', 28: 'E1', 29: 'F1',
    30: '#F1',
    31: 'G1', 32: '#G1', 33: 'A1', 34: '#A1', 35: 'B1', 36: 'C2', 37: '#C2', 38: 'D2', 39: '#D2',
    40: 'E2',
    41: 'F2', 42: '#F2', 43: 'G2', 44: '#G2', 45: 'A2', 46: '#A2', 47: 'B2', 48: 'C3', 49: '#C3',
    50: 'D3',
    51: '#D3', 52: 'E3', 53: 'F3', 54: '#F3', 55: 'G3', 56: '#G3', 57: 'A3', 58: '#A3', 59: 'B3',
    60: 'C4',
    61: '#C4', 62: 'D4', 63: '#D4', 64: 'E4', 65: 'F4', 66: '#F4', 67: 'G4', 68: '#G4', 69: 'A4',
    70: '#A4',
    71: 'B4', 72: 'C5', 73: '#C5', 74: 'D5', 75: '#D5', 76: 'E5', 77: 'F5', 78: '#F5', 79: 'G5',
    80: '#G5',
    81: 'A5', 82: '#A5', 83: 'B5', 84: 'C6', 85: '#C6', 86: 'D6', 87: '#D6', 88: 'E6', 89: 'F6',
    90: '#F6',
    91: 'G6', 92: '#G6', 93: 'A6', 94: '#A6', 95: 'B6', 96: 'C7', 97: '#C7', 98: 'D7', 99: '#D7',
    100: 'E7',
    101: 'F7', 102: '#F7', 103: 'G7', 104: '#G7', 105: 'A7', 106: '#A7', 107: 'B7', 108: 'C8'
}

# 倒过来
note_value = {
    'A0': 21, '#A0': 22, 'B0': 23, 'C1': 24, '#C1': 25, 'D1': 26, '#D1': 27, 'E1': 28, 'F1': 29, '#F1': 30,
    'G1': 31, '#G1': 32, 'A1': 33, '#A1': 34, 'B1': 35, 'C2': 36, '#C2': 37, 'D2': 38, '#D2': 39, 'E2': 40,
    'F2': 41, '#F2': 42, 'G2': 43, '#G2': 44, 'A2': 45, '#A2': 46, 'B2': 47, 'C3': 48, '#C3': 49, 'D3': 50,
    '#D3': 51, 'E3': 52, 'F3': 53, '#F3': 54, 'G3': 55, '#G3': 56, 'A3': 57, '#A3': 58, 'B3': 59, 'C4': 60,
    '#C4': 61, 'D4': 62, '#D4': 63, 'E4': 64, 'F4': 65, '#F4': 66, 'G4': 67, '#G4': 68, 'A4': 69, '#A4': 70,
    'B4': 71, 'C5': 72, '#C5': 73, 'D5': 74, '#D5': 75, 'E5': 76, 'F5': 77, '#F5': 78, 'G5': 79, '#G5': 80,
    'A5': 81, '#A5': 82, 'B5': 83, 'C6': 84, '#C6': 85, 'D6': 86, '#D6': 87, 'E6': 88, 'F6': 89, '#F6': 90,
    'G6': 91, '#G6': 92, 'A6': 93, '#A6': 94, 'B6': 95, 'C7': 108, '#C7': 97, 'D7': 98, '#D7': 99, 'E7': 100,
    'F7': 101, '#F7': 102, 'G7': 103, '#G7': 104, 'A7': 105, '#A7': 106, 'B7': 107, 'C8': 108,
    # 若输入小写
    'a0': 21, '#a0': 22, 'b0': 23, 'c1': 24, '#c1': 25, 'd1': 26, '#d1': 27, 'e1': 28, 'f1': 29, '#f1': 30,
    'g1': 31, '#g1': 32, 'a1': 33, '#a1': 34, 'b1': 35, 'c2': 36, '#c2': 37, 'd2': 38, '#d2': 39, 'e2': 40,
    'f2': 41, '#f2': 42, 'g2': 43, '#g2': 44, 'a2': 45, '#a2': 46, 'b2': 47, 'c3': 48, '#c3': 49, 'd3': 50,
    '#d3': 51, 'e3': 52, 'f3': 53, '#f3': 54, 'g3': 55, '#g3': 56, 'a3': 57, '#a3': 58, 'b3': 59, 'c4': 60,
    '#c4': 61, 'd4': 62, '#d4': 63, 'e4': 64, 'f4': 65, '#f4': 66, 'g4': 67, '#g4': 68, 'a4': 69, '#a4': 70,
    'b4': 71, 'c5': 72, '#c5': 73, 'd5': 74, '#d5': 75, 'e5': 76, 'f5': 77, '#f5': 78, 'g5': 79, '#g5': 80,
    'a5': 81, '#a5': 82, 'b5': 83, 'c6': 84, '#c6': 85, 'd6': 86, '#d6': 87, 'e6': 88, 'f6': 89, '#f6': 90,
    'g6': 91, '#g6': 92, 'a6': 93, '#a6': 94, 'b6': 95, 'c7': 108, '#c7': 97, 'd7': 98, '#d7': 99, 'e7': 100,
    'f7': 101, '#f7': 102, 'g7': 103, '#g7': 104, 'a7': 105, '#a7': 106, 'b7': 107, 'c8': 108,
    # 如果没有输入音区：
    'C': 60, '#C': 61, 'D': 62, '#D': 63, 'E': 64, 'F': 65,
    '#F': 66, 'G': 67, '#G': 68, 'A': 69, '#A': 70, 'B': 71,
    # 如果没有音区也没有大小写
    'c': 60, '#c': 61, 'd': 62, '#d': 63, 'e': 64, 'f': 65,
    '#f': 66, 'g': 67, '#g': 68, 'a': 69, '#a': 70, 'b': 71
}

# note_names = list(note_value.key())
notes_names = [
    'A0', '#A0', 'B0', 'C1', '#C1', 'D1', '#D1', 'E1', 'F1', '#F1', 'G1', '#G1', 'A1', '#A1', 'B1',
    'C2', '#C2', 'D2', '#D2', 'E2', 'F2', '#F2', 'G2', '#G2', 'A2', '#A2', 'B2',
    'C3', '#C3', 'D3', '#D3', 'E3', 'F3', '#F3', 'G3', '#G3', 'A3', '#A3', 'B3',
    'C4', '#C4', 'D4', '#D4', 'E4', 'F4', '#F4', 'G4', '#G4', 'A4', '#A4', 'B4',
    'C5', '#C5', 'D5', '#D5', 'E5', 'F5', '#F5', 'G5', '#G5', 'A5', '#A5', 'B5',
    'C6', '#C6', 'D6', '#D6', 'E6', 'F6', '#F6', 'G6', '#G6', 'A6', '#A6', 'B6',
    'C7', '#C7', 'D7', '#D7', 'E7', 'F7', '#F7', 'G7', '#G7', 'A7', '#A7', 'B7', 'C8',
    'a0', '#a0', 'b0', 'c1', '#c1', 'd1', '#d1', 'e1', 'f1', '#f1', 'g1', '#g1', 'a1', '#a1', 'b1',
    'c2', '#c2', 'd2', '#d2', 'e2', 'f2', '#f2', 'g2', '#g2', 'a2', '#a2', 'b2',
    'c3', '#c3', 'd3', '#d3', 'e3', 'f3', '#f3', 'g3', '#g3', 'a3', '#a3', 'b3',
    'c4', '#c4', 'd4', '#d4', 'e4', 'f4', '#f4', 'g4', '#g4', 'a4', '#a4', 'b4',
    'c5', '#c5', 'd5', '#d5', 'e5', 'f5', '#f5', 'g5', '#g5', 'a5', '#a5', 'b5',
    'c6', '#c6', 'd6', '#d6', 'e6', 'f6', '#f6', 'g6', '#g6', 'a6', '#a6', 'b6',
    'c7', '#c7', 'd7', '#d7', 'e7', 'f7', '#f7', 'g7', '#g7', 'a7', '#a7', 'b7', 'c8',
    'C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B',
    'c', '#c', 'd', '#d', 'e', 'f', '#f', 'g', '#g', 'a', '#a', 'b'
]

chords_chroma_vector = {
    #
    #                                             三和弦
    #
    # 大三和弦                                     index:
    'C': [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 12*0
    '#C': [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    'D': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    '#D': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    'E': [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    'F': [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    '#F': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    'G': [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    'bA': [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'A': [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    'bB': [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    'B': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    # 小三和弦
    'Cm': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # 12*1
    '#Cm': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    'Dm': [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    '#Dm': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'Em': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    'Fm': [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Fm': [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    'Gm': [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    'bAm': [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    'Am': [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    'bBm': [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    'Bm': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    # 减三和弦
    'Cdim': [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 12*2
    '#Cdim': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    'Ddim': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Ddim': [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    'Edim': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'Fdim': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    '#Fdim': [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    'Gdim': [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    'bAdim': [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    'Adim': [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    'bBdim': [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    'Bdim': [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    # 增三和弦
    'C/E/#Gaug': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 12*3
    'bDaug/F/A': [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'D/#F/#Aaug': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    'bD/G/Baug': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    # 挂二/四和弦
    'Csus2/Gsus4': [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 4 + 12*3
    '#Csus2/bAsus4': [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'Dsus2/Asus4': [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    '#Dsus2/bBsus4': [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    'Esus2/Bsus4': [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    'Fsus2/Csus4': [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    '#Fsus2/#Csus4': [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    'Gsus2/Dsus4': [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    'bAsus2/#Dsus4': [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    'Asus2/Esus4': [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    'bBsus2/Fsus4': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    'Bsus2/#Fsus4': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    #
    #                                                省略音七和弦
    # 大七和弦（或增大七和弦）省略五音
    'CM7,-5': [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # 4 + 12*4
    '#CM7,-5': [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'DM7,-5': [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    '#DM7,-5': [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    'EM7,-5': [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    'FM7,-5': [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    '#FM7,-5': [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    'GM7,-5': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    'bAM7,-5': [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    'AM7,-5': [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    'bBM7,-5': [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    'BM7,-5': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    # 小大七和弦省略五音（有没有减大七和弦？）
    'CmM7,-5': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # 4 + 12*5
    '#CmM7,-5': [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'DmM7,-5': [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    '#DmM7,-5': [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    'EmM7,-5': [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    'FmM7,-5': [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    '#FmM7,-5': [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    'GmM7,-5': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    'bAmM7,-5': [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    'AmM7,-5': [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    'bBmM7,-5': [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    'BmM7,-5': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    # 属七和弦（或增小七和弦）省略五音
    'C7,-5': [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],  # 4 + 12*6
    '#C7,-5': [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    'D7,-5': [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    '#D7,-5': [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    'E7,-5': [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    'F7,-5': [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    '#F7,-5': [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    'G7,-5': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    'bA7,-5': [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    'A7,-5': [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    'bB7,-5': [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    'B7,-5': [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    # 属七和弦（或小七和弦）省略三音
    'C7,-3': [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 4 + 12*7
    '#C7,-3': [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    'D7,-3': [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    '#D7,-3': [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    'E7,-3': [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    'F7,-3': [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    '#F7,-3': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    'G7,-3': [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    'bA7,-3': [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    'A7,-3': [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    'bB7,-3': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    'B7,-3': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    # 小七和弦（或半减七和弦）省略五音
    'Cm7,-5': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # 4 + 12*8
    '#Cm7,-5': [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    'Dm7,-5': [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    '#Dm7,-5': [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    'Em7,-5': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    'Fm7,-5': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Fm7,-5': [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    'Gm7,-5': [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    'bAm7,-5': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    'Am7,-5': [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    'bBm7,-5': [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    'Bm7,-5': [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    # 半减七和弦省略三音
    'Cm7-3': [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 4 + 12*9
    '#Cm7-3': [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    'Dm7-3': [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    '#Dm7-3': [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    'Em7-3': [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    'Fm7-3': [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    '#Fm7-3': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    'Gm7-3': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    'bAm7-3': [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    'Am7-3': [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    'bBm7-3': [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    'Bm7-3': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    #
    #                                               七和弦
    # 大七和弦
    'CM7': [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],  # 4 + 12*10
    '#CM7': [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    'DM7': [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    '#DM7': [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    'EM7': [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    'FM7': [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    '#FM7': [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    'GM7': [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    'bAM7': [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    'AM7': [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    'bBM7': [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    'BM7': [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    # 增大七和弦（半增七和弦）
    'Caug7': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # 4 + 12*11
    '#Caug7': [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'Daug7': [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    '#Daug7': [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    'Eaug7': [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    'Faug7': [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    '#Faug7': [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    'Gaug7': [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    'bAaug7': [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    'Aaug7': [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    'bBaug7': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    'Baug7': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    # 小大七和弦
    'CmM7': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # 4 + 12*12
    '#CmM7': [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    'DmM7': [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    '#DmM7': [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'EmM7': [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    'FmM7': [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    '#FmM7': [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    'GmM7': [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    'bAmM7': [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    'AmM7': [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    'bBmM7': [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    'BmM7': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    # 属七和弦
    'C7': [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],  # 4 + 12*13
    '#C7': [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    'D7': [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    '#D7': [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    'E7': [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    'F7': [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    '#F7': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    'G7': [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    'bA7': [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    'A7': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    'bB7': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    'B7': [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    # 小七和弦
    'Cm7': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],  # 4 + 12*14
    '#Cm7': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    'Dm7': [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    '#Dm7': [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'Em7': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    'Fm7': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Fm7': [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    'Gm7': [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    'bAm7': [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    'Am7': [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    'bBm7': [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    'Bm7': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    # 半减七和弦（导七和弦，旧名减小七和弦）
    'Cm7-5': [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],  # 4 + 12*15
    '#Cm7-5': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    'Dm7-5': [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Dm7-5': [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    'Em7-5': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'Fm7-5': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    '#Fm7-5': [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    'Gm7-5': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    'bAm7-5': [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    'Am7-5': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    'bBm7-5': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    'Bm7-5': [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    # 减七和弦
    'C/#D/#F/A dim7': [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],  # 4 + 12*16
    '#C/E/G/bB dim7': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'D/F/bA/B dim7': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #
    #                                           六和弦和挂留七和弦
    # 大六和弦
    'C6': [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # 7 + 12*16
    '#C6': [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    'D6': [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    '#D6': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    'E6': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    'F6': [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    '#F6': [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'G6': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    'bA6': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    'A6': [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    'bB6': [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    'B6': [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    # 小六和弦
    'Cm6': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # 7 + 12*17
    '#Cm6': [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    'Dm6': [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    '#Dm6': [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    'Em6': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    'Fm6': [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    '#Fm6': [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    'Gm6': [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    'bAm6': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    'Am6': [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    'bBm6': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    'Bm6': [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    # 属七挂四和弦
    'C7sus4': [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],  # 7 + 12*18
    '#C7sus4': [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    'D7sus4': [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    '#D7sus4': [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    'E7sus4': [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    'F7sus4': [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    '#F7sus4': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    'G7sus4': [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    'bA7sus4': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    'A7sus4': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    'bB7sus4': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    'B7sus4': [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    #
    #                                               省略音九和弦：
    # 大九和弦省略七音（或加九音）
    'Cadd9': [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 7 + 12*19
    '#Cadd9': [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    'Dadd9': [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    '#Dadd9': [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    'Eadd9': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    'Fadd9': [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    '#Fadd9': [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    'Gadd9': [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    'bAadd9': [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    'Aadd9': [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    'bBadd9': [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    'Badd9': [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    # 大九和弦省略三音（也是五音的大三和弦加四音）
    'CM9,-3': [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 7 + 12*20
    '#CM9,-3': [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'DM9,-3': [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    '#DM9,-3': [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    'EM9,-3': [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    'FM9,-3': [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    '#FM9,-3': [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    'GM9,-3': [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    'bAM9,-3': [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    'AM9,-3': [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    'bBM9,-3': [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    'BM9,-3': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    # 大九和弦（小九和弦）省略五音
    'CM9,-5': [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # 7 + 12*21
    '#CM9,-5': [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    'DM9,-5': [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    '#DM9,-5': [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    'EM9,-5': [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    'FM9,-5': [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    '#FM9,-5': [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    'GM9,-5': [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    'bAM9,-5': [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    'AM9,-5': [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    'bBM9,-5': [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    'BM9,-5': [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    # TODO: unfinished
}

# The circle of fifth value of a pitch-class.
# 五度圈音级集和：
note_cof_value = {0: 0, 1: -5, 2: 2, 3: -3, 4: 4, 5: -1, 6: 6, 7: 1, 8: -4, 9: 3, 10: -2, 11: 5}
# 紧张度计算的音程预设值
note_tension = {0: 0, 1: 32, 2: 8, 3: 4, 4: 2, 5: 1, 6: 16, 7: 1, 8: 2, 9: 4, 10: 8, 11: 32}
