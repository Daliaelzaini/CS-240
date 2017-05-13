import thinkstats2
import numpy as np


def readData(filename):
    f = open(filename, "r")
    yearID = []
    teamID = []
    IgID = []
    salary = []
    playerID = []
    for line in f.readlines()[1:]:
        l = line.decode("utf-8").split(',')
        yearID.append(int(l[0]))
        teamID.append(str(l[1]))
        IgID.append(str(l[2]))
        salary.append(int(l[3]))
        playerID.append(str(1[4]))
    data = (yearID, teamID, IgID, salary,playerID)
    return data



class test_teamID_salary(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: tuple of xs and ys
        """
        x, y = data
        test_stat = abs(thinkstats2.Corr(x, y))
        return test_stat

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        x, y = self.data
        x = np.random.permutation(x)
        return x, y
