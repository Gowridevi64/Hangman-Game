from importlib import reload
import modulerld
import time

modulerld.add(4, 5)

time.sleep(45)

reload(modulerld)

modulerld.sub(23, 10)