import pandas as pd

def clean_review_data(df):
    """
    Cleans raw review data for analysis.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Raw review data with columns: review_id, raw_text, rating, verified
    
    Returns:
    --------
    pandas.DataFrame
        Cleaned data ready for LLM processing
    
    Business Logic:
    ---------------
    - Keeps only verified purchases (reduces bot/fake reviews)
    - Removes HTML tags
    - Converts to lowercase
    - Filters for negative reviews (rating < 4)
    """
    df_cleaned = df.copy()
    
    # Filter for verified purchases only
    df_cleaned = df_cleaned[df_cleaned['verified'] == True]
    
    # Clean text: remove HTML tags and convert to lowercase
    df_cleaned['raw_text'] = (df_cleaned['raw_text']
                               .str.replace(r'<[^<>]*>', '', regex=True)
                               .str.lower()
                               .str.strip())
    
    # Filter for negative reviews (rating < 4)
    df_cleaned = df_cleaned[df_cleaned['rating'] < 4]
    
    return df_cleaned
