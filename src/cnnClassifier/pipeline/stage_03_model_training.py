import keras

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger


STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        callback_list = [
        keras.callbacks.EarlyStopping(patience=2),
        #keras.callbacks.ModelCheckpoint(filepath='model_checkpoints/model.{epoch:02d}-{val_loss:.2f}.h5'),
        keras.callbacks.ModelCheckpoint(filepath=training_config.checkpoint_path),
        keras.callbacks.TensorBoard(log_dir="./logs"),
        ]
        training.train(
            callback_list=callback_list
        )
        

if __name__ == "__main__":
    try:
        logger.info(f"************************")
        logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        