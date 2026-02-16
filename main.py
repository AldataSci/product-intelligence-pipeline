import pandas as pd
from src.cleaner import clean_review_data
from src.analyzer import process_all_reviews

def run_pipeline():
    """Runs the complete product intelligence pipeline."""
    
    # 1. Load raw data
    print("Loading data...")
    df = pd.read_csv('data/sample_reviews.csv')
    print(f"Loaded {len(df)} reviews\n")
    
    # 2. Clean data
    print("Cleaning data...")
    cleaned_df = clean_review_data(df)
    print(f"Cleaned to {len(cleaned_df)} negative, verified reviews\n")
    
    # 3. Analyze with LLM
    print("Analyzing reviews...")
    insights_df = process_all_reviews(cleaned_df)
    
    # 4. Generate report
    print("\n=== EXECUTIVE SUMMARY ===")
    print(f"Total Issues Found: {len(insights_df)}")
    print(f"High Severity Issues: {len(insights_df[insights_df['severity'] == 'High'])}")
    print(f"\nTop Complaint Categories:")
    print(insights_df['category'].value_counts())
    
    # 5. Save results
    insights_df.to_csv('data/final_insights.csv', index=False)
    print("\n✅ Pipeline complete. Results saved to data/final_insights.csv")

if __name__ == "__main__":
    run_pipeline()
