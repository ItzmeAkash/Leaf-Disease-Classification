from diseaseClassifier import logger
from diseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from diseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME}  started <<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "PrePare Base Model stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME}  started <<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e

        
