import math

from Utils import *


class Calculator:

    """like manhattan but hundred times slowe plus needs refactoring"""
    @staticmethod
    def euclidian_heuristic(current_board, goal_raw, size):
        distance = 0
        current = Calculator.flatten_2d(current_board)
        goal = Calculator.coordinates_tuple(goal_raw)
        for i in range(size):
            for j in range(size):
                pos = i * size + j
                if current[pos] != 0:
                    value = current[pos]
                    print( "value{}".format(value))
                    pos_in_model = goal[value]
                    dx = pos_in_model % size - pos % size
                    dy = math.floor(pos_in_model / size) - math.floor(pos / size)
                    distance += math.sqrt(dx * dx + dy * dy)
        return distance

    @staticmethod
    def different_sign(a, b):
        if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
            return False
        return True

    @staticmethod
    def linear_conflict(current_board, goal_raw, size):
        conflict = 0

        current = MyList(current_board).flatten()
        goal = MyList(goal_raw).coordinates_tuple()

        sqr_size = int(math.pow(size, 2))
        for i in range(sqr_size):
            if i / size == goal[current[i]] / size and current[i] != 0:
                j = 1
                while (j + i % size < size):
                    if (i + j) / size == goal[current[i + j]] / size and current[i + j] != 0 and current[i] != 0:
                        if Calculator.different_sign(j, goal[current[i + j]] % size - goal[
                            current[i]] % size):
                            conflict += 1
                    j += 1
            if i % size == goal[current[i]] % size and current[i] != 0:
                j = size
                while ((j + i) / size < size):
                    if (i + j) % size == goal[current[i + j]] % size and current[i + j] != 0 and current[i] != 0:
                        if Calculator.different_sign(j, goal[current[i + j]] / size - goal[
                            current[i]] / size):
                            conflict += 1
                    j += size
        return conflict

    @staticmethod
    def linear_conflict_efficient(current_board, goal_dict, size):
        number_of_conflicts = 0
        iterations = int(math.pow(size, 2))
        current_list = MyList(current_board).flatten()

        print("cur cur >>> {}".format(current_list))
        return 0

    @staticmethod
    def manhattan_distance(current_board, goal_board_dict, size):
        distance = 0
        for i in range(size):
            for j in range(size):
                lookup_val = current_board[i][j]
                if lookup_val != 0:
                    x = i
                    y = j
                    goal_x, goal_y = goal_board_dict[lookup_val]
                    distance += math.fabs(x - goal_x) + math.fabs(y - goal_y)
                else:
                    continue
        # print('manhattan {}'.format(distance))
        # if distance == 0:
        #     print('current board is {}'.format(current_board))
        #     print('goal board is {}'.format(goal_board_dict))
        return distance

    @staticmethod
    def hamming_distance(current_board, goal_board, size):
        misplaced_tiles = 0
        for i in range(size):
            for j in range(size):
                if current_board[i][j] != goal_board[i][j] and current_board[i][j] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles
