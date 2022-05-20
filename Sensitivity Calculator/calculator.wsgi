#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:08:26 2022

@author: natsukoyamaguchi
"""

import sys
# add your project directory to the sys.path
project_home = '/usr/local/www/wsgi-scripts/seti_snr'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from calculator import Flask_App as application
