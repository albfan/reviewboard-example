OpenShift Quickstart - ReviewBoard
==================================

This repository is designed to be used with [OpenShift][openshift]
applications.

Before using this quickstart, make sure you've created an account on
[OpenShift][openshift].

When configured, you will have a running installation of
[Review Board][reviewboard].

Usage
=====
Quick
-----
1. `rhc app create -a reviewboard python-2.6 mysql-5.1 --from-code git://github.com/openshift/reviewboard-example.git`

Manual
------
1. Create a python-2.6 application and attach mysql to it:

    ```
    rhc app create -a reviewboard -t python-2.6
    rhc cartridge add -a reviewboard -c mysql-5.1
    ```

1. Add this upstream reviewboard repo

    ```
    cd reviewboard
    git remote add upstream -m master git://github.com/openshift/reviewboard-example.git
    git pull -s recursive -X theirs upstream master
    ```

1. Then push the repo upstream

    ```
    git push
    ```

Credentials
===========

| Username | Password       |
| -------- | -------------- |
| Admin    | OpenShiftAdmin |

Updates
=======

In order to update or upgrade to the latest reviewboard, you'll need to re-pull
and re-push.

1. If you created your application using the 'quick' approach, you will
   need to add this repository as an upsteam.

    ```
    git remote add upstream -m master git://github.com/openshift/reviewboard-example.git
    ```

1. Pull from upstream:

    ```
    cd reviewboard/
    git pull -s recursive -X theirs upstream master
    ```

1. Push the new changes upstream

    ```
    git push
    ```

Note: When new releases are pushed from the reviewboard dev team, your app will
automatically download them on your next git push.


Repo layout
===========

| Path | Purpose |
| ---- | ------- |
| wsgi/ | Externally exposed wsgi code |
| libs/ | Additional libraries |
| data/    | For not-externally exposed wsgi code |
| setup.py | Standard setup.py, specify deps here |
| ../data  | For persistent data (also env var: OPENSHIFT_DATA_DIR) |
| .openshift/action_hooks/build | Script that gets run every push, just prior to starting your app |


Environment Variables
=====================

OpenShift provides many environment variables for your application.
See [OpenShift Environment Variables][openshift_env] for a complete
list.


Notes
=====
Repository Layout
-----------------
Please leave wsgi, libs and data directories but feel free to create additional directories if needed.

Note: Every time you push, everything in your remote repo dir gets recreated.
Please store long term items (like a sqlite database) in `$OPENSHIFT_DATA_DIR` which will persist between pushes of your repo.


setup.py
--------

Adding deps to the install_requires will have the OpenShift server actually install those deps at git push time.

[reviewboard]: http://www.reviewboard.org/
[openshift_env]: https://www.openshift.com/page/openshift-environment-variables
[openshift]: http://openshift.redhat.com

