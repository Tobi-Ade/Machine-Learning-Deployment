#importing necessary libraries
import pandas as pd 
import numpy as np 
import seaborn as sns 
import pickle
import matplotlib.pyplot as plt
import warnings
import xgboost as xgb
from xgboost import DMatrix
from scipy.stats import chi2_contingency
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
warnings.filterwarnings("ignore")

#reading the data
print("parsing data...")
try:
    data  = pd.read_csv("data/Cleaned_Consumer_Complaints.csv")
    print("Data Successfuly Loaded!")
except Exception as error:
    print(error)

print("Preprocessing the Data...")
#Data Preparation
df = data.copy()
df['Date_sent_to_company'] = pd.to_datetime(df['Date_sent_to_company'])
df['Year'] = df['Date_sent_to_company'].dt.year

#encoding 
df['Consumer_disputed?'] = df['Consumer_disputed?'].replace({"Yes": 1, "No": 0})
df['Timely_response?'] = df['Timely_response?'].replace({"Yes": 1, "No": 0})


#dropping columns 
df.drop(columns=["ZIP_code", "Date_sent_to_company", "Company", "State"], inplace=True)
df.columns = df.columns.str.strip('?')

categorical = [col for col in df.columns if df[col].dtype != 'int64']
numerical = [col for col in df.columns if df[col].dtype == 'int64']
numerical.remove("Consumer_disputed")


#Splitting the data
features, target = (df[categorical + numerical], df['Consumer_disputed'])
df_full_train, df_test, y_full_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
df_train, df_val, y_train, y_val = train_test_split(df_full_train, y_full_train, test_size=0.25, random_state=42)


# Handling Class Imbalance 

#instantiating a class of random oversampler
oversampler = RandomOverSampler(random_state=1)

#creating oversampled training and testing sets
df_train, y_train = oversampler.fit_resample(df_train, y_train)

print("Data Transformation in progress...")
#Transforming Data splits with one hot encoding 
train_dict = df_train.to_dict(orient="records")
dv = DictVectorizer()
X_train = dv.fit_transform(train_dict)

val_dict = df_val[categorical + numerical].to_dict(orient="records")
X_val = dv.transform(val_dict)

print("Transformation Complete!")


print("Training the Model...")
# XGBOOST
#storing features in a dmatrix
dmatrix = DMatrix
dtrain = dmatrix(X_train, label=y_train, feature_names= dv.feature_names_)
dval = dmatrix(X_val, feature_names= dv.feature_names_)

#specifying parameters 
xgb_params = {
    'learning_rate': 0.1,
    'max_depth': 9
}

xgb_model = xgb.train(xgb_params, dtrain)

print("Training Succesful")


print("Loading Prediction Score...")
y_pred_xgb = xgb_model.predict(dval)

score = roc_auc_score(y_val, y_pred_xgb)

print(f"{score:.2f}")


model_file = "model_file_v1.bin"

with open(model_file, "wb") as output_file:
    pickle.dump((xgb_model, dv, dmatrix), output_file)