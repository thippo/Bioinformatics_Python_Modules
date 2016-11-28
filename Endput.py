class Endput():

    def __init__(self, number_lines, tofile=''):
        self.number_lines = number_lines
        self.n = 1
        if tofile:
            self.tofile = open(tofile, 'a')
        else:
            self.tofile = tofile

    def generator(self, line):
        if self.n == self.number_lines:
            self.n +=1
            yield line
        elif self.n < self.number_lines:
            self.n +=1
            yield line+'\n'
        else:
            raise StopIteration

    def __call__(self, line):
        if not self.tofile:
            return self.generator(line).__next__()
        else:
            self.tofile.write(self.generator(line).__next__())
            if self.n == self.number_lines+1:
                self.tofile.close()
