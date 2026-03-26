from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_component import Evaluation
from src.cnnClassifier import logger
import os 

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/surajkale99/wd_project_26.mlflow"
        # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        os.environ["MLFLOW_TRACKING_USERNAME"] = "surajkale99"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "e4f2406488322cebc687e5c389841eb67f8beeec"

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

