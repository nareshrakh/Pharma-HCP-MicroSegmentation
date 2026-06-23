import config
import pickle
import json
import pandas as pd
import numpy as np
from src.database import get_data_collection
data_collection = get_data_collection()

class MedicalInsurance():

    def __init__(self):
        pass
        
    def load_model(self):
        """
            This method will be used to load Linear Regresion Model
        """
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)
        return self.model

    def load_json_data(self):
        """
        Docstring for load_json_data
        
        :param self: Description
        """
        with open(config.LABEL_ENCODED_DATA, "r") as f:
            self.column_encoded_data = json.load(f)

        return self.column_encoded_data

    def create_test_df(self):
        self.load_model()
        self.load_json_data()

        test_array = np.zeros((1,self.model.n_features_in_))
        
        test_array[0,0] = self.data['age']
        test_array[0,1] = self.column_encoded_data['gender'][self.data['gender']]
        test_array[0,2] = self.data['bmi']
        test_array[0,3] = self.data['children']
        test_array[0,4] = self.column_encoded_data['smoker'][self.data['smoker']]

        region = f"region_{self.data['region']}"

        region_index = np.where(self.model.feature_names_in_ == region)[0]
        test_array[0,region_index] = 1
        # print("test_array", test_array)
        self.test_df = pd.DataFrame(test_array, columns=self.model.feature_names_in_)

    def predict_charges(self, user_input_data):
        self.data = user_input_data
        self.create_test_df()

        self.prediction = np.around(self.model.predict(self.test_df)[0],4)
        # print("Predicted Price is :",self.prediction )
        return self.prediction
    
    def save_data_in_db(self):
        input_data = dict(self.data)
        input_data.update({"Prediction": self.prediction})
        data_collection.insert_one(input_data)
        return "Successful"
    
    def save_data_in_db_test(self):
        input_data = dict(self.data)
        input_data.update({"Prediction": self.prediction})
        data_collection.insert_one(input_data)
        return "Successful"
