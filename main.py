import matplotlib.pyplot as plt
import pandas as pd
import thinkstats2
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

#part 1 hypothesis

data = pd.read_csv("salaries.csv")#we are reading the data from the file we had
year_ID = data[0]
team_ID = data[1]
Ig_ID = data[2]
player_ID = data[3]
Salary = data [4]

h2 = main.test_yearID_Salary((year_ID, Salary))
print np.mean(year_ID)
print np.mean(Salary)
print h2.TestStatistic((year_ID, Salary))
h2.PValue(iters=10000)


#part 2 regression
slope, intercept = np.polyfit(year_ID, Salary, 1)
print "slope: ", slope, "intercept: ", intercept
pointsLine = [intercept + slope * x for x in year_ID]
plt.figure()
plt.plot(year_ID, team_ID, "ro")
plt.plot(year_ID, pointsLine, "--")
plt.show()

residuals = [y - (slope*x + intercept) for x, y in zip(year_ID, Salary)]
res_plt = sorted(zip(year_ID, residuals))
t2 = [x for x,y in res_plt]
r2 = [y for x,y in res_plt]
plt.figure()
plt.plot(t2, r2, 'ro-')
plt.show()

log_teamID= [np.log(x) for x in team_ID]
slope_log, intercept_log = np.polyfit(team_ID, log_teamID, 1)
print "line fit for age and log(teamID)"
print "slope: ", slope_log, "intercept: ", intercept_log
pointsLineLog = [intercept_log + slope_log * x for x in team_ID]
plt.figure()
plt.plot(team_ID, log_teamID, "ro")
plt.plot(team_ID, pointsLineLog, '--')
plt.show()

formula='yearID ~ teamID + salary + IgID'
data_dict = {"yearId":year_ID, "teamID":team_ID, "salary":Salary, "IgID":Ig_ID}
model = smf.poisson(formula, data=data_dict)
model = model.fit()

print "predicted salary for 870000 NL with year of born 1985: ", model.predict({"salary": 8700, "IgID":'NL', "yearID":1985})

print "slope for yearID and salary is: ", slope

print "\n\nMultiple regression model:"
modelMR = smf.ols('salary ~ salary + YearId + IgID', data=data_dict)
modelMR = modelMR.fit()
print modelMR.summary()
modelMR.predict({"salary":8700, "yearID":1985, "IgID":'NL'})
