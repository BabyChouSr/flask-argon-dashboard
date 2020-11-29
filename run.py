# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
'''
from app import app, db
'''
from flask_frozen import Freezer
from app import app,db

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
