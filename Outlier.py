# Outlier treatment refers to the process of identifying and handling outliers in a dataset.
def remove_outlier(dataset, series):
    # original_dataset_shape = dataset.shape
    Q1 = dataset[series].quantile(0.25)
    Q3 = dataset[series].quantile(0.75)
    IQR = Q3 - Q1 
    lower_limit = Q1 - 1.5*IQR
    upper_limit = Q3 + 1.5*IQR
    # print(f"Q1 : {round(Q1,2)}\t Q3 : {round(Q3,2)} \t IQR : {round(IQR,2)}")
    # print(f"Lower Limit : {round(lower_limit,4)} \t Upper Limit : {round(upper_limit,4)}")
    # print(f"\n\nOriginal Dataset Shape : {original_dataset_shape}\n After Removing Outliear Dataset Shape : {dataset[(dataset[series]>lower_limit)&(dataset[series]<upper_limit)].shape}")
    return dataset[(dataset[series]>lower_limit)&(dataset[series]<upper_limit)]
