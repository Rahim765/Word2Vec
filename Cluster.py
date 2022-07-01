import math

import numpy as np


class Cluster:
    def __init__(self, data, cTarget, k):
        self.data = data
        self.cTarget = cTarget
        self.N = len(data)
        self.D_original = []
        self.R_k = []
        self.k = k
        self.label = []
        for i in range(self.N):
            self.label.append(i)
        self.g = 10
        self.D_current = []

    def distance(self):
        for i in range(self.N):

            col = []
            # col = np.array(col)
            for j in range(self.N):
                ab = self.data[i] - self.data[j]
                sub = np.linalg.norm(ab)
                col.append(sub)

                # col = np.append(col ,np.subtract( self.data[i], self.data[j]))
            self.D_original.append(col)
        self.D_original = np.array(self.D_original)

    def relation(self):
        for i in range(self.N):
            row = self.D_original[i]

            row = np.delete(row, i)
            col = []
            for k in range(self.k):
                index = np.argmin(row)
                if index >= i:
                    col.append(index + 1)  # self.data[index+1]

                elif index < i:
                    col.append(index)  # self.data[index]

                row = np.delete(row, index)
            self.R_k.append(col)

    def select_seed(self, D, C):
        min = 99999999
        current_seed = 0
        index = 0
        seeds = []
        for i in range(self.N):
            sum = 0
            for j in range(len(D[i])):
                sum = sum + D[i][j]

            if sum < min:
                min = sum
                index = i

        current_seed = current_seed + 1
        seeds.append(index)
        if current_seed == C:
            return  # arr

        while current_seed < C:

            print(current_seed)
            kseeds = []
            for i in range(self.k):
                min = 9999999
                for j in range(self.N):
                    sum = 0
                    for k in range(len(D[j])):
                        sum = sum + D[j][k]

                    if sum < min and (j not in seeds) and (j not in kseeds):
                        min = sum
                        index = j

                kseeds.append(index)

            # print(kseeds)
            max = 0
            for i in range(self.k):
                sum = 0
                for j in range(len(seeds)):
                    sum = sum + D[seeds[j]][kseeds[i]]
                if sum > max:
                    max = i

            seeds.append(kseeds[max])
            current_seed = current_seed + 1
        print("seeds: ")
        print(seeds)
        return seeds

    def dCurrentCalculator(self):
        for i in range(self.N):
            print(i)
            col = []
            for j in range(self.N):
                sum = 0
                for k in range(len(self.R_k[i])):
                    sum2 = 0
                    for p in range(len(self.R_k[j])):
                        sub = self.D_original[self.R_k[i][k]][self.R_k[j][p]]
                        sum2 = sum2 + sub
                    sum = sum + sum2

                sum = (1 / math.pow(self.k + 1, 2)) * sum
                col.append(sum)

            self.D_current.append(col)

        print(self.D_current)

    def clustring(self):
        cPrevious = self.N
        cCurrent = self.N / self.g
        self.dCurrentCalculator()
        while cCurrent >= self.cTarget:
            seed = self.select_seed(self.D_current, cCurrent)
            p_i = []
            p_j = []
            print("CCurrent :")
            print(cCurrent)
            for i in range(self.N):

                if i not in seed:
                    min = 99999999
                    index = 0
                    for j in seed:
                        if self.D_current[self.label[i]][j] < min:
                            min = self.D_current[self.label[i]][j]
                            index = j
                    self.label[i] = index  # self.D_current[self.label[i]][index]

            for i in range(len(seed)):
                print(i)
                for j in range(len(seed)):

                    col = []
                    col2 = []
                    for k in range(len(self.label)):
                        if self.label[k] == seed[i]:
                            col.append(k)
                            for t in range(len(self.R_k[k])):
                                col.append(self.R_k[k][t])
                        if self.label[k] == seed[j]:
                            col2.append(k)
                            for t in range(len(self.R_k[k])):
                                col2.append(self.R_k[k][t])
                    p_i.append(col)
                    p_j.append(col2)

                    sum = 0
                    for k in p_i[i]:
                        for t in p_j[j]:
                            sum = sum + self.D_original[k][t]

                    self.D_current[i][j] = (1 / len(p_i) * len(p_j)) * sum
            cPrevious = cCurrent
            cCurrent = cCurrent / self.g
            if cCurrent < self.cTarget:
                cCurrent = self.cTarget
        mn =[]
        for t in self.label:
            if t not in mn:
                mn.append(t)
        print(self.label)
        print(mn)


    def fit(self):
        print("hi0")
        self.distance()
        print("hi1")

        self.relation()
        print("hi2")

        # self.select_seed(self.D_original, self.cTarget)

        print("hi3")
        self.clustring()
        # self.dCurrentCalculator()
        # print("hi4")

    #
    # def dCurrentCalculator(self):
    #     for i in range(self.N):
    #         print(i)
    #         col = []
    #         for j in range(self.N):
    #             sum = 0
    #             for k in range(len(self.R_k[i])):
    #                 sum2 = 0
    #                 for p in range(len(self.R_k[j])):
    #                     ab = self.R_k[i][k] - self.R_k[j][p]
    #                     sub = np.linalg.norm(ab)
    #                     sum2 = sum2 + sub
    #                 sum = sum + sum2
    #
    #             sum = (1 / math.pow(self.k + 1, 2)) * sum
    #             col.append(sum)
    #
    #         self.D_current.append(col)
    #
    #     print(self.D_current)

    #
    # def select_seed(self):
    #     min = 99999999
    # current_seed = 0
    # index = 0
    # for i in range(self.N):
    #     sum = 0
    #     for j in range(len(self.D_original[i])):
    #         sum = sum + self.D_original[i][j]
    #
    #     if sum < min:
    #         min = sum
    #         index = i
    #
    # current_seed = current_seed + 1
    # self.seeds.append(index)
    # if current_seed == self.cTarget:
    #     return
    #
    # while current_seed < self.cTarget:
    #     print(self.seeds)
    #     kseeds = []
    #     for i in range(self.k):
    #         min = 9999999
    #         for j in range(self.N):
    #             sum = 0
    #             for k in range(len(self.D_original[j])):
    #                 sum = sum + self.D_original[j][k]
    #
    #             if sum < min and (j not in self.seeds) and (j not in kseeds):
    #                 min = sum
    #                 index = j
    #
    #         kseeds.append(index)
    #
    #     print(kseeds)
    #     max = 0
    #     for i in range(self.k):
    #         sum = 0
    #         for j in range(len(self.seeds)):
    #             sum = sum + self.D_original[self.seeds[j]][kseeds[i]]
    #         if sum > max:
    #             max = i
    #
    #     self.seeds.append(kseeds[max])
    #     current_seed = current_seed + 1
    # print("seeds: ")
    # print(self.seeds)
