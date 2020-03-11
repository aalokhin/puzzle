import math

from Node import Node
from Calculator import Calculator


class Puzzle:
    def __init__(self, size, goal_position):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []
        self.goal = goal_position
        self.goal_dict = Calculator.coordinates_dictionary(goal_position) #self.coordinates_dictionary(goal_position)

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        #return Calculator.manhattan_distance(start.data, self.goal_dict, self.n) + start.level

        return Calculator.hamming_distance(start.data, self.goal, self.n)
        #return Calculator.h(start.data, self.goal, self.n)+start.level

    def print_result(self, cur):
        print("")
        print("  | ")
        print("  | ")
        print(" \\\'/ \n")
        print('level is {}'.format(cur.level))
        print(str(cur))

    def process(self, puzzle):
            """ Accept Start and Goal Puzzle state"""
            start = puzzle
            iteration = 0
            start = Node(start, 0, 0, None)
            start.fval = self.f(start, self.goal)
            """ Put the start node in the open list"""
            self.open.append(start)
            print("\n\n")
            while True:
                iteration+=1
                cur = self.open[0]
                self.print_result(cur)
                """ If the difference between current and goal node is 0 we have reached the goal node"""
                if Calculator.manhattan_distance(cur.data, self.goal_dict, self.n) == 0:
                    print('hurra we found a solutions --> heuristic manhattan -> {}'.format(cur.level))
                    print('the step iteration {}'.format(iteration))
                    while True:
                        prev = cur.parent
                        print(prev)
                        cur = prev
                        if cur is None:
                            break

                    break
                if Calculator.h(cur.data, self.goal, self.n) == 0:
                    print('hurra we found a solutions --> heuristic h ')
                    break

                children = cur.generate_child(self.closed)
                for i in children:
                    i.fval = self.f(i, self.goal)
                    if Calculator.manhattan_distance(i.data, Calculator.coordinates_dictionary(cur.data), self.n) != 0:
                        self.open.append(i)

                self.closed.append(cur)
                del self.open[0]


                """ sort the opne list based on f value """
                self.open.sort(key=lambda x: x.fval, reverse=False)
                for one in self.open:
                    print('level is{}'.format(one.level))
                    print(str(one))

