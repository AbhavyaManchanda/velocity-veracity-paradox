import pandas as pd

def clean_research_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Handling missing values for critical columns
    df['urgency_level'] = df['urgency_level'].fillna('Low')
    df['belief_alignment_status'] = df['belief_alignment_status'].fillna('Neutral')
    
    # Categorizing accuracy for Betrayal Aversion analysis
    df['is_accurate'] = df['answer_accuracy_percentage'] >= 70
    
    # Binning Verification Duration to observe the Absorption Gap
    df['verification_bin'] = pd.cut(df['verification_duration_mins'], 
                                    bins=[0, 5, 15, 30, 45], 
                                    labels=['0-5m', '5-15m', '15-30m', '30-45m'])
    
    print("Data Cleaning Complete. Dataset shape:", df.shape)
    return df

if __name__ == "__main__":
    df = clean_research_data('../data/ai_skepticism_dataset.csv')
    df.to_csv('../data/cleaned_ai_data.csv', index=False)