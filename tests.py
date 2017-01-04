import logging
import unittest
import HTMLTestRunner
from tests.zadanie_1 import FirstRequestTest


def fake_attrs():
    g2attrs = [
        ('My Project Name', 'Fake Project Name'),
        ('Reponsible Team', 'Fake Team'),
        ('Build Number', '42'),
    ]
    g3attrs = [
        ('Produc Under Test', 'The Fake Product Site'),
        ('Product Team', 'Fake Product Team')
    ]
    attrs = {'group2': g2attrs, 'group3': g3attrs}
    return attrs


def fake_description():
    desc = """This is a fake description
    divided in two lines."""
    return desc


if __name__ == '__main__':
    logging.basicConfig(filename='myapp.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')

    # Create the report file
    html_report = open('sample_test_report.html', 'w')
    # Create the runner and set the file as output and higher verbosity
    runner = HTMLTestRunner.HTMLTestRunner(stream=html_report, verbosity=2, attrs=fake_attrs(),
                                           description=fake_description())
    # Create a test list
    tests = [FirstRequestTest]
    # Load test cases
    loader = unittest.TestLoader()
    # Create a SuiteCase
    test_list = []
    for test in tests:
        cases = loader.loadTestsFromTestCase(test)
        test_list.append(cases)
    suite = unittest.TestSuite(test_list)
    # Run the suite
    runner.run(suite)
    logging.info('Finished')