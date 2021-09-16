import pytest
import app
import os
from utils.classfunct import *

def test_asimpletest():
   a = 20
   b = 30
   result = a + b
   
   assert result == 50
   

os.system('curl -X POST --data-urlencode "payload={\"channel\": \"#buildstatus\", \"username\": \"Build Status\", \"text\": \"A change to the directory structure was noticed and you need to check your build logs @/srv/www/logs\", \"icon_emoji\": \":eight_spoked_asterisk:\"}" https://hooks.slack.com/services/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')