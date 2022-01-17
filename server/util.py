import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def load_saved_artifactes():  
     print("Loading artifacts")
     global __data_columns
     global __locations
     global __model
     with open("C:/CHP/server/artifacts/column.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[4:]
     if __model is None:
        with open("C:/CHP/server/artifacts/chennai_prediction_model.pickle",'rb') as f:
             __model=pickle.load(f)
     print("Loading artifactes done") 



def get_estimated_price(location,area,bhk,bath,age):
    try:
         loc_ind=__data_columns.index(location.lower())
    except:
         loc_ind=-1
    p=np.zeros(len(__data_columns))
    p[0]=area
    p[1]=bhk
    p[2]=bath
    p[3]=age
    if(loc_ind>=0):
        p[loc_ind]=1
    return round( __model.predict([p])[0],2)



def get_location_names():
    return __locations  
def get_data_columns():
    return __data_columns 
if __name__=='__main__':
    load_saved_artifactes()
    print(get_estimated_price('sembakkam',1000,3,3,2))
    print(get_estimated_price('rajakilpakkam',1200,3,2,2))
    print(get_estimated_price('adyar',1000,1,1,1))