import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            obj=DataIngestion()
            train_data,test_data=obj.initiate_data_ingestion()

            data_transformation=DataTransformation()
            train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

            modeltrainer=ModelTrainer()
            print(f"R-squared on testing sample is {modeltrainer.initiate_model_trainer(train_arr,test_arr) * 100:.2f}%")
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    trainpipeline = TrainPipeline()
    trainpipeline.train()