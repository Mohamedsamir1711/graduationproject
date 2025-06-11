import pickle
import os
from django.conf import settings

# Define the path to your model file
MODEL_PATH = os.path.join(settings.BASE_DIR, 'show_reports', 'random_forest_model.pkl')

# Load the model once at startup
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)
