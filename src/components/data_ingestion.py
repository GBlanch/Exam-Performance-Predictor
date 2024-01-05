import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# decorator for holding solely data objects
@dataclass
class DataIngestionConfig:

    # store them here:
    train_data_path: str = os.path.join('artifacts',
                                        'train.csv')
    test_data_path: str = os.path.join('artifacts',
                                       'test.csv')
    raw_data_path: str = os.path.join('artifacts',
                                      'raw.csv')
    # Note to self: recall to update gitignore file with .artifacts

class DataIngestion:

    def __init__(self):
        ''' assigns the 3 sub-object variables defined above 
            to the class variable 'ingestion_config' '''

        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info('Data ingestion method/component has commenced')

        try:
            # here we could add MongoClient class 
            # or any other DB framework/API instat. etcetera.
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('The dataset has been parsed as a dataframe') 
            
            # create a leaf directory and all intermediate ones
            os.makedirs(os.path\
                          .dirname(self.ingestion_config\
                                       .train_data_path),
                        exist_ok = True)
            
            # Write the dataframe object to a csv file 
            df.to_csv(self.ingestion_config\
                          .raw_data_path,
                      index = False,
                      header = True)

            logging.info('Train test split process has commenced')

            train_set,test_set = train_test_split(df,
                                                  test_size = .2,
                                                  random_state = 42)

            train_set.to_csv(self.ingestion_config\
                                 .train_data_path,
                             index = False,
                             header = True)

            test_set.to_csv(self.ingestion_config\
                                .test_data_path,
                            index = False,
                            header = True)

            logging.info('Data Ingestion has finalized')

            # What I'll be passing here it'll be 
            # the input of the data transformation module
            return(
                self.ingestion_config\
                    .train_data_path,
                self.ingestion_config\
                    .test_data_path
            )
        
        except Exception as e:

            raise CustomException(e,sys)
        
if __name__=="__main__":

    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()

    train_arr, test_arr, _ = data_transformation\
                             .initiate_data_transformation(train_data,
                                                           test_data)
     
    modeltrainer = ModelTrainer()

    print (modeltrainer\
          .initiate_model_trainer(train_arr,
                                  test_arr)\
          .round(5))





