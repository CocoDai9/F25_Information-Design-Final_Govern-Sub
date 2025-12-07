import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

# Configuration
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['figure.dpi'] = 150

# --- DATA PREP ---
df_cadres = pd.DataFrame({
    'Region': ['Interior', 'Interior', 'Border', 'Border'],
    'Role': ['Director', 'Staff', 'Director', 'Staff'],
    'Salary': [40060, 32048, 44066, 35253]
})

df_border = pd.DataFrame({
    'Type': ['Frontline Village', 'General Village'],
    'Subsidy': [13800, 6800]
})

df_welfare = pd.DataFrame({
    'Type': ['Centralized', 'Dispersed'],
    'Amount': [14778, 8010]
})

# --- LAYOUT SETUP (Logical Categorization) ---
fig = plt.figure(figsize=(15, 10))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1])

# Colors
c_strong = '#1b5e20'
c_med = '#43a047'
c_light = '#a5d6a7'

# --- CHART 1: Job Performance (Top Left) ---
ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(data=df_cadres, x='Region', y='Salary', hue='Role', 
            palette=[c_strong, c_light], ax=ax1, edgecolor=c_strong)
ax1.set_title("Category I: Job Performance\n(Village Cadre Compensation)", 
              loc='left', fontsize=12, fontweight='bold', color=c_strong)
ax1.set_ylabel("Annual Salary (CNY)")
ax1.grid(axis='y', linestyle='--', alpha=0.3)
for container in ax1.containers:
    ax1.bar_label(container, fmt='%d', padding=3)

# --- CHART 2: Strategic Location (Top Right) ---
ax2 = fig.add_subplot(gs[0, 1])
sns.barplot(data=df_border, x='Type', y='Subsidy', 
            palette=[c_strong, c_med], ax=ax2)
ax2.set_title("Category II: Strategic Location\n(Border Resident Subsidy)", 
              loc='left', fontsize=12, fontweight='bold', color=c_strong)
ax2.set_ylabel("Annual Subsidy (CNY)")
ax2.grid(axis='y', linestyle='--', alpha=0.3)
for container in ax2.containers:
    ax2.bar_label(container, fmt='%d', padding=3)

# --- CHART 3: Social Safety Net (Bottom Full Width) ---
ax3 = fig.add_subplot(gs[1, :])
# Combining Poverty and Nursing (Visual representation of Nursing rate)
bars = sns.barplot(data=df_welfare, x='Type', y='Amount', 
            palette=[c_med, c_light], ax=ax3, width=0.4)
ax3.set_title("Category III: Social Safety Net\n(Poverty Alleviation Standards)", 
              loc='left', fontsize=12, fontweight='bold', color=c_strong)
ax3.set_ylabel("Standard (CNY/Year)")
ax3.grid(axis='y', linestyle='--', alpha=0.3)
ax3.bar_label(bars.containers[0], fmt='%d', padding=3)

# Add text annotation for Nursing logic to make it a complete view
text_str = (
    "NURSING CARE LOGIC (Add-on):\n"
    "• Dispersed (Home): 10-50% of Monthly Min Wage\n"
    "• Centralized (Inst): 10-15% of Annual Living Std"
)
ax3.text(0.5, 0.5, text_str, transform=ax3.transAxes, 
         bbox=dict(facecolor='#f1f8e9', edgecolor=c_strong, boxstyle='round,pad=1'),
         ha='left', va='center', fontsize=10)

plt.subplots_adjust(hspace=0.4, wspace=0.3)
plt.suptitle("2024 Policy Benefits Structure: Categorized View", fontsize=16, y=0.95)

plt.show()