import builtins


class MyList(list):
    def __init__(self, li):
        super(MyList, self).__init__(li)

    def flatten(self):
        res = []
        for x, row in enumerate(self):
            for y, value in enumerate(row):
                res.append(self[x][y])
        return res

    def coordinates_tuple(self):
        coordinates_board = {}
        i = 0
        for x, row in enumerate(self):
            for y, value in enumerate(row):
                coordinates_board[value] = i
                i += 1
        return coordinates_board

    def coordinates_dictionary(self):
        coordinates_board = {}
        for x, row in enumerate(self):
            for y, value in enumerate(row):
                coordinates_board[value] = (x, y)
        return coordinates_board
