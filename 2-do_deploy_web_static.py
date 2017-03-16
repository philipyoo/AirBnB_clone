#!/usr/bin/python3

from fabric.api import put, run, env
from os.path import isfile

env.hosts = ['75.101.171.13', '54.174.68.191']


def do_deploy(archive_path):
    file_name = archive_path.split("/")[-1]
    file_without = file_name.split(".")[0]
#    if not isfile(archive_path):
#        return False

    put(archive_path, "/tmp/")
    run("sudo mkdir -p /data/web_static/releases/%s" % file_without)
    run("sudo tar -xzf /tmp/%s -C /data/web_static/releases/%s/"
        % (file_name, file_without))
    run("sudo rm /tmp/%s" % file_name)
    run("""sudo mv /data/web_static/releases/%s/web_static/*
    /data/web_static/releases/%s""" % (file_without, file_without))
    run("sudo rm -rf /data/web_static/releases/%s/web_static" % file_without)
#    run("rm -rf /data/web_static/current")
    run("sudo ln -sf /data/web_static/releases/%s/ /data/web_static_current"
        % file_without)

    return True
