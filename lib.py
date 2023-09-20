import pandas as pd
import matplotlib.pyplot as plt

def perform_data_analysis():
  
    url = "https://raw.githubusercontent.com/fivethirtyeight/data &&\
    /master/covid-geography/mmsa-icu-beds.csv"

    
    df = pd.read_csv(url)

    
    total_at_risk_stats = df['total_at_risk'].describe()

    
    print(total_at_risk_stats)

    
    summary_data = pd.DataFrame({
        'Statistic': ['Mean', 'Median', 'Standard Deviation'],
        'Value': [667188.7, 396081.5, 884786.8]
    })

    
    plt.figure(figsize=(8, 6))
    plt.bar(summary_data['Statistic'], 
            summary_data['Value'], color=['blue', 'green', 'red'])
    plt.ylabel('Value')
    plt.title('Summary Statistics for "total_at_risk"')
    plt.show()




if __name__ =="__main__":
  perform_data_analysis()
