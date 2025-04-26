from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= 1200) 
solver.Add(swordsmen*20 + bowmen*10 <= 800)                 
solver.Add(bowmen*40 + horsemen*100 <= 600)                 