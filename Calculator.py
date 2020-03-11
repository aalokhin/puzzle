import math


class Calculator:
    @staticmethod
    def coordinates_dictionary(board):
        coordinates_board = {}
        for x, row in enumerate(board):
            for y, value in enumerate(row):
                coordinates_board[value] = (x, y)
        #print("here we go {} ".format(coordinates_board))
        return coordinates_board

    @staticmethod
    def manhattan_distance(current_board, goal_board_dict, size):
        distance = 0
        for i in range(size):
            for j in range(size):
                lookup_val = current_board[i][j]
                x = i
                y = j
                goal_x, goal_y = goal_board_dict[lookup_val]
                distance += math.fabs(x - goal_x) + math.fabs(y - goal_y)
        #print('manhattan {}'.format(distance))
        # if distance == 0:
        #     print('current board is {}'.format(current_board))
        #     print('goal board is {}'.format(goal_board_dict))
        return distance
    @staticmethod
    def hamming_distance(current_board, goal_board, size):
        misplaced_tiles = 0
        for i in range(size):
            for j in range(size):
                if current_board[i][j] != goal_board[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles


    @staticmethod
    def h(start, goal, size):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,size):
            for j in range(0,size):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp += 1
        #print('temp {}'.format(temp))
        return temp
