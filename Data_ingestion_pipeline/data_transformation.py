from src.RestuarantClassification.utils.utils import save_object
from src.RestuarantClassification.exception import Custom_Exception
from Data_ingestion_pipeline.data_ingestion import DataIngestion
import os
import sys

class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    
class  Data_Transformation:
    
