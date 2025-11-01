import pickle
import os

# Define the relative path to the model file
# This path goes UP from 'App' (../) and then DOWN into 'Model'
MODEL_PATH = "../Model/logistic_regression_model.pkl"

def get_model():
    """
    Loads and returns the trained model from the specified path.
    """
    try:
        # Get the absolute path of the directory this script is in (App/)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Join the base path with the relative model path
        model_file_path = os.path.join(base_dir, MODEL_PATH)
        
        # Normalize the path to fix any '..' issues
        model_file_path = os.path.normpath(model_file_path)

        if not os.path.exists(model_file_path):
            print(f"Error: Model file not found at {model_file_path}")
            return None

        with open(model_file_path, "rb") as file:
            loaded_model = pickle.load(file)
        
        print(f"Model loaded successfully from {model_file_path}")
        return loaded_model

    except Exception as e:
        print(f"Error loading model in connecter.py: {e}")
        return None
