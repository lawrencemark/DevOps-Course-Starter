import pytest
import app
from utils.classfunct import *

def test_asimpletest():
   a = 20
   b = 30
   result = a + b
   
   assert result == 50
   

   