import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# Dummy logging (for now)
import logging
logging.basicConfig(level=logging.INFO)

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        print("INGESTION STARTED")

        try:
            # Load CSV
            df = pd.read_csv('notebook/data/stud.csv')
            print("CSV LOADED")

            # Create artifacts folder
            os.makedirs("artifacts", exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            # Split data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train & test
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            print("ARTIFACT CREATED SUCCESSFULLY")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            print("ERROR:", e)