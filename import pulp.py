import pulp

# Create the problem variable
prob = pulp.LpProblem("Weekend Assignment", pulp.LpMaximize)

# Create the decision variables
x = pulp.LpVariable.dicts("person_weekend", [(i, j) for i in range(11) for j in range(52)], cat="Binary")

# Add the capacity constraints
for j in range(52):
    prob += pulp.lpSum(x[(i, j)] for i in range(11)) == 5

# Add the work frequency constraints
for i in range(11):
    prob += pulp.lpSum(x[(i, j)] for j in range(0, 52, 2)) == 26

# Add the objective function
prob += pulp.lpSum(x)

# Solve the problem
prob.solve()

# Print the solution
for i in range(11):
    for j in range(52):
        if pulp.value(x[(i, j)]) == 1:
            print(f"Person {i+1} works on weekend {j+1}")
