

def pythagorean():
    
    control = False
    
    for i in range(1,1000):
        for j in range(1,1000-i):

            c = ((i**2)+(j**2))**0.5
            if c + i + j == 1000:
                control = True
                print(i*j*c)

        if control :
            break

pythagorean()