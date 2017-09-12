from Classes.Options import Options


class StressParser():
    def __init__(self, fname):
        self.__f = open(fname, 'r')
        self.__parse()

    def __parse(self):
        o = Options()
        multiplier = o.getProperty('multiplier')
        self.__f.readline()
        self.__timestep = int(self.__f.readline())
        self.__f.readline()
        self.__atomsNum = int(self.__f.readline())
        l = len(self.__f.readline().split())
        if l == 9:
            [xlo, xhi, trash] = self.__f.readline().split()
            [ylo, yhi, trash] = self.__f.readline().split()
            [zlo, zhi, trash] = self.__f.readline().split()
        else:
            [xlo, xhi] = self.__f.readline().split()
            [ylo, yhi] = self.__f.readline().split()
            [zlo, zhi] = self.__f.readline().split()
        [xlo, xhi] = [float(xlo), float(xhi)]
        [ylo, yhi] = [float(ylo), float(yhi)]
        [zlo, zhi] = [float(zlo), float(zhi)]
        self.__xlo = xlo
        self.__xhi = xhi
        self.__ylo = ylo
        self.__yhi = yhi
        self.__zlo = zlo
        self.__zhi = zhi
        self.__f.readline()
        self.__stresses = [0 for i in range(int((zhi - zlo + 1) * multiplier + 1))]
        for i in range(self.__atomsNum):
            ls = self.__f.readline().split()
            z = int((float(ls[1]) - zlo) * multiplier)
            self.__stresses[z] += float(ls[2])

    def stresses(self):
        return self.__stresses

    def lx(self):
        return self.__xhi - self.__xlo

    def ly(self):
        return self.__yhi - self.__ylo

    def lz(self):
        return self.__zhi - self.__zlo
        
    def zlo(self):
        return self.__zlo