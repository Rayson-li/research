import pandas as pd
from MechFind import MechFind


df = pd.read_csv("processed_reactions.csv")

rxn = df.loc[0, "mapped"]

print("正在运行第一条 mapped 反应：")
print(rxn)

# 执行 MechFind
solutions = MechFind(
    desired_reaction = 'CC(=O)SCC.[OH2:1].[NH3+]CC>>CC(=O)NCC.SCC.[OH3+:1]',
    radius = 1,
    max_steps = 20,
    iterations = 5,
    time_limit = 60
)

print("\n机制结果：")
print(solutions)
