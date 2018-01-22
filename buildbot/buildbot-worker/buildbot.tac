import os

from buildbot_worker.bot import Worker
from twisted.application import service
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import LogFile


basedir = os.path.abspath(os.path.dirname(__file__))
rotateLength = 10000000
maxRotatedFiles = 10

# note: this line is matched against to check that this is a worker
# directory; do not edit it.
application = service.Application('buildbot-worker')

logfile = LogFile.fromFullPath(
    os.path.join(basedir, "twistd.log"),
    rotateLength=rotateLength,
    maxRotatedFiles=maxRotatedFiles
)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

buildmaster_host = 'localhost'
port = 9989
workername = 'example-worker'
passwd = 'pass'
keepalive = 600
umask = None
maxdelay = 300
numcpus = None
allow_shutdown = None
maxretries = None

worker = Worker(
    buildmaster_host,
    port,
    workername,
    passwd,
    basedir,
    keepalive,
    umask=umask,
    maxdelay=maxdelay,
    numcpus=numcpus,
    allow_shutdown=allow_shutdown,
    maxRetries=maxretries,
)
worker.setServiceParent(application)

# vim: set ft=python et:
