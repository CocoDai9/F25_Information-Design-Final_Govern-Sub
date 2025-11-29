import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# --- DATASET 1: Village Cadres ---
data_cadres = {
    'County Type': ['Interior Counties', 'Interior Counties', 'Border Counties', 'Border Counties'],
    'Role': ['Secretary/Director', 'Other Cadres', 'Secretary/Director', 'Other Cadres'],
    'Compensation (CNY)': [40060, 32048, 44066, 35253]
}
df_cadres = pd.DataFrame(data_cadres)

# --- DATASET 2: Border Residents ---
data_border = {
    'Location': ['Frontline Border', 'General Border'],
    'Subsidy (CNY)': [13800, 6800]
}
df_border = pd.DataFrame(data_border)

# --- DATASET 3: Poverty Living Subsidy ---
data_poverty = {
    'Category': ['Centralized/Urban Dispersed', 'Rural Dispersed'],
    'Subsidy (CNY)': [14778, 8010]
}
df_poverty = pd.DataFrame(data_poverty)

# --- PLOTTING ---
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: Cadres
sns.barplot(x='County Type', y='Compensation (CNY)', hue='Role', data=df_cadres, ax=axes[0], palette='viridis')
axes[0].set_title('2024 Village Cadre Annual Compensation', fontsize=14, fontweight='bold')
axes[0].set_ylim(0, 50000)
for container in axes[0].containers:
    axes[0].bar_label(container, fmt='%d')

# Plot 2: Border Residents
sns.barplot(x='Location', y='Subsidy (CNY)', data=df_border, ax=axes[1], palette='Blues_d')
axes[1].set_title('2024 Border Resident Annual Subsidy', fontsize=14, fontweight='bold')
axes[1].set_ylim(0, 16000)
for container in axes[1].containers:
    axes[1].bar_label(container, fmt='%d')

# Plot 3: Poverty Living Subsidy
sns.barplot(x='Category', y='Subsidy (CNY)', data=df_poverty, ax=axes[2], palette='Reds_d')
axes[2].set_title('2023 Special Poverty Living Subsidy', fontsize=14, fontweight='bold')
axes[2].set_ylim(0, 18000)
for container in axes[2].containers:
    axes[2].bar_label(container, fmt='%d')

plt.tight_layout()
plt.show()
