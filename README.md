# macports-update

This is a simple script that will update your macports while you are sleeping.

It installs a simple service (via launchd) which runs the three commands below.

```shell
$ port selfupdate
$ port upgrade outdated
$ port uninstall inactive
```

Now your macports are always up to date.

By default the scripts assumes the following:

* The repository is cloned in to `/var/root/src`
* Logging is to `/var/root/logs/macports.log`
* Update time is 1:10AM

If these assumptions do not match with your needs you'll need to edit the `macports.py` and `org.macports.update.plist` files.

## Install

The script needs to be run as root, so become root before installing.

1. Clone this repository.
2. If needed, edit the `macports.py` and `org.macports.update.plist` files to suit. (See above.)
3. Run the `install.py` script

## Uninstall

1. Run the `uninstall.py` script


