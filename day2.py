sumIds = 0
noGame = False
f = open("input4", "r")
for l in f:
    id = int(l.split(':')[0].split('Game')[1])
    print(id)
    game = l.split(':')[1]

    bag = game.split(';')
    for b in bag:
        cubes = b.split(',')
        green = 0;
        red = 0;
        blue = 0;
        for c in cubes:        
            if "green" in c:
                green = int(c.split('green')[0])
            elif "red" in c:
                red = int(c.split('red')[0])
            elif "blue" in c:
                blue = int(c.split('blue')[0])        
        if green > 13 or red > 12 or blue > 14:
            noGame = True        
        print(red,green,blue)
        #print(id)
    if not noGame:
        sumIds = sumIds + id
    noGame = False
    print('=',sumIds)

print(sumIds)
