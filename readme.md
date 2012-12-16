# Motivation

This is a modification of Blossom's [Flask GAE Skeleton](https://github.com/blossom/flask-gae-skeleton) . I modify this to run under the Python 2.7 Runtime. Credits to Thomas Schranz, Allan Berger, and Nik Graf for the initial skeleton.

This is a project skeleton which includes some of the things (libs and configuration) that I pick for most projects.

# Components

## General

here is a list of assembled components

* flask decorators for (cache_page, login_required)
* gae specific monkeypatch for werkzeug debugger [http://dev.pocoo.org/projects/werkzeug/wiki/UsingDebuggerWithAppEngine](http://dev.pocoo.org/projects/werkzeug/wiki/UsingDebuggerWithAppEngine)
* a simple user model
* google appengine specific development/production environment switch
* google appengine appstats configured
* google appengine memcache caching backend configured
* favicon.ico stub to avoid unneeded error logs
* deck module with 26 char uuid generator
* deck module with JsonProperty for the datastore
* lib directory for external dependencies prepended to syspath

## Libraries

### Python

* Flask
* Jinja
* werkzeug
* gaeUtils from blossom [http://github.com/blossom/gae-utils](http://github.com/blossom/gae-utils)
* gaePath [http://github.com/nikgraf/gae-path](http://github.com/nikgraf/gae-path)

# Dependencies

## General

* Python 2.7
* Google AppEngine SDK [http://code.google.com/appengine/downloads.html](http://code.google.com/appengine/downloads.html)

# Setup

clone repository

    git clone https://github.com/femmerling/Flask-GAE-py27.git <project_name>

change to directory of <project_name>

    cd <project_name>

fetch all the submodules via

    git submodule update --init

set your own appengine application id in app.yaml

change the 'secret_key' in settings.py by generating a new one

add replace remote

    git remote rm origin
    git remote add origin <new_remote like git@github.com:your_name/project_name.git>
    git commit -am "initial setup"
    git push origin master

# Update from Skeleton

Add the remote and merge in all changes and removes the old stuff again.

    git remote add skeleton https://github.com/femmerling/Flask-GAE-py27.git
    git pull skeleton
    git checkout -b skeleton remotes/skeleton/master
    git rebase <your_development_branch like master>
    git checkout <your_development_branch like master>
    git merge --no-ff skeleton
    git branch -D skeleton
    git remote rm skeleton
    git submodule update

# Usage

## Run Application

Go to path "code" and run

    dev_appserver.py .

## Run Remote Console

Go to path "code" and run

    python appengine_console.py <app-id>


