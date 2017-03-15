#!/usr/bin/python3

from fabric.api import local
import datetime

def do_pack():
    local('mkdir -p versions')
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local('tar -cvzf "versions/web_static_%s.tgz" ./web_static' % timestamp)
