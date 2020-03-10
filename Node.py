from Calculator import Calculator


class Node:
    def __init__(self, data, level, fval, parent):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.data_dict = Calculator.coordinates_dictionary(data)
        self.level = level
        self.fval = fval
        self.parent = parent


    def check_if_child_was_ever_born(self, potential_child, parents, size):
        for parent in parents:
            if Calculator.manhattan_distance(parent.data, Calculator.coordinates_dictionary(potential_child.data), size) == 0:
                return 1
        return 0


    def generate_child(self, parents):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x, y = self.get_current_coordinates(self.data, 0)
        #print('x->{} y ->{}'.format(x, y))
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        for i in val_list:
            if i[0] < 0 or i[0] >= len(self.data) or i[1] < 0 or i[1] >= len(self.data):
               val_list.remove(i)

        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            child_node = Node(child, self.level + 1, 0, self)
            if self.check_if_child_was_ever_born(child_node, parents, 3) == 0:
                children.append(child_node)
            # else:
            #     print("this child existed before")
        #
        # for i in children:
        #     print(str(i))
        # for j in i:
        #             print(j, end=" ")
        #         print("")
        #     print('-----------')

        # print('================ children =====================')
        # for child in children:
        #     print('-----------')
        #
        #     for i in child.data:
        #         for j in i:
        #             print(j, end=" ")
        #         print("")
        #     print('-----------')
        # print('================ children =====================')
        return children


    def shuffle(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        #print('coordinates we received x {} y {}'.format(x2, y2))
        temp_puz = self.copy(puz)
        temp = temp_puz[x2][y2]
        temp_puz[x2][y2] = temp_puz[x1][y1]
        temp_puz[x1][y1] = temp
        return temp_puz


    def copy(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def get_current_coordinates(self, puz, val):
        """ Specifically used to find the position of the blank space """
        return self.data_dict[val]

    def __str__(self):
        ret = ''
        for i in self.data:
            for j in i:
                ret += str(j)
                ret+=' '
            ret += '\n'
        return ret
