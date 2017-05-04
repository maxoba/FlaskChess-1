import pprint

# class White:
#     def __init__(self):
#         self.pawn = [
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [50, 50, 50, 50, 50, 50, 50, 50],
#             [10, 10, 20, 30, 30, 20, 10, 10],
#             [5, 5, 10, 25, 25, 10, 5, 5],
#             [0, 0, 0, 20, 20, 0, 0, 0],
#             [5, -5, -10, 0, 0, -10, -5, 5],
#             [5, 10, 10, -20, -20, 10, 10, 5],
#             [0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#         self.knight = [
#             [-50, -40, -30, -30, -30, -30, -40, -50],
#             [-40, -20, 0, 0, 0, 0, -20, -40],
#             [-30, 0, 10, 15, 15, 10, 0, -30],
#             [-30, 5, 15, 20, 20, 15, 5, -30],
#             [-30, 0, 15, 20, 20, 15, 0, -30],
#             [-30, 5, 10, 15, 15, 10, 5, -30],
#             [-40, -20, 0, 5, 5, 0, -20, -40],
#             [-50, -40, -30, -30, -30, -30, -40, -50]
#         ]
#         self.bishop = [
#             [-20, -10, -10, -10, -10, -10, -10, -20],
#             [-10, 0, 0, 0, 0, 0, 0, -10],
#             [-10, 0, 5, 10, 10, 5, 0, -10],
#             [-10, 5, 5, 10, 10, 5, 5, -10],
#             [-10, 0, 10, 10, 10, 10, 0, -10],
#             [-10, 10, 10, 10, 10, 10, 10, -10],
#             [-10, 5, 0, 0, 0, 0, 5, -10],
#             [-20, -10, -10, -10, -10, -10, -10, -20]
#         ]
#         self.rook = [
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [5, 10, 10, 10, 10, 10, 10, 5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [0, 0, 0, 5, 5, 0, 0, 0]
#         ]
#         self.queen = [
#              [-20, -10, -10, -5, -5, -10, -10, -20],
#              [-10, 0, 0, 0, 0, 0, 0, -10],
#              [-10, 0, 5, 5, 5, 5, 0, -10],
#              [-5, 0, 5, 5, 5, 5, 0, -5],
#              [0, 0, 5, 5, 5, 5, 0, -5],
#              [-10, 5, 5, 5, 5, 5, 0, -10],
#              [-10, 0, 5, 0, 0, 0, 0, -10],
#              [-20, -10, -10, -5, -5, -10, -10, -20]
#         ]
#         self.king = [
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-20, -30, -30, -40, -40, -30, -30, -20],
#             [-10, -20, -20, -20, -20, -20, -20, -10],
#             [20, 20, 0, 0, 0, 0, 20, 20],
#             [20, 30, 10, 0, 0, 10, 30, 20]
#         ]
#
# class Black:
#     def __init__(self):
#         self.pawn = [
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [5, 10, 10, -20, -20, 10, 10, 5],
#             [5, -5, -10, 0, 0, -10, -5, 5],
#             [0, 0, 0, 20, 20, 0, 0, 0],
#             [5, 5, 10, 25, 25, 10, 5, 5],
#             [10, 10, 20, 30, 30, 20, 10, 10],
#             [50, 50, 50, 50, 50, 50, 50, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#         self.knight = [
#             [-50, -40, -30, -30, -30, -30, -40, -50],
#             [-40, -20, 0, 0, 0, 0, -20, -40],
#             [-30, 0, 10, 15, 15, 10, 0, -30],
#             [-30, 5, 15, 20, 20, 15, 5, -30],
#             [-30, 0, 15, 20, 20, 15, 0, -30],
#             [-30, 5, 10, 15, 15, 10, 5, -30],
#             [-40, -20, 0, 5, 5, 0, -20, -40],
#             [-50, -40, -30, -30, -30, -30, -40, -50]
#         ]
#         self.bishop = [
#             [-20, -10, -10, -10, -10, -10, -10, -20],
#             [-10, 0, 0, 0, 0, 0, 0, -10],
#             [-10, 0, 5, 10, 10, 5, 0, -10],
#             [-10, 5, 5, 10, 10, 5, 5, -10],
#             [-10, 0, 10, 10, 10, 10, 0, -10],
#             [-10, 10, 10, 10, 10, 10, 10, -10],
#             [-10, 5, 0, 0, 0, 0, 5, -10],
#             [-20, -10, -10, -10, -10, -10, -10, -20]
#         ]
#         self.rook = [
#             [0, 0, 0, 5, 5, 0, 0, 0],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [-5, 0, 0, 0, 0, 0, 0, -5],
#             [5, 10, 10, 10, 10, 10, 10, 5],
#             [0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#         self.queen = [
#              [-20, -10, -10, -5, -5, -10, -10, -20],
#              [-10, 0, 0, 0, 0, 0, 0, -10],
#              [-10, 0, 5, 5, 5, 5, 0, -10],
#              [-5, 0, 5, 5, 5, 5, 0, -5],
#              [0, 0, 5, 5, 5, 5, 0, -5],
#              [-10, 5, 5, 5, 5, 5, 0, -10],
#              [-10, 0, 5, 0, 0, 0, 0, -10],
#              [-20, -10, -10, -5, -5, -10, -10, -20]
#         ]
#         self.king = [
#             [20, 30, 10, 0, 0, 10, 30, 20],
#             [20, 20, 0, 0, 0, 0, 20, 20],
#             [-10, -20, -20, -20, -20, -20, -20, -10],
#             [-20, -30, -30, -40, -40, -30, -30, -20],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30],
#             [-30, -40, -40, -50, -50, -40, -40, -30]
#         ]

class White:
    def __init__(self):
        self.pawn = [
            0, 0, 0, 0, 0, 0, 0, 0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
            5, 5, 10, 25, 25, 10, 5, 5,
            0, 0, 0, 20, 20, 0, 0, 0,
            5, -5, -10, 0, 0, -10, -5, 5,
            5, 10, 10, -20, -20, 10, 10, 5,
            0, 0, 0, 0, 0, 0, 0, 0
        ]
        self.knight = [
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50,
        ]
        self.bishop = [
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 10, 10, 5, 0, -10,
            -10, 5, 5, 10, 10, 5, 5, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -20, -10, -10, -10, -10, -10, -10, -20,
        ]
        self.rook = [
            0, 0, 0, 0, 0, 0, 0, 0,
            5, 10, 10, 10, 10, 10, 10, 5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            0, 0, 0, 5, 5, 0, 0, 0
        ]
        self.queen = [
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -5, 0, 5, 5, 5, 5, 0, -5,
            0, 0, 5, 5, 5, 5, 0, -5,
            -10, 5, 5, 5, 5, 5, 0, -10,
            -10, 0, 5, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20
        ]
        self.king = [
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -20, -30, -30, -40, -40, -30, -30, -20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            20, 20, 0, 0, 0, 0, 20, 20,
            20, 30, 10, 0, 0, 10, 30, 20
        ]

class Black:
    def __init__(self):
        self.pawn = [
            0, 0, 0, 0, 0, 0, 0, 0,
            5, 10, 10, -20, -20, 10, 10, 5,
            5, -5, -10, 0, 0, -10, -5, 5,
            0, 0, 0, 20, 20, 0, 0, 0,
            5, 5, 10, 25, 25, 10, 5, 5,
            10, 10, 20, 30, 30, 20, 10, 10,
            50, 50, 50, 50, 50, 50, 50, 50,
            0, 0, 0, 0, 0, 0, 0, 0
        ]
        self.knight = [
            -50, -40, -30, -30, -30, -30, -40, -50,
            -40, -20, 0, 0, 0, 0, -20, -40,
            -30, 0, 10, 15, 15, 10, 0, -30,
            -30, 5, 15, 20, 20, 15, 5, -30,
            -30, 0, 15, 20, 20, 15, 0, -30,
            -30, 5, 10, 15, 15, 10, 5, -30,
            -40, -20, 0, 5, 5, 0, -20, -40,
            -50, -40, -30, -30, -30, -30, -40, -50,
        ]
        self.bishop = [
            -20, -10, -10, -10, -10, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 10, 10, 5, 0, -10,
            -10, 5, 5, 10, 10, 5, 5, -10,
            -10, 0, 10, 10, 10, 10, 0, -10,
            -10, 10, 10, 10, 10, 10, 10, -10,
            -10, 5, 0, 0, 0, 0, 5, -10,
            -20, -10, -10, -10, -10, -10, -10, -20,
        ]
        self.rook = [
            0, 0, 0, 5, 5, 0, 0, 0,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            -5, 0, 0, 0, 0, 0, 0, -5,
            5, 10, 10, 10, 10, 10, 10,
            5, 0, 0, 0, 0, 0, 0, 0, 0
        ]
        self.queen = [
            -20, -10, -10, -5, -5, -10, -10, -20,
            -10, 0, 0, 0, 0, 0, 0, -10,
            -10, 0, 5, 5, 5, 5, 0, -10,
            -5, 0, 5, 5, 5, 5, 0, -5,
            0, 0, 5, 5, 5, 5, 0, -5,
            -10, 5, 5, 5, 5, 5, 0, -10,
            -10, 0, 5, 0, 0, 0, 0, -10,
            -20, -10, -10, -5, -5, -10, -10, -20
        ]
        self.king = [
            20, 30, 10, 0, 0, 10, 30, 20,
            20, 20, 0, 0, 0, 0, 20, 20,
            -10, -20, -20, -20, -20, -20, -20, -10,
            -20, -30, -30, -40, -40, -30, -30, -20,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30,
            -30, -40, -40, -50, -50, -40, -40, -30
        ]

square_table = {
    1: [
        0, 0, 0, 0, 0, 0, 0, 0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5, 5, 10, 25, 25, 10, 5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, -5, -10, 0, 0, -10, -5, 5,
        5, 10, 10, -20, -20, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0
    ],
    2: [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50,
    ],
    3: [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -20, -10, -10, -10, -10, -10, -10, -20,
    ],
    4: [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, 10, 10, 10, 10, 5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        0, 0, 0, 5, 5, 0, 0, 0
    ],
    5: [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -5, 0, 5, 5, 5, 5, 0, -5,
        0, 0, 5, 5, 5, 5, 0, -5,
        -10, 5, 5, 5, 5, 5, 0, -10,
        -10, 0, 5, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],
    6: [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        20, 20, 0, 0, 0, 0, 20, 20,
        20, 30, 10, 0, 0, 10, 30, 20
    ]
}

def format(table):
    newtable = []
    rowcount = 0
    i = 0

    while rowcount < 8:
        squarecount = 0
        row = []
        while squarecount < 8:
            row.append(table[i])
            squarecount += 1
            i += 1
        newtable.append(row)
        rowcount += 1

    print(newtable)

def reverse(table):
    print( table[::-1])

if __name__=="__main__":
    table = [
        0, 0, 0, 0, 0, 0, 0, 0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5, 5, 10, 25, 25, 10, 5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, -5, -10, 0, 0, -10, -5, 5,
        5, 10, 10, -20, -20, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0
    ]

    reverse(table)



