from copy import deepcopy
import matplotlib.pyplot as plt
class Cube:
    '''
    Simple implementation of Menger sponge iterator
    https://en.wikipedia.org/wiki/Menger_sponge
    '''
    def __init__(self):
        self.speed=3
        self.previous=[[1]]
        self.current_dimension=1

    def __iter__(self):
        return self


    def __next__(self):
        b_previous=[]
        for i in range(self.current_dimension):
            b_previous.append(self.previous[i]*self.speed)

        for i in range(self.current_dimension):
            temp_arr=deepcopy(self.previous[i])
            temp_arr.extend([0]*self.current_dimension)
            temp_arr.extend(self.previous[i])
            b_previous.append(temp_arr)

        for i in range(self.current_dimension):
            b_previous.append(self.previous[i]*self.speed)
        self.current_dimension*=self.speed
        self.previous=b_previous
        return self.previous



def plot_data(cube):
    x=[]
    y=[]
    for row in range(len(cube)):
        for column in range(len(cube[row])):
            if(cube[row][column]==1):
                x.append(row)
                y.append(column)
    plt.plot(x,y,'bo')
    plt.show()
    plt.clf()




gadmo=Cube()
for iteration in gadmo:
    plot_data(iteration)


