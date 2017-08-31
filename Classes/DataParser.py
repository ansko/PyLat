class DataParser():
    def __init__(self, fname):
        self.__fname = fname
        self.__parseHeader()
    
    def __parseHeader(self):
        self.__f = open(self.__fname, 'r')
        self.__f.readline()
        self.__f.readline()
        self.__atomsNum = int(self.__f.readline().split()[0])
        self.__atomsTypesNum = int(self.__f.readline().split()[0])
        self.__bondsNum = int(self.__f.readline().split()[0])
        self.__bondsTypeNum = int(self.__f.readline().split()[0])
        self.__anglesNum = int(self.__f.readline().split()[0])
        self.__anglesTypesNum = int(self.__f.readline().split()[0])
        self.__dihedralsNum = int(self.__f.readline().split()[0])
        self.__dihedralsTypesNum = int(self.__f.readline().split()[0])
        self.__impropersNum = int(self.__f.readline().split()[0])
        self.__impropersTypesNum = int(self.__f.readline().split()[0])
        self.__f.readline()
        words = self.__f.readline().split()
        self.__xlo = float(words[0])
        self.__xhi = float(words[1])
        words = self.__f.readline().split()
        self.__ylo = float(words[0])
        self.__yhi = float(words[1])
        words = self.__f.readline().split()
        self.__zlo = float(words[0])
        self.__zhi = float(words[1])
        words = self.__f.readline().split()
        if len(words) > 0:
            self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__masses = [None,]
        while len(words) > 0:
            self.__masses.append(0)
            self.__masses[int(words[0])] = float(words[1])
            words = self.__f.readline().split()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__pairCoeffs = [None,]
        while len(words) > 0:
            self.__pairCoeffs.append([0, 0])
            self.__pairCoeffs[int(words[0])] = [float(words[1]),
                                                float(words[2])]
            words = self.__f.readline().split()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__bondCoeffs = [None,]
        while len(words) > 0:
            self.__bondCoeffs.append([0, 0])
            self.__bondCoeffs[int(words[0])] = [float(words[1]),
                                                float(words[2])]
            words = self.__f.readline().split()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__angleCoeffs = [None,]
        while len(words) > 0:
            self.__angleCoeffs.append([0, 0])
            self.__angleCoeffs[int(words[0])] = [float(words[1]), 
                                                 float(words[2])]
            words = self.__f.readline().split()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__dihedralCoeffs = [None,]
        while len(words) > 0:
            self.__dihedralCoeffs.append([0, 0, 0])
            self.__dihedralCoeffs[int(words[0])] = [float(words[1]),
                                                    float(words[2]),
                                                    float(words[3])]
            words = self.__f.readline().split()
        self.__f.readline()
        self.__f.readline()
        words = self.__f.readline().split()
        self.__improperCoeffs = [None,]
        while len(words) > 0:
            self.__improperCoeffs.append([0, 0, 0])
            self.__improperCoeffs[int(words[0])] = [float(words[1]),
                                                    float(words[2]),
                                                    float(words[3])]
            words = self.__f.readline().split()

    def parseAtoms(self):
        self.__f.readline()
        self.__f.readline()
        self.__atoms = [None, ]
        for i in range(self.__atomsNum):
            self.__atoms.append([0, 0, 0, 0, 0, 0])
        for i in range(self.__atomsNum):
            words = self.__f.readline().split()
            self.__atoms[int(words[0])] = [int(words[1]),
                                           int(words[2]),
                                           float(words[3]),
                                           float(words[4]),
                                           float(words[5]),
                                           float(words[6])]
                                           
    def parseVelocities(self):
        self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        self.__velocities = [None, ]
        for i in range(self.__atomsNum):
            self.__velocities.append([0, 0, 0])
        for i in range(self.__atomsNum):
            words = self.__f.readline().split()
            self.__velocities[int(words[0])] = [float(words[1]),
                                                float(words[2]),
                                                float(words[3])]
    def parseBonds(self):
        self.parseVelocities()
        self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        self.__bonds = [None, ]
        for i in range(self.__bondsNum):
            self.__bonds.append([0, 0, 0])
        for i in range(self.__bondsNum):
            words = self.__f.readline().split()
            self.__bonds[int(words[0])] = [int(words[1]),
                                           int(words[2]),
                                           int(words[3])]
            
    def parseAngles(self):
        self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        self.__angles = [None, ]
        for i in range(self.__anglesNum):
            self.__angles.append([0, 0, 0, 0])
        for i in range(self.__anglesNum):
            words = self.__f.readline().split()
            self.__angles[int(words[0])] = [int(words[1]),
                                            int(words[2]),
                                            int(words[3]),
                                            int(words[4])]
                                            
    def parseDihedrals(self):
        self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        self.__dihedrals = [None, ]
        for i in range(self.__dihedralsNum):
            self.__dihedrals.append([0, 0, 0, 0, 0])
        for i in range(self.__dihedralsNum):
            words = self.__f.readline().split()
            self.__dihedrals[int(words[0])] = [int(words[1]),
                                               int(words[2]),
                                               int(words[3]),
                                               int(words[4])]
                                               
    def parseImpropers(self):
        self.__f.readline()
        self.__f.readline()
        self.__f.readline()
        self.__impropers = [None, ]
        for i in range(self.__impropersNum):
            self.__impropers.append([0, 0, 0, 0, 0])
        for i in range(self.__dihedralsNum):
            words = self.__f.readline().split()
            self.__impropers[int(words[0])] = [int(words[1]),
                                               int(words[2]),
                                               int(words[3]),
                                               int(words[4]),
                                               int(words[5])]
                                               
    def atoms(self):
        return self.__atoms
        
    def bonds(self):
        return self.__bonds
    
    def angles(self):
        return self.__angles
        
    def dihedrals(self):
        return self.__dihedrals
        
    def impropers(self):
        return self.__impropers
        
    def xlo(self):
        return self.__xlo
        
    def xhi(self):
        return self.__xhi
        
    def ylo(self):
        return self.__ylo
        
    def yhi(self):
        return self.__yhi
    
    def zlo(self):
        return self.__zlo
        
    def zhi(self):
        return self.__zhi
        
    def masses(self):
        return self.__masses