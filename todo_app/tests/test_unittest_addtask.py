import pytest
import app
from utils.classfunct import *

def test_addtask():
   
   addcard = card_tasks()

   result = addcard.addcard_todo("Test Card","PyTest Adding a card!")
   index = 'Test Card' in cardsonlist
   assert result == "200"
   assert index == True