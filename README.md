# Automated Product Intelligence Pipeline

## 🎯 Business Impact
This project automates the extraction of actionable insights from thousands of unstructured customer reviews. By using LLMs to categorize defects and assess severity, it enables Engineering and Product teams to prioritize high-ROI fixes and reduce customer churn.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Engineering:** Pandas (Cleaning, Filtering, Regex)
- **AI:** LLM Integration (Prompt Engineering, JSON-Schema Enforcement)
- **Architecture:** Modular Pipeline Design

## 🚀 Key Features
- **Data Quality Layer:** Automated filtering for verified purchases and regex-based HTML noise removal.
- **Structured AI Extraction:** Engineered prompts that force LLMs to return 100% parseable JSON objects for downstream analytics.
- **Production-Ready Workflow:** Implemented batch processing with error handling and API mocking for cost-effective development.
- **Executive Reporting:** Automated summary generation highlighting top complaint categories and high-severity issues.

## 📂 Project Structure
- `src/cleaner.py`: Data preprocessing and business logic filtering.
- `src/analyzer.py`: LLM integration and structured data extraction.
- `main.py`: Orchestration script for the end-to-end pipeline.
- `data/`: Sample raw datasets and generated insights.

## 🚦 Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run the pipeline: `python main.py`
