#!/usr/bin/env python
# -*- coding: utf-8 -*-
# macports: uninstalls macports update
# https://github.com/bnomis/macports-update
# (c) Simon Blanchard
from __future__ import print_function

import os
import os.path

def launchctl_unload(path):
    argv = ['launchctl', 'unload', path]
    try:
        p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print('Exception running %s: %s' % (argv, e))
    else:
        stdout, stderr = p.communicate()
        if stdout:
            print(stdout.decode().strip())
        if stderr:
            print(stderr.decode().strip())
        p.wait()
        
def uninstall():
    launchctl_unload()
    
    fn = 'org.macports.update.plist'
    destdir = '/Library/LaunchDaemons'
    dest = os.path.join(destdir, fn)
    try:
        os.remove(dest)
    except Exception as e:
        print('Exception deleting %s: %s' % (dest, e))


if __name__ == '__main__':
    uninstall()

