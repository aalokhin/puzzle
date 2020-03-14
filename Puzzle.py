import math

from Node import Node
from Calculator import Calculator


class Puzzle:
    def __init__(self, size, goal_position):
        """ open list for nodes that haven't yet been checkd on children; closed are those whose children we have added to open list """
        self.n = size
        self.open = []
        self.closed = []
        self.goal = goal_position
        self.goal_dict = Calculator.coordinates_dictionary(goal_position) #self.coordinates_dictionary(goal_position)

    def f(self,start,goal):
        """ Will need to use lambdas here Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) ;
        with f(x) = h(x) works faster for some reason , need to check """
        """so slow"""
        #return Calculator.euclidian_heuristic(start.data, self.goal, self.n) + start.level

        return Calculator.linear_conflict(start.data, self.goal, self.n) * 2 \
               + Calculator.manhattan_distance(start.data, self.goal_dict, self.n) + start.level

        """so far the lowest  level """
        #return Calculator.manhattan_distance(start.data, self.goal_dict, self.n) + start.level
        """so far the best speed but something is wrong with parents """
        #return Calculator.manhattan_distance(start.data, self.goal_dict, self.n)
        # return Calculator.hamming_distance(start.data, self.goal, self.n)
        """This line will warm up your PC as if it was not a line but a whole Android studio"""
        #return Calculator.hamming_distance(start.data, self.goal, self.n) + start.level

    def print_result(self, cur):
        print("")
        print("  | ")
        print("  | ")
        print(" \\\'/ \n")
        print('level is {}'.format(cur.level))
        print(str(cur))

    def process(self, puzzle):
            """ takes starting state and appends it to open list. the goal state has been created during initialization"""
            start = puzzle
            iteration = 0
            start = Node(start, 0, 0, None)
            start.fval = self.f(start, self.goal)
            """ Put the start node in the open list"""
            self.open.append(start)
            print("\n\n")
            """algorithm starting"""
            while len(self.open) != 0:
                iteration += 1
                cur = self.open[0]
                self.print_result(cur)
                """ If the difference between current and goal boaed is 0 we have reached the goal node"""
                if cur == self.goal:
                    print('hurra we found a solutions --> heuristic manhattan -> {}'.format(cur.level))
                    print('the step iteration {}'.format(iteration))
                    while True:
                        prev = cur.parent
                        print(prev)
                        cur = prev
                        if cur is None:
                            break
                    break
                print('Length of open before {}'.format(len(self.open)))
                children = cur.generate_child(self.closed, self.open)
                print('Length of open after {}'.format(len(self.open)))

                for i in children:
                    i.fval = self.f(i, self.goal)
                    self.open.append(i)
                """ moving current node to the closed list and deleting it from the open list """

                self.closed.append(cur)
                del self.open[0]

                """ sort the open list based on the  value of our heuristic function"""
                self.open.sort(key=lambda x: x.fval, reverse=False)
