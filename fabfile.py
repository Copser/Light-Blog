#!/usr/bin/env python
from fabric.api import local 


def deploy():
    """
    Deploy latest version on GitHub
    """
    local("git push origin master")