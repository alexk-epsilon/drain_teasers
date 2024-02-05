#Given a string containing numbers, find all possible placements of +-* so that
#resulting expression is equial to a value provided
#Example
#123 6 => [1*2*3, 1+2+3]
#124 8 => [1*2*4, 12-4]
#241 8 => [2*4*1]
from pdb import set_trace as b

def dfs(solutions,current_solution,s,val)->list:
    #print(f"dfs {solutions} {current_solution} {s} {val}")
    L = len(s)
    for i in range(1,L+1):
        solution = current_solution
        num = int(s[0:i])
        solution += str(num)
        if i==L:
            if num == val:
                solutions.append(solution)
        else:
            #try +
            solution_so_far = solution + "+"
            solutions = dfs(solutions,solution_so_far,s[i:],val-num)
            #try -
            solution_so_far = solution + "-"
            solutions = dfs(solutions,solution_so_far,s[i:],num-val)
            #try *
            solution_so_far = solution + "*"
            if num >0 :
                solutions = dfs(solutions,solution_so_far,s[i:],val/num)

    return solutions

def arrange_ops(s,val):
    solutions = []
    current_solution = ""
    return dfs(solutions,current_solution,s,val)

s = "124" 
val = 8
print(arrange_ops(s,val))