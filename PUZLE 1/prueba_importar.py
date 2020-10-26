from puzle1 import *


rf = RfidPN532()
uid = rf.read_uid()
print(uid)