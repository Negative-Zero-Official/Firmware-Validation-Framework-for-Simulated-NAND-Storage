import unittest
import logging

logging.basicConfig(
    filename = "logs/test_log.txt",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = 'a'
)
logger = logging.getLogger(__name__)

def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('test_cases')

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    with open("report/test_summary.md", "w") as f:
        f.write("# Test Summary\n")
        f.write(f"- Total Tests: {result.testsRun}\n")
        f.write(f"- Failures: {len(result.failures)}\n")
        f.write(f"- Errors: {len(result.errors)}\n")
    
    logger.info("========== Test run complete ==========")
    logger.info(f"Total: {result.testsRun}, Failures: {len(result.failures)}, Errors: {len(result.errors)}")
    logger.info("=======================================\n")


if __name__ == "__main__":
    run_all_tests()