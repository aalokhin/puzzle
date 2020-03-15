import math

from Utils import *


class Calculator:

    """like manhattan but hundred times slowe plus needs refactoring"""
    @staticmethod
    def euclidian_heuristic(current_board, goal_raw, size):
        distance = 0
        current = MyList(current_board).flatten()
        goal = MyList(goal_raw).coordinates_tuple()
        for i in range(size):
            for j in range(size):
                pos = i * size + j
                if current[pos] != 0:
                    value = current[pos]
                    print("value{}".format(value))
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
    def count_linear_conflict(current_board, goal_raw, size):
        number_of_conflicts = 0
        sqr_size = int(math.pow(size, 2))
        current = MyList(current_board).flatten()
        goal = MyList(goal_raw).coordinates_tuple()
        for i in range(sqr_size):
            value_to_check = current[i]
            if value_to_check != 0:
                if i / size == goal[value_to_check] / size:
                    j = 1
                    while (j + i % size < size):
                        if (i + j) / size == goal[current[i + j]] / size and current[i + j] != 0 and current[i] != 0:
                            if Calculator.different_sign(j, goal[current[i + j]] % size - goal[current[i]] % size):
                                number_of_conflicts += 1
                        j += 1
                if i % size == goal[value_to_check] % size:
                    j = size
                    while ((j + i) / size < size):
                        if (i + j) % size == goal[current[i + j]] % size and current[i + j] != 0 and current[i] != 0:
                            if Calculator.different_sign(j, goal[current[i + j]] / size - goal[current[i]] / size):
                                number_of_conflicts += 1
                        j += size

        if number_of_conflicts != 0:
            print("my linear conflict is: \n{} \n{}".format(current_board, goal_raw))

        return number_of_conflicts


    @staticmethod
    def manhattan_distance(current_board, goal_board_dict, size):
        distance = 0
        for x in range(size):
            for y in range(size):
                lookup_val = current_board[x][y]
                if lookup_val != 0:
                    goal_x, goal_y = goal_board_dict[lookup_val]
                    distance += math.fabs(x - goal_x) + math.fabs(y - goal_y)
        return distance

    @staticmethod
    def hamming_distance(current_board, goal_board, size):
        misplaced_tiles = 0
        for i in range(size):
            for j in range(size):
                if current_board[i][j] != goal_board[i][j] and current_board[i][j] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles

    # @staticmethod
    # def linear_conflict(current_board, goal_raw, size):
    #     conflict = 0
    #
    #     current = MyList(current_board).flatten()
    #     goal = MyList(goal_raw).coordinates_tuple()
    #
    #     sqr_size = int(math.pow(size, 2))
    #     for i in range(sqr_size):
    #         # print(" i / size is {} and goal[cur[i]] / size is {} ".format((i / size), (goal[current[i]] / size)))
    #
    #         if i / size == goal[current[i]] / size and current[i] != 0:
    #             j = 1
    #             while (j + i % size < size):
    #                 if (i + j) / size == goal[current[i + j]] / size and current[i + j] != 0 and current[i] != 0:
    #                     if Calculator.different_sign(j, goal[current[i + j]] % size - goal[current[i]] % size):
    #                         conflict += 1
    #                 j += 1
    #         if i % size == goal[current[i]] % size and current[i] != 0:
    #             j = size
    #             while ((j + i) / size < size):
    #                 if (i + j) % size == goal[current[i + j]] % size and current[i + j] != 0 and current[i] != 0:
    #                     if Calculator.different_sign(j, goal[current[i + j]] / size - goal[current[i]] / size):
    #                         conflict += 1
    #                 j += size
    #     if conflict != 0:
    #         print("Linear conflict is: \n{} \n{}".format(current_board, goal_raw))
    #
    #     return conflict

