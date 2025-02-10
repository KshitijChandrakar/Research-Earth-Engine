# %% Importing Earth Engine
import ee
import google.auth
import os
from EarthEngine.config import *
import datetime

# %% Check that All Environment Variables Exist
CheckEnvs()

# %% Connect To Earth Engine Servers
# CREDENTIALS = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, CREDENTIALS)

ee.Initialize(ee.ServiceAccountCredentials(SERVICE_ACCOUNT, CREDENTIALS), project="ee-project-mentor-jayasree")
print(ee.String('Hello from the Earth Engine servers!').getInfo())

# %%
