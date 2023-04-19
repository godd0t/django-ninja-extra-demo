#!/bin/bash -e
APP_PATH="."

export PYTHONPATH=$APP_PATH

pytest
