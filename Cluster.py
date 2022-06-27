import numpy as np

class Cluster:
    def __init__(self , data , cTarget , k):
        self.data = data
        self.cTarget  = cTarget
        self.N = len(data)
        self.D_original =[]
        self.R_k = []
        self.k = k
        self.label = []
        for i in range(self.N):
            self.label.append(i)


    def distance(self):
        for i in range(self.N):
            print(i)
            # if i%500==0:
            col = []
            # col = np.array(col)
            for j in range(self.N):

                sub = np.subtract(self.data[i] , self.data[j])
                average=0
                for t in sub:
                    if t<0:
                        t = -t
                    average = average+t
                col.append(average/100)

                # col = np.append(col ,np.subtract( self.data[i], self.data[j]))
            self.D_original.append(col)
        self.D_original = np.array(self.D_original)
        print(self.D_original)


    def relation(self):
        for i in range(self.N):
            row = self.D_original[i]
            row.sort()
            col =[]
            counter =0
            itr =0
            while counter < self.k:
                if itr != i :
                    col.append(row[itr])
                    counter = counter +1
                itr = itr+1
            self.R_k.append(col)
        print(self.R_k[0])
        print(len(self.R_k[5]))
        print(len(self.R_k[100]))
        print(self.R_k[990])
        print(len(self.R_k[990]))


    def select_seed(self):
        min = self.D_original[0][6]
        print(min)
        current_seed = 0
        seeds = []
        index = 0
        for i in range(self.N):
            sum =0
            for j in range(len(self.D_original[i])):
                sum= sum + self.D_original[i][j]

            c = np.greater(min , sum)
            t=0
            f=0
            for i in c:
                if i == True:
                    t= t+1
                else:
                    f=f+1
            # print("t : ")
            # print(t)
            # print("f : ")
            # print(f)
            # print(" ")
            #
            if np.greater(min.any() , sum.any()):
                print("min: ")
                print(min)
                print("sum : ")
                print(sum)
                min = sum
                index = i

        current_seed = current_seed+1
        seeds.append(self.data[index])
        if current_seed == self.cTarget:
            return


        while current_seed < self.cTarget :
            kseeds = []
            for i in range(self.k):
                min = 9999999;
                for j in range(self.N):
                    sum =0;
                    for k in range(len(self.D_original[j])):
                        sum= sum + self.D_original[j][k]
                    if sum < min & seeds.__contains__(self.data[j]) == False & kseeds.__contains__(self.data[j]) == False:
                        min = sum
                        index = j


                kseeds.append(self.data[index])

            max = 0
            for i in range(self.k):
                if kseeds[i] > max:
                    max = i

            seeds.append(kseeds[max])
            current_seed = current_seed+1;







    def fit(self):
        print("hi0")
        self.distance()
        print("hi1")

        self.relation()
        print("hi2")

        self.select_seed()
        print("hi3")




