import nose
import os
from camel import CamelUtils
class CamelTestSuite:
    
    camelUtils = None
    
    def __init__(self):
        self.camelUtils = CamelUtils.CamelUtils()
    
    def runTests(self, schemaVersion):
        tests = self.camelUtils.getTests(schemaVersion)
        if len(tests) != 0:
            for test in tests[0]:
                support = os.path.join(os.path.dirname(__file__), '../tests')
                t = os.path.join(support, test)
                nose.run(argv=['nosetests', '-v', t])
        else:
            print ' ----No tests suite'