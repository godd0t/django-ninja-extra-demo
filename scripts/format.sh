#!/bin/bash -e

APP_PATH="."

ruff $APP_PATH --fix
black $APP_PATH
isort $APP_PATH
