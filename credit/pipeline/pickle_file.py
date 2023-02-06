# Written Code For Pickling That from root dir
import pickle
import os,sys

ROOT_DIR = os.getcwd()
SAVED_DIR_PATH = "saved_models"
SAVED_ZERO_FILE="0"
MODEL_FILE_DIR ="model"
MODEL_FILE_NAME = "model.pkl"
TRANSFORMER_FILE_DIR="transformer"
TRANSFORMER_FILE_NAME="transformer.pkl"
TARGET_ENCODER_FILE_DIR="target_encoder"
TARGET_ENCODER_FILE_NAME="target_encoder.pkl"

MODEL_DIR = os.path.join(ROOT_DIR, SAVED_DIR_PATH,SAVED_ZERO_FILE,MODEL_FILE_DIR,MODEL_FILE_NAME)
print("MODEL_PATH:-",MODEL_DIR)

TRANSFORMER_DIR= os.path.join(ROOT_DIR, SAVED_DIR_PATH,SAVED_ZERO_FILE,TRANSFORMER_FILE_DIR,TRANSFORMER_FILE_NAME)
print("TRANSFORMER_PATH:-",TRANSFORMER_DIR)

TARGET_ENCODER_DIR= os.path.join(ROOT_DIR, SAVED_DIR_PATH,SAVED_ZERO_FILE,TARGET_ENCODER_FILE_DIR,TARGET_ENCODER_FILE_NAME)
print("TARGET_ENCODER_PATH:-",TARGET_ENCODER_DIR)
# Load The Model
model=pickle.load(open(MODEL_DIR,"rb"))
print(model)
transfomer=pickle.load(open(TRANSFORMER_DIR,"rb"))
print(transfomer)
target_encoder=pickle.load(open(TARGET_ENCODER_DIR,'rb'))
print(target_encoder)