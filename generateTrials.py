

def repTrails(numberBlock, LeftRight, numberTask):
    for x in range(1, numberBlock + 1):
        for y in range(3):
            if y < 2:
                for l in LeftRight:
                    a = ''.join([str(x), ',','Mask',',',l])
                    print a
            else:
                for l in LeftRight:
                    a = ''.join([str(x), ',','NonMask',',',l])
                    print a


repTrails(5, ['right', 'left'], 6)
            
        