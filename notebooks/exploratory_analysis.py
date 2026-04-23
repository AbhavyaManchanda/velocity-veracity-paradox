import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('../data/cleaned_ai_data.csv')
sns.set_theme(style="whitegrid")

# Analysis 1: Betrayal Aversion Evidence
def plot_betrayal_aversion(df):
    inaccurate_df = df[df['is_accurate'] == False].copy()
    order = ['Low', 'Medium', 'High', 'Critical']
    inaccurate_df['decision_importance'] = pd.Categorical(inaccurate_df['decision_importance'], categories=order, ordered=True)
    
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=inaccurate_df, x='decision_importance', y='trust_score_out_of_10', color='darkred')
    plt.title('Betrayal Aversion: Trust Collapse in High-Stakes Errors')
    plt.savefig('../visuals/betrayal_aversion.png')
    plt.close()

# Analysis 2: The Absorption Gap
def plot_absorption_gap(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='user_skepticism_category', y='verification_duration_mins', palette='Blues')
    plt.title('Organizational Absorption Gap: Verification Latency')
    plt.savefig('../visuals/absorption_gap.png')
    plt.close()

if __name__ == "__main__":
    plot_betrayal_aversion(df)
    plot_absorption_gap(df)
    print("EDA Visuals generated in /visuals folder.")