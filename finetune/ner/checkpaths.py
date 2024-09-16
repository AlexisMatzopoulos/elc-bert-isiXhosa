import os
import argparse
import logging

logger = logging.getLogger(__name__)

def check_path(path, description):
    if os.path.exists(path):
        logger.info(f"{description} exists: {path}")
    else:
        logger.error(f"Error: {description} does not exist: {path}")
        raise FileNotFoundError(f"{description} does not exist: {path}")

def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--data_dir", default=None, type=str, required=True, help="Path to the input data directory.")
    parser.add_argument("--pretrained_model_path", default=None, type=str, required=True, help="Path to the pretrained model directory.")
    parser.add_argument("--model_name_or_path", default=None, type=str, required=True, help="Path to pre-trained model or shortcut name.")
    parser.add_argument("--output_dir", default=None, type=str, required=True, help="Output directory.")
    parser.add_argument("--test_result_file", default="test_results.txt", type=str, help="Test result file.")
    parser.add_argument("--test_prediction_file", default="test_predictions.txt", type=str, help="Test prediction file.")

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO,
    )

    logger.info("Checking paths...")

    # Check data directory
    check_path(args.data_dir, "Data directory")

    # Check pretrained model path
    check_path(args.pretrained_model_path, "Pretrained model path")

    # Check model name or path
    check_path(args.model_name_or_path, "Model name or path")

    # Check output directory (create if not exists)
    if not os.path.exists(args.output_dir):
        logger.info(f"Output directory does not exist. Creating: {args.output_dir}")
        os.makedirs(args.output_dir)
    else:
        logger.info(f"Output directory exists: {args.output_dir}")

    # Check if test result and prediction files can be written in the output directory
    test_result_file_path = os.path.join(args.output_dir, args.test_result_file)
    test_prediction_file_path = os.path.join(args.output_dir, args.test_prediction_file)
    
    try:
        with open(test_result_file_path, "w") as f:
            f.write("Path test: Test results\n")
        logger.info(f"Test result file is writable: {test_result_file_path}")
    except Exception as e:
        logger.error(f"Error writing test result file: {test_result_file_path}")
        raise e
    
    try:
        with open(test_prediction_file_path, "w") as f:
            f.write("Path test: Test predictions\n")
        logger.info(f"Test prediction file is writable: {test_prediction_file_path}")
    except Exception as e:
        logger.error(f"Error writing test prediction file: {test_prediction_file_path}")
        raise e

    logger.info("All paths are valid and files are writable.")

if __name__ == "__main__":
    main()
