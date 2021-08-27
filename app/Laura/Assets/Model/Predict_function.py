import pickle
import pandas as pd
import numpy as np
X = pd.read_csv("X.csv",sep=',')
def predict_price(location,sqft,bath,bhk):
    pickle_in = open("Laura_Linear_model.pickle","rb")
    Laura = pickle.load(pickle_in)
    loc_index = np.where(X.columns==location)[0][0]
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
        
    return Laura.predict([x])[0]

print(predict_price('Devarachikkanahalli',1250,2,2))
