import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import Data_ingestion 
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import argparse 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
import Report_generation 


df= Data_ingestion.ingestion()

def process_query(query):
    """Process the user query to extract key terms."""
    tokens = word_tokenize(query.lower())
    filtered_tokens = [ps.stem(w) for w in tokens if w not in stop_words]
    return filtered_tokens

def generate_report(df):
    """Placeholder function to generate a report."""
    print("Generating report...")
    summary = df.describe().to_string()
    with open('report.txt', 'w') as f:
        f.write(summary)
    print("Report generated and saved as 'report.txt'.")

def create_visualization(df):
    """Placeholder function to create a visualization."""
    print("Creating visualization...")
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.pairplot(df)
    plt.savefig('visualization.png')
    print("Visualization saved as 'visualization.png'.")

def provide_summary(df):
    summary=f"""
    Olympic Games Report:
    
    Total number of countries: {df['Country'].nunique()}
    Average number of medals won: {df['Total'].mean():.2f}
    Country with the most medals: {df.iloc[df['Total'].idxmax()]['Country']}
    """
    print(summary)

def handle_query(query, df):
    """Handle user queries and route them to the appropriate function."""
    tokens = process_query(query)
    
    if "report" in tokens:
        generate_report(df)
    elif "visualization" in tokens or "plot" in tokens:
        create_visualization(df)
    elif "summary" in tokens:
        provide_summary(df)
    else:
        print("Sorry, I didn't understand your query. Please try again.")

def cli():
    """Main function to handle command-line input."""
    parser = argparse.ArgumentParser(description="AI CLI for Data Analysis")
    parser.add_argument('--query', type=str, help="Your query for the AI (e.g., 'Generate a report')")
    args = parser.parse_args()
    
    # Load your dataset here
    df= Data_ingestion.ingestion()
    
    if args.query:
        handle_query(args.query, df)
    else:
        # Prompt for query if not provided via command line
        while True:
            query = input("Enter your query (type 'exit' to quit): ")
            if query.lower() == 'exit':
                break
            handle_query(query, df)

if __name__ == "__main__":
    cli()
