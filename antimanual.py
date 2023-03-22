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



edlp()
print("")

scratch()
print("")

koto()
print("")

whiteboard()
print("")

inshot()
print("")

esfile()
print("")

wps()
print("")

safe()
print("")

shareit()
print("")


settings()

subprocess.run(['adb', 'shell', 'svc', 'power', 'stayon', 'false'])
