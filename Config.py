import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24086498"))
    API_HASH = os.environ.get("API_HASH", "0c459b186767a4634604c740c001c0c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFvh-IAaOkBnrTD0HLoGiJwuqU4k7JHoxbP-dyyo2rQsbWu7aROO3IxsG7bbQ5A14OGM-eNu_ePJbP9ArPPvQmn9OflXXqtEa9TtgWRDfUOHOqGTIEXR47l_rw4TIHV6JdHf6KGFCXdmNMDtBQ0II_2AnIvOfoZSs2t5PP3AbOjZhT0vd63RMdIy3Qer2evKA8mQdRWmHvh3_eE23xqou_cfnAhNKGD8UcInDYz0-3UeAIkQdZwg-2haFgIitgiwZ4bm-JDLvm5HjjzDXJloRrTfN4DKCCrRxbHbLr1iSwWPWK-6nUiKfPXURTSH15bqTDme2hfK97SBCv4qQthuR30h_ilBwAAAAE5g3gCAA")
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
