import pandas as  pd
import numpy as np
from RestuarantClassification.logger import logging
from RestuarantClassification.exception import Custom_Exception
import sys
import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

raw_data = pd.read_csv(r"C:/Users/Krishna.Arjun/Desktop/Krish/iNeuron/Practice work/RestaurantProject/notebooks/data/restuarant.csv")



class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw_data.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","restuarant.csv")))
            logging.info(" i have read dataset as a df")
            
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            return (
                 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise Custom_Exception(e,sys)           
        





