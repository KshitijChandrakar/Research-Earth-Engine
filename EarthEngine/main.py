# %%
!pip install earthengine-api google-auth
!pip install pytest


# %% Importing Earth Engine
import ee
import google.auth
# %%
import os

# %%

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not cred_path:
    raise ValueError("Set GOOGLE_APPLICATION_CREDENTIALS env variable!")

# %%
SERVICE_ACCOUNT = os.getenv("GOOGLE_APPLICATION_EMAIL")
if not SERVICE_ACCOUNT:
    raise ValueError("Set GOOGLE_APPLICATION_EMAIL env variable!")
CREDENTIALS = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, cred_path)

# %%
ee.Initialize(CREDENTIALS, project="ee-project-mentor-jayasree")
print(ee.String('Hello from the Earth Engine servers!').getInfo())
