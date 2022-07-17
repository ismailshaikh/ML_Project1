from collections import namedtuple
from unicodedata import name

DataIngestionConfig = namedtuple("DataIngestionConfig", 
        [
        "dataset_download_url",
        "tgz_download_dir",
        "raw_data_dir",
        "ingested_train_dir",
        "ingested_test_dir"
        ])
# -------------------------------------------------------------------------------------------


DataValidationConfig = namedtuple("DataValidationConfig",
        ["schema_file_path"])
# schema_file_path : How many number of column and ehat are there datatype 
# -------------------------------------------------------------------------------------------


DataTransformationConfig = namedtuple("DataTransformationConfig",
        [
        "add_bedroom_per_room",
        "transformed_train_dir",
        "transformed_test_dir",
        "preprocessed_object_file_path"
        ])

'''
DataTransformationConfig        : For Feature engineering
add_bedroom_per_room (Optional) : dataset this collumn is not available then we will add this column as (True)
transformed_train_dir           : preprocessing apply and then transform dataset location
transformed_test_dir            : after apply feature enginnering where we will apply after transformation we will do in this location 
preprocessed_object_file_path   : pickle file created of abouve info and  stored in this file
'''
# -------------------------------------------------------------------------------------


ModelTrainerConfig = namedtuple("ModelTrainerConfig",
        [
        "trained_model_file_path",
        "base_accuracy"
        ])
'''
ModelTrainerConfig      : 
trained_model_file_path : after trainning model export in pickle file that location specify through this 
base_accuracy           : minimum criteria for accuracy 
'''
# -------------------------------------------------------------------------------------


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
        [
        "model_evaluation_file_path",
        "time_stamp"
        ])
'''
ModelEvaluationConfig      :
model_evaluation_file_path : keep information about all model which is in production, 
                                use test data, and compare models
time_stamp                 :  just to stored activity of comparing at what time happen

'''
# -------------------------------------------------------------------------------------


ModelPusherConfig = namedtuple("ModelPusherConfig",
        ["export_dir_path"])

'''
ModelPusherConfig
export_dir_path     : where i will export my train model
'''
# -------------------------------------------------------------------------------------


TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
        ["artifact_dir"])

'''
TrainingPipelineConfig
artifact_dir
'''


