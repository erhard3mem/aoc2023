class Line:
    numberStr = ''
    def __init__(self,line):
        for i in range(0,len(line)):
            if len(self.numberStr) == 0:
                try:
                    i = int(line[i])
                    self.numberStr = self.numberStr + str(i)
                    #print(self.numberStr)
                    break
                except:
                    continue
        for i in reversed(range(0,len(line))):
            #print(i)
            if len(self.numberStr) < len(line):
                try:
                    i = int(line[i])
                    self.numberStr = self.numberStr + str(i)
                   # print(self.numberStr)
                    break
                except:
                    continue


sum = 0
f = open("input", "r")

for x in f:                
    l = Line(x)
    #print(l.numberStr)
    #print(sum)

    sum = sum + int(l.numberStr)
    

print(sum)
