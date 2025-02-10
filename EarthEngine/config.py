from os import getenv
SERVICE_ACCOUNT = getenv("GOOGLE_APPLICATION_EMAIL")
CREDENTIALS = getenv("GOOGLE_APPLICATION_CREDENTIALS")
def CheckEnvs():
    global getenv
    if not CREDENTIALS:
        raise ValueError("Set GOOGLE_APPLICATION_CREDENTIALS env variable!")
    if not SERVICE_ACCOUNT:
        raise ValueError("Set GOOGLE_APPLICATION_EMAIL env variable!")
    del getenv
