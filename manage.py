#!/usr/bin/env python
"""Flask command-line utility for administrative tasks."""
import os
import sys
import click
from flask.cli import cli
import subprocess
from subprocess import Popen
from routes import App
# from flask_script import Manager #TODO(Reminder not a todo): flask_script is not supported in flask >= 2.x versions
# debug = os.environ.get('LOCAL', True)


# cli = FlaskGroup(App)

# @App.cli.command()
# @click.option('-d', '--debug', is_flag=True, help='Enable and Disable debug mode')
# @click.option(
#     '-a', '--address', default='127.0.0.1',
#     help="Specify the address to which to bind the web server")
# @click.option(
#     '-p', '--port', default='9090',
#     help="Specify the port on which to run the web server")
# @click.option(
#     '-t', '--timeout', default='60',
#     help="Specify the timeout (seconds) for the gunicorn web server")
# @click.option(
#     '-w', '--workers', default='2',
#     help="Number of gunicorn web server workers to fire up")
# @click.option(
#     '-h', '--threads', default=30,
#     help="Number of gunicorn web server threads for each worker to fire up")
#
# def runserver(debug, address, port, timeout, workers):
#     if debug:
#         App.run(
#             host='127.0.0.1',
#             port=9090,
#             debug=True
#         )
#     else:
#         cmd(
#             'gunicorn '
#             '-w {workers} '
#             '-threads {threads} '
#             '--timeout {timeout} '
#             '-b {address}:{port} '
#             'routes:App'
#         ).format(**locals())
#         Popen(cmd, shell=True).wait()

# @App.cli.command('runserver')
# @click.option('-d', '--debug', action='store_true', help='Enable and Disable debug mode')
def set_debug():
    App.debug=True
# @click.option('--port', default=9000, help='The port to bind to.')
# @click.option('--debug', is_flag=True, help='Enable or disable debug mode.')
# def run(host, port,debug):
#     'custom runserver command with your own options'
#     if debug:
#         App.run(
#             host=host,
#             port=port,
#             debug=debug
#         )
# @App.cli.command
# def test():
#     """Running Tests."""


@App.cli.command()
@click.option('-d', '--debug', is_flag=True, help='Enable and Disable debug mode')
def runserver(debug):
    if debug:
        gunicorn_cmd = [
            sys.executable,
            '-m', 'gunicorn',
            '-w', '4',
            '-b', '127.0.0.1:8000',
            "routes:App"]
        subprocess.run(gunicorn_cmd)

if __name__ == '__main__':
    # runserver()
    print('haris')
    # App.cli.add_command(runserver_command)
    host='127.0.0.1'
    port=9000
    # debug
    App.run()

    if App.debug:
        App.run()
    else:
        gunicorn_cmd = [
            sys.executable,
            '-m', 'gunicorn',
            '-w',  '4',
            '-b', f'{host}:{port}',
            "routes:App"]
        subprocess.run(gunicorn_cmd)