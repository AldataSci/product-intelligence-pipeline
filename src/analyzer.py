import json
import requests
import pandas as pd

def analyze_review_with_llm(review_text, use_real_api=False):
    """
    Analyzes a customer review using an LLM.
    
    Parameters:
    -----------
    review_text : str
        The cleaned review text to analyze
    use_real_api : bool
        If True, calls real LLM API. If False, returns mock data.
    
    Returns:
    --------
    list of dict
        Structured analysis results
    """
    
    prompt = f"""You are a product analyst. Analyze the following customer review and extract key information.

REVIEW:
"{review_text}"

INSTRUCTIONS:
1. Identify the PRIMARY complaint category from this list ONLY:
   - Battery
   - Build Quality
   - Shipping/Delivery
   - UI/UX
   - Overheating
   - Price/Value
   - Customer Service
   - Other

2. Assign a severity level:
   - High: Safety issue, product unusable, or customer demands refund
   - Medium: Product works but has significant flaws
   - Low: Minor annoyance, still usable

3. Write a one-sentence summary for the engineering team (max 15 words).

4. If multiple issues exist, return multiple objects in the list. Prioritize product issues over service issues.

OUTPUT FORMAT (JSON list only, no explanation):
[
  {{
    "category": "CategoryName",
    "severity": "High/Medium/Low",
    "summary": "Brief summary here"
  }}
]
"""
    
    if not use_real_api:
        return [{"category": "Battery", "severity": "High", "summary": "Mock response for testing"}]
    else:
        api_url = "https://routellm.abacus.ai/v1/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY_HERE",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a product analyst."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            api_response = response.json()
            content_string = api_response["choices"][0]["message"]["content"]
            
            return json.loads(content_string)
        
        except Exception as e:
            print(f"API call failed: {e}")
            return [{"category": "Other", "severity": "Low", "summary": "API call failed"}]


def process_all_reviews(df):
    """
    Processes all reviews in a dataframe and extracts insights.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Cleaned review data
    
    Returns:
    --------
    pandas.DataFrame
        Insights with category, severity, and summary for each issue
    """
    all_insights = []
    
    for index, row in df.iterrows():
        text = row['raw_text']
        results = analyze_review_with_llm(text, use_real_api=False)
        all_insights.extend(results)
    
    return pd.DataFrame(all_insights)

