import sys
import os
sys.path.append(os.getcwd())

from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    logging.info("Application started")

    # 🔹 Step 1: Data Ingestion
    data_ingestion = DataIngestion()
    train_path, test_path = data_ingestion.initiate_data_ingestion()

    logging.info(f"Data ingestion completed: {train_path}, {test_path}")

    # 🔹 Step 2: Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
        train_path,
        test_path
    )

    logging.info("Data transformation completed")

    # 🔹 Step 3: Model Training
    model_trainer = ModelTrainer()
    score = model_trainer.initiate_model_trainer(train_arr, test_arr)

    logging.info(f"Model training completed. Score: {score}")

    print("Pipeline executed successfully")