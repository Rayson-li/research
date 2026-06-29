import pandas as pd
import json

df = pd.read_csv("processed_reactions.csv")

with open("1.json", "r", encoding="utf-8") as f:
    mcsa = json.load(f)

def ec_from_solution_step(step, mcsa):
    entry_id = int(step.split('_')[0])  # 提取 69

    for entry in mcsa["results"]:       # ← 必须从 results 里找
        if entry.get("mcsa_id") == entry_id:
            return entry["reaction"]["ec"]   # ← EC 在 reaction.ec 里

    return None


def get_ec_from_desired(desired_reaction, df):
    row = df[df["unmapped"] == desired_reaction]
    if len(row) == 0:
        return None
    return row.iloc[0]["ec_num"]



solution = ['69_1_1', '69_1_2']
desired_reaction = "CCCCCCCCCCCCCC(=O)SCCNC(=O)CCNC(=O)[C@H](O)C(C)(C)COP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1OP(=O)(O)O.C[N+](C)(C)C[C@H](O)CC(=O)O>>CC(C)(COP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1OP(=O)(O)O)[C@@H](O)C(=O)NCCC(=O)NCCS.CCCCCCCCCCCCCC(=O)O[C@H](CC(=O)O)C[N+](C)(C)C"

ec_mech = ec_from_solution_step(solution[0], mcsa)
ec_true = get_ec_from_desired(desired_reaction, df)

print("EC from mechanism:", ec_mech)
print("EC from desired reaction:", ec_true)
