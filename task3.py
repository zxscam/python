class Matrix:
    def __init__(self,mat):
        self.mat = mat

    def __add__(self, other):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                self.mat[i][j] += other.mat[i][j]
        return self.mat

    def __str__(self):
        return str('\n'.join(['\t'.join([str(num) for num in i]) for i in self.mat]))
    
m1 = Matrix([[4,8,1],[9,6,4]])
m2 = Matrix([[3,1,2],[4,9,2]])
m3 = Matrix([[],[]])
m3.mat = m1+m2
print(m3)