from fabric.api import local


def register():
    local("python setup.py register")


def upload():
    local("python setup.py sdist upload")
