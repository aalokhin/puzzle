import math

class Reader:

    def parse_file(self, filepath):
        start = []
        complexity = 0

        with open(filepath) as fp:
            line = fp.readline()
            while line:
                if line.startswith('#'):
                    line = fp.readline()
                    continue
                elif line.strip().isdigit():
                    complexity = int(line)
                else:
                    line.strip()
                    if len(line) != 0:
                        start.append(' '.join(line.split()).split(' '))
                line = fp.readline()

        ret = [[0 for i in range(complexity)] for j in range(complexity)]
        for i in range(complexity):
            for j in range(complexity):
                ret[i][j] = int(start[i][j])
        return complexity, ret

    def find_solution(self, size):
        x = int(math.ceil(size / 2))
        print(x)
        model = [[0 for i in range(size)] for j in range(size)]
        print('--->{}'.format(model))
        s = 0
        for l in range(x):
            k = 0
            n = size - 2 * l
            p = 2 * n + 2 * (n - 2)
            h = (n - 1) * 3 + 1
            for j in range(l, n + l):
                model[l][j] = k + 1 + s
                model[size - l - 1][j] = h + s
                if (h + s) == (size * size) and j == l:
                    model[size - l - 1][j] = 0
                h -= 1
                k += 1
            k = 0
            for i in range(l + 1, size - l - 1):
                model[i][l] = p + s
                model[i][size - l - 1] = n + k + 1 + s
                p -= 1
                k += 1
            s += 2 * n + 2 * (n - 2)
        print('--->{}'.format(model))
        return model