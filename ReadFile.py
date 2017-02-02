__author__ = 'jalali'


class ReadFile:
    def __init__(self, read_file_name, writeFileName):
        self.input_file = open(read_file_name)
        self.map = []

    def read_file(self):
        line = self.input_file.readline()
        while line:
            # print line
            temp_list = line.strip().split(" ")
            # print temp_list
            self.map.append(temp_list)
            line = self.input_file.readline()

        self.input_file.close()
        x = []
        for i in range(0, len(self.map)):
            ttemp = []
            for j in range(0, len(self.map)):
                ttemp.append('.')
            x.append(ttemp)
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[i])):
                x[j][i] = self.map[i][j]
        # print len(self.map)
        return self.map
