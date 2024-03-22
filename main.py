import cvxpy as cv

t = 2/3
x = cv.Variable(1)
prob = cv.Problem(objective=cv.Maximize(cv.log(x) + cv.log(1 - t * x)), constraints=[x <= 1, x >= 0])
prob.solve(solver=cv.ECOS)
print("Status: ", prob.status)
print(("Optimal value: ", prob.value))
print("Optimal var: ", x.value)
