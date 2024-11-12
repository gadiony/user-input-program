import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from datetime import datetime, timedelta

def load_and_prepare_data():
    """Load the Iris dataset and add a fake timestamp column for time series analysis"""
    try:
        # Load iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Add a fake timestamp column for time series demonstration
        base = datetime.now() - timedelta(days=150)
        timestamps = [base + timedelta(days=x) for x in range(150)]
        df['timestamp'] = timestamps
        
        # Add some random missing values for demonstration
        df.loc[np.random.choice(df.index, 10), 'sepal length (cm)'] = np.nan
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def explore_and_clean_data(df):
    """Explore and clean the dataset"""
    print("\n=== Data Exploration ===")
    print("\nFirst few rows:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Clean missing values
    df = df.fillna(df.mean())
    
    return df

def perform_basic_analysis(df):
    """Perform basic statistical analysis"""
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    print("\nMean values by species:")
    print(df.groupby('species').mean().round(2))
    
    return df

def create_visualizations(df):
    """Create various visualizations"""
    # Set up the plotting style
    plt.style.use('seaborn')
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(15, 12))
    
    # 1. Line chart - Time series of sepal length
    plt.subplot(2, 2, 1)
    plt.plot(df['timestamp'], df['sepal length (cm)'], linewidth=2)
    plt.title('Sepal Length Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sepal Length (cm)')
    plt.xticks(rotation=45)
    
    # 2. Bar chart - Average measurements by species
    plt.subplot(2, 2, 2)
    species_means = df.groupby('species')['petal length (cm)'].mean()
    species_means.plot(kind='bar')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    
    # 3. Histogram - Distribution of sepal width
    plt.subplot(2, 2, 3)
    plt.hist(df['sepal width (cm)'], bins=20, edgecolor='black')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter plot - Sepal length vs Petal length
    plt.subplot(2, 2, 4)
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.scatter(subset['sepal length (cm)'], 
                   subset['petal length (cm)'], 
                   label=species)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    
    plt.tight_layout()
    return fig

def main():
    """Main function to run the analysis"""
    # Task 1: Load and Explore the Dataset
    df = load_and_prepare_data()
    if df is None:
        return
    
    # Clean and explore the data
    df = explore_and_clean_data(df)
    
    # Task 2: Basic Data Analysis
    df = perform_basic_analysis(df)
    
    # Task 3: Data Visualization
    fig = create_visualizations(df)
    plt.show()
    
    print("\n=== Analysis Complete ===")
    print("\nKey Findings:")
    print("1. The Iris dataset contains measurements of sepals and petals for three species")
    print("2. There are clear differences in petal length between species")
    print("3. Sepal width shows a roughly normal distribution")
    print("4. There is a positive correlation between sepal length and petal length")

if __name__ == "__main__":
    main()