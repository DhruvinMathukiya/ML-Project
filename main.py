import sys
import os
from src.logger import logging
sys.path.append(os.getcwd())

from src.components.data_ingestion import DataIngestion
logging.info("TEST LOG FILE")
if __name__ == "__main__":
    print("MAIN STARTED")

    obj = DataIngestion()
    obj.initiate_data_ingestion()

from src.logger import logging
from src.components.data_transformation import DataTransformation

logging.info("Starting application")

obj = DataTransformation()

logging.info("Created DataTransformation object")

data_transformation = DataTransformation()

train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
    train_path="artifacts/train.csv",
    test_path="artifacts/test.csv"
)

from src.components.model_trainer import ModelTrainer

logging.info("Starting model training")

model_trainer = ModelTrainer()

score = model_trainer.initiate_model_trainer(train_arr, test_arr)

logging.info(f"Model training completed. Score: {score}")