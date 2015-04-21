#!/usr/bin/env python
# -*- coding: utf-8 -*-
# macports: updates macports
# https://github.com/bnomis/macports-update
# (c) Simon Blanchard
import argparse
import datetime
import subprocess
import sys

# the port command
portcmd = '/opt/local/bin/port'

# where to write logs
logfile = '/var/root/logs/macports.log'


# version info
version_info = (0, 1, 0)
__version__ = ".".join([str(v) for v in version_info])


def write_log(options, log, exception=None):
    with open(logfile, 'a') as fp:
        fp.write(log + '\n')
        if exception:
            fp.write('%s\n' % exception)


def run_port(options, cmd):
    argv = [portcmd, '-q']
    argv.extend(cmd.split())
    try:
        p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        write_log(options, 'Exception running %s' % argv, exception=e)
    else:
        stdout, stderr = p.communicate()
        if stdout:
            write_log(options, stdout.decode().strip())
        if stderr:
            write_log(options, stderr.decode().strip())
        p.wait()


def macports_update(options):
    write_log(options, '\n------------')
    write_log(options, 'Starting update %s' % datetime.datetime.now())

    run_port(options, 'selfupdate')
    run_port(options, 'upgrade outdated')
    run_port(options, 'uninstall inactive')

    write_log(options, 'Starting ended %s' % datetime.datetime.now())
    write_log(options, '------------\n')


def main(argv):
    program_name = 'macports'
    usage_string = '%(prog)s [options]'
    version_string = '%(prog)s %(version)s' % {'prog': program_name, 'version': __version__}
    description_string = 'macports: updates the installed macports'

    parser = argparse.ArgumentParser(
        prog=program_name,
        usage=usage_string,
        description=description_string,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--version',
        action='version',
        version=version_string
    )
    options = parser.parse_args(argv)

    macports_update(options)
    return 0

def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == '__main__':
    run()

