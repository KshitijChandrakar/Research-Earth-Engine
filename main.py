# %%
!pip install earthengine-api google-auth

# %% Importing Earth Engine
import ee
import google.auth
import os


# %%
os.getcwd()

# %%

print(os.path.exists("ee-project-mentor-jayasree-8b1f7ae43ce4.json"))  # Should return True if the file exists

# %%
SERVICE_ACCOUNT = 'pulsar-debian@ee-project-mentor-jayasree.iam.gserviceaccount.com'
CREDENTIALS = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, 'Earth Engine/ee-project-mentor-jayasree-8b1f7ae43ce4.json')

# %%
ee.Initialize(CREDENTIALS, project="ee-project-mentor-jayasree")

# %%
print(ee.String('Hello from the Earth Engine servers!').getInfo())
