#!/usr/bin/python3

from fabric.api import put, run, env

env.hosts = ['75.101.171.13', '54.174.68.191']


def do_deploy(archive_path):
    try:
        file_name = archive_path.split("/")[-1]
        file_without = file_name.split(".")[0]
        dirname = "/data/web_static/releases/%s" % file_without

        put(archive_path, "/tmp")
        run("sudo mkdir -p %s" % dirname)
        run("sudo tar -xzf /tmp/%s -C %s" % (file_name, dirname))
        run("sudo rm /tmp/%s" % file_name)
        run("sudo mv %s/web_static/* %s/" % (dirname, dirname))
        run("sudo rm -rf %s/web_static" % dirname)
        run("""sudo ln -sf %s/ /data/web_static_current""" % dirname)
        return True
    except Exception:
        return False
