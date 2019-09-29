#!/bin/bash

[ ! -d "venv" ] && python3 -m virtualenv venv && source venv/bin/activate && pip install -r requirements.txt || source venv/bin/activate
python .
deactivate
