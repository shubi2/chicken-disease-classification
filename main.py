from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME='Data ingetion stage'

if __name__=='__main__':
    try:
        logger.info(f'..........stage {STAGE_NAME} started')
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'..........stage {STAGE_NAME} completed')

    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME='prepare base model'

if __name__=="__main__":
    try:
        logger.info(f'stage {STAGE_NAME} started')
        obj= PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'stage {STAGE_NAME} completed')

    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME='Training Stage'

try:
        logger.info(f'stage {STAGE_NAME} started')
        obj= ModelTrainingPipeline()
        obj.main()
        logger.info(f'stage {STAGE_NAME} completed')

except Exception as e:
        logger.exception(e)
        raise e
    
    

STAGE_NAME='Evaluation Stage'
if __name__=='__main__':
    try:
        logger.info(f'stage {STAGE_NAME} started')
        obj= EvaluationPipeline()
        obj.main()
        logger.info(f'stage {STAGE_NAME} completed')


    except Exception as e:
        logger.exception(e)
        raise e