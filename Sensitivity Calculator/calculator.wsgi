#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:10:28 2022

@author: natsukoyamaguchi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:08:26 2022

@author: natsukoyamaguchi
"""

# add your project directory to the sys.path
import sys
project_home = '/usr/local/www/wsgi-scripts/setisnr'

#sys.path.insert(0, project_home)
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from calculator import Flask_App as application
