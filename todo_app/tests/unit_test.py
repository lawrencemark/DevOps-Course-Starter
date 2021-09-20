
import os,sys,inspect, pytest 
from datetime import datetime
sys.path.append('/srv/www/')
import utils.classfunct 

class TestClass():
    def setup_class(self):
        pass

    def teardown_class(self):
        pass


    def teardown_method(self):
        pass # we will add some fancy webhooks and emails here passed on the status of the tests later
    
    # Unit Test Web Server is running and application is running
    def test_unittestWebServer(self,app, client):
        result = client.get('/')
        assert result.status_code == 200
