from Calculator import Calculator

"""these functions are here just because i am not sure hwo to structure this stuff yet"""


def level_is_lower(node, nodes):
    for i in range(len(nodes)):
        if node == nodes[i] and node.level < nodes[i].level:
            print("we have equal nodes. child_node level is {} and other node's level is {} \
            therefore we leave child but delete the node with higher tree level".format(node.level, nodes[i].level))
            del nodes[i]
            return True
    return False


class Node:
    def __init__(self, data, level, fval, parent):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.data_dict = Calculator.coordinates_dictionary(data)
        self.level = level
        self.fval = fval
        self.parent = parent

    def generate_child(self, parents, open_list):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x, y = self.get_current_coordinates(self.data, 0)
        # print('x->{} y ->{}'.format(x, y))
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        for i in val_list:
            if i[0] < 0 or i[0] >= len(self.data) or i[1] < 0 or i[1] >= len(self.data):
                val_list.remove(i)
        children = []
        for i in val_list:
            child = self.shuffle(x, y, i[0], i[1])
            child_node = Node(child, self.level + 1, 0, self)
            if not (child_node in parents) and not (child_node in open_list):
                print("this child never existed before")
                children.append(child_node)
            elif child_node in open_list:
                if level_is_lower(child_node, open_list):
                    print("this child existed before")
                    children.append(child_node)
            else:
                print("this child existed before")
        # print('================ children =====================')
        # for child in children:
        #     print('-----------')
        #     print(str(child))
        #     print('-----------')
        # print('================ children =====================')
        return children

    def shuffle(self, x1, y1, x2, y2):
        """ Move the blank space in the given direction; the coordinates are guaranteed to be valid  """
        # print('coordinates we received x {} y {}'.format(x2, y2))
        temp_puz = self.copy()
        temp = temp_puz[x2][y2]
        temp_puz[x2][y2] = temp_puz[x1][y1]
        temp_puz[x1][y1] = temp
        return temp_puz

    def get_current_coordinates(self, puz, val):
        """ Specifically used to find the position of the blank space """
        return self.data_dict[val]

    def copy(self):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in self.data:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    """eases printing"""
    def __str__(self):
        ret = ''
        for i in self.data:
            for j in i:
                ret += str(j)
                ret += ' '
            ret += '\n'
        return ret

    """two nodes are equal if there data are equal. we don't consider level here"""

    def __eq__(self, other):
        if isinstance(other, Node):
            return other.data == self.data
        return self.data == other
