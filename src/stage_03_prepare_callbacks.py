from src.utils.all_utils import read_yaml, create_directory
import argparse
import os
import logging
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from src.utils.callbacks import create_and_save_tensorboard_callback
from src.utils.callbacks import create_and_save_checkpoint_callback

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")


def prepare_callbacks(config_path, params_path):
    config = read_yaml(config_path)
    params_path = read_yaml(params_path)
    artifacts = config['artifacts']
    artifacts_dir = artifacts['ARTIFACTS_DIR']
    tensorboard_log_dir = os.path.join(artifacts_dir,artifacts['TENSORBOARD_ROOT_LOG_DIR'])

    checkpoint_dir = os.path.join(artifacts_dir,artifacts['CHECKPOINT_DIR'])
    callback_dir = os.path.join(artifacts_dir,artifacts['CALLBACKS_DIR'])

    create_directory([tensorboard_log_dir,checkpoint_dir,callback_dir])

    create_and_save_tensorboard_callback(callback_dir,tensorboard_log_dir)
    create_and_save_checkpoint_callback(callback_dir, checkpoint_dir)



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage three started")
        prepare_callbacks(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("stage three completed! callbacks are prepared and saved as binary >>>>>")
    except Exception as e:
        logging.exception(e)
        raise e