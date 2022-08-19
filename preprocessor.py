import pandas as pd
df= pd.read_csv("C:/Users/Neha Rahi/athlete_events.csv")
region_df= pd.read_csv("C:/Users/Neha Rahi/Downloads/noc_regions.csv")

def preprocess(df,region_df):
    df= df[df['Season'] == 'Summer']
    df= df.merge(region_df,on= 'NOC',how= 'left')
    df.drop_duplicates(inplace=True)
    #one hot encoding
    df= pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df




