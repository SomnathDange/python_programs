from fabric.api import *

@task
def staging():
    env.user='user'
    env.password='password'
    env.roledefs['app']=['0.0.0.0']

@task
@roles('app')
def cmd():
    sudo('hostname')
