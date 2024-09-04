import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import Data_ingestion 
from analysis_implementation import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
df= Data_ingestion.ingestion()
def visualizations():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Country', y='Total', data=df.sort_values('Total', ascending=False).head(10))
    plt.title('Top 10 Countries by Total Medals')
    plt.xticks(rotation=90)
    plt.savefig('top_countries_medals.png')
    plt.close()



    

def report(df, file_name=r'C:\Users\Hp\Desktop\file\.venv\olympics_report.pdf'):
    visualizations()
    Clustering_analysis()
    pairplot()
    regression_text = str(Regression_analysis())
    summary = f"""
    Olympic Games Report:
    
    Total number of countries: {df['Country'].nunique()}
    Average number of medals won: {df['Total'].mean():.2f}
    Country with the most medals: {df.iloc[df['Total'].idxmax()]['Country']}
    """
    
    
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, "Olympic Games Analysis Report")

    c.setFont("Helvetica", 12)
    text = c.beginText(100, height - 150)
    text.textLines(summary)
    text.textLines(regression_text)
    c.drawText(text)
    
    c.drawImage(r'C:\Users\Hp\Desktop\file\.venv\top_countries_medals.png', 100, height - 400, width=400, height=250)
    c.drawImage(r'C:\Users\Hp\Desktop\file\.venv\clustering_analysis.png', 100, height - 700, width=400, height=250)
    c.drawImage(r'C:\Users\Hp\Desktop\file\.venv\pairplot.png', 100, height - 1000, width=400, height=250)
    c.save()
    print(f"Report generated and saved as {file_name}")


report(df)