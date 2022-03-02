from mymodule import add as sum
import mymodule3
import mymodule3
import time
print("Before sleep")
time.sleep(10)
print("After sleep")
#from imp import reload
from importlib import reload
reload(mymodule3)
reload(mymodule3)
