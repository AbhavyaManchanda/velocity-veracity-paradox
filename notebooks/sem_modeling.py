import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def run_sem_analysis(file_path):
    df = pd.read_csv(file_path)
    
    # Selecting features for the Trust Model
    X = df[['answer_accuracy_percentage', 'verification_duration_mins', 'has_cited_sources']].copy()
    X['has_cited_sources'] = X['has_cited_sources'].astype(int)
    y = df['trust_score_out_of_10']

    # Standardizing to get Beta (Path) Coefficients
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    # Mapping Path Coefficients
    paths = {
        'Accuracy -> Trust': model.coef_[0],
        'Verification (Velocity) -> Trust': model.coef_[1],
        'Transparency (Citations) -> Trust': model.coef_[2]
    }
    
    # Plotting Path Strengths
    plt.figure(figsize=(10, 6))
    colors = ['green' if v > 0 else 'red' for v in paths.values()]
    sns.barplot(x=list(paths.values()), y=list(paths.keys()), palette=colors)
    plt.axvline(0, color='black', lw=1)
    plt.title('SEM Path Coefficients (Paradox Validation)')
    plt.savefig('../visuals/sem_path_coeffs.png')
    
    return paths

if __name__ == "__main__":
    results = run_sem_analysis('../data/cleaned_ai_data.csv')
    for path, beta in results.items():
        print(f"Path: {path} | Beta: {beta:.2f}")