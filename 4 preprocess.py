import pandas as pd

df = pd.read_csv("processed_reactions.csv", dtype=str)

# 1. Remove reverse reactions
mask_reverse = df["rule"].str.contains("reversed", case=False, na=False)
df_filtered = df[~mask_reverse].copy()

# 2. Find unique reactions
unique_key = "mapped"
unique_reactions = df_filtered.drop_duplicates(subset=[unique_key]).copy()

# 3. Collect UniProt IDs for each unique reaction
reaction_to_uniprot = (
    df_filtered.groupby(unique_key)["protein_refs"]
    .apply(lambda x: sorted({u for lst in x.dropna() for u in eval(lst) if u}))
)

# 4. Collect EC numbers
reaction_to_ec = (
    df_filtered.groupby(unique_key)["ec_num"]
    .apply(lambda x: sorted(set(x.dropna())))
)

# 5. 将 UniProt 和 EC 信息加入 unique_reactions
unique_reactions["uniprot_list"] = unique_reactions[unique_key].map(reaction_to_uniprot)
unique_reactions["ec_list"] = unique_reactions[unique_key].map(reaction_to_ec)

# 6. 保存结果（保持原格式 + 新列）
unique_reactions.to_csv("unique_reactions_with_uniprot_ec.csv", index=False)
