from fabric.api import local


def register():
    local("pip register")


def upload():
    local("python setup.py sdist upload")
