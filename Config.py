import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24086498"))
    API_HASH = os.environ.get("API_HASH", "0c459b186767a4634604c740c001c0c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFvh-IAe7KuoZAx_j3rZrBGO-Jkri-VGLlXbCvNG9V37pmlr4rtr2VnYwJEXoY405pBv8sJyV0PF9lVJrA2hnB9wtQJmKdc1Tz6p5dZkUidfp-WHs3lHZZPJSzoqo3a0Kc0Mp5ivxK-EQdXu-YDmDw2NvWZrQhTjaYI_oL-62AlKRxD4P1ZP9tp1zW8sP-LNKYqvOxmHoRbJ7pCQYFERGPlwjQ1iEnZmPwKfkRJKvJI34pidhzvNAbBRDWXk82dmt6CI1H_ggAav-9CwTMJIXXRWM6pG37pJ-QElb1MxK1aHE23xUjeiuxf5bUoTBufDVlrZiMCoNpIK9O_lwBzXCJql4kZQwAAAAE5g3gCAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
