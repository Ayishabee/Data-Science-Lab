import numpy
def scalingMatrix(sx=0, sy=0):
    return numpy.matrix([[sx,0,0],
                         [0,sy,0],
                         [0,0,1]])
matrix=scalingMatrix(2,2)
print(matrix)

def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, -s, 0],
                         [s, c, 0],
                         [0,0, 1]])
matrix=rotationMatrix(30)
print(matrix)

def scalingMatrix(sx=0, sy=0):
    return numpy.matrix([[sx,0,0],
                         [0,sy,0],
                         [0,0,1]])
matrix=scalingMatrix(2,2)
print(matrix)
