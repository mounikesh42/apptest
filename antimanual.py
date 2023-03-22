from wps import wps
from safe import safe
from shareit import shareit
from edlp import edlp
from scratch import scratch
from koto import koto
from whiteboard import whiteboard
from inshot import inshot
from esfile import esfile
from settings import settings
import subprocess


subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'true'])


#
edlp()
print("")
esfile()
print("")
safe()
print("")
#
scratch()
print("")
whiteboard()
print("")
shareit()
print("")
wps()
print("")
koto()
print("")


inshot()
print("")
#

#







# settings()

subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'false'])
