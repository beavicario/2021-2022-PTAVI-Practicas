import argparse
import json
import os
import sys
import unittest

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Check practice.')
    parser.add_argument('--silent', action='store_true',
                        help="silent output, only summary is written")
    parser.add_argument('--json', action='store_true',
                        help="output in json format")
    args = parser.parse_args()

    this_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.join(this_dir, '..')
#    sys.path.insert(0, parent_dir)
    test_suite = unittest.TestLoader().discover(this_dir,
                                                pattern='test_*.py',
                                                top_level_dir=parent_dir)
    stream = None
    if args.silent:
        stream = open(os.devnull, 'w')
    runner = unittest.TextTestRunner(buffer=True, stream=stream)
    result = runner.run(test_suite)

    if args.json:
        result_dict = {
            'errors': [str(item[0]) for item in result.errors],
            'failures': [str(item[0]) for item in result.failures],
            'errors_no': len(result.errors),
            'failures_no': len(result.failures),
            'tests_run': result.testsRun,
            'success': result.wasSuccessful()
        }
        print(json.dumps(result_dict))
    else:
        print(f"Errors: {len(result.errors)}, Failures: {len(result.failures)}, " +
              f"Tests run: {result.testsRun}, All tests successful: {result.wasSuccessful()}")
    sys.exit(not result.wasSuccessful())
