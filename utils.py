import pickle
import json
import numpy as np

with open(r"stacic/Model_file/logistic_classification.pkl","rb") as f:
    model = pickle.load(f)

with open(r"stacic/Project_Data/proj_data.json") as f:
    json_data = json.load(f)

def get_flower_species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
    test_array = np.zeros([1,model.n_features_in_])
    test_array[0,0] = SepalLengthCm
    test_array[0,1] = SepalWidthCm
    test_array[0,2] = PetalLengthCm
    test_array[0,3] = PetalWidthCm
    predicted_species = np.around(model.predict(test_array)[0])
    return predicted_species