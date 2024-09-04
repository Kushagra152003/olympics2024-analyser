import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import Data_ingestion 
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error

df= Data_ingestion.ingestion()

def descriptional_analysis():
    print(df.describe())

def Clustering_analysis():
    X = df[['Gold', 'Silver', 'Bronze']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)
    plt.scatter(df['Gold'], df['Silver'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('Gold Medals')
    plt.ylabel('Silver Medals')
    plt.title('K-Means Clustering of Countries Based on Medals')
    plt.savefig(r'C:\Users\Hp\Desktop\file\.venv\clustering_analysis.png')
    plt.close()


def Regression_analysis():
    X = df[['Gold', 'Silver', 'Bronze']]
    y = df['Total']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    model_score = model.score(X_test, y_test)

    print(f'{mae},is the mean squared error and , {model_score}, is the model score')

def pairplot():
    sns.pairplot(df, vars=['Gold', 'Silver', 'Bronze'], hue='Total',diag_kind="kde")
    plt.savefig(r'C:\Users\Hp\Desktop\file\.venv\pairplot.png')
    plt.close()

descriptional_analysis()
Clustering_analysis()
Regression_analysis()
pairplot()