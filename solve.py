from Puzzle import Puzzle
from argparse import ArgumentParser
from Reader import Reader

import logging


class Solve:

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="write report to FILE", metavar="FILE")

    args = parser.parse_args()
    filepath = args.filename
    goal = []
    reader = Reader()
    size, start_position = reader.parse_file(filepath)
    goal_position = reader.find_solution(size)
    puz = Puzzle(size, goal_position)
    puz.process(start_position)

