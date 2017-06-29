import numpy

matrixA = []
matrixB = []
for i in open("matrixA.txt"):
    row = [int(x) for x in i.split(',')]
    if len(row) > 0:
        matrixA.append(row)


for i in open("matrixB.txt"):
    row = [int(x) for x in i.split(',')]
    if len(row) > 0:
        matrixB.append(row)

matrixA = numpy.matrix(matrixA)
print matrixA.shape
matrixB = numpy.matrix(matrixB)
print matrixB.shape

ans = numpy.dot(matrixA,matrixB);
print ans.shape

numpy.savetxt('Q1_ans.txt',ans,fmt='%d',delimiter='\n')

