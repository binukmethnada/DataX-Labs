import pandas as pd

#read the csv file containing the sample data
sampleData = pd.read_csv("sales_data_sample.csv",encoding="latin1")

print(sampleData)
print()

#cleaning up the column names
sampleData.columns = (sampleData.columns.str.lower().str.strip().str.replace(" ", "_"))

#check for missing values
print(f"Missing Values Found : \n{sampleData.isnull().sum()}")

#handle missing values
sampleData["addressline2"] = sampleData["addressline2"].fillna("Not Included")
sampleData["state"] = sampleData["state"].fillna("Not Included")
sampleData["postalcode"] = sampleData["postalcode"].fillna("Not Included")
sampleData["territory"] = sampleData["territory"].fillna("Not Included")

#remove  duplicates
sampleData.drop_duplicates(inplace=True)

#Standardize text
sampleData["country"] = sampleData["country"].str.strip().str.title()
sampleData["city"] = sampleData["city"].str.strip().str.title()
sampleData["customername"] = sampleData["customername"].str.strip().str.title()

#convert date to proper format
sampleData["orderdate"] = pd.to_datetime(sampleData["orderdate"])

#check and correct the data types
#no invalid data types have been imputed

#Save to a new csv
sampleData.to_csv("cleaned_sales_data_sample.csv",index=False)
print("\nSaved cleaned sales data into cleaned_sales_data_sample.csv")

