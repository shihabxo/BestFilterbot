# 📡 API & BOT Settings
API_ID = 24059088
API_HASH = "40c03e1bebb18c40760703b09c51df61"
BOT_TOKEN = "7685758094:AAF9OmztzitHTbjSLfxAF0Kn6LW0ruCnxNo"

# 🗄️ MongoDB Database Settings
MONGO_URI = "mongodb+srv://Shihabx:Shihabx@cluster0.e0car2d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "ShiplaBot"

# 🔗 Groups & Logs
LOG_CHANNEL = -1002716060565     # Error, logs যাবে এখানে
ADMINS = [1775476699]            # Bot owner(s)
ALLOW_ALL_GROUPS = True          # যেকোনো গ্রুপে কাজ করবে কি না

# 🔁 Forwarding Settings
FORWARD_AS_COPY = True           # Copy করে ফাইল পাঠাবে
BROADCAST_AS_COPY = False        # Broadcast message copy হবে কি না

# 🚫 URL Lock & Warnings
URL_LOCK = True                  # গ্রুপে url দিলে warning দিবে
MAX_WARNINGS = 3                 # কয়বার warning দিলে ban করবে
BAN_COMMAND = "/ban"             # Ban কমান্ড কী হবে

# 🙋‍♂️ Welcome Message
SEND_WELCOME = True              # গ্রুপে কেউ join করলে welcome দিবে
WELCOME_TEXT = "👋 স্বাগতম! মুভির নাম লিখে সার্চ করুন 🔎"
WELCOME_DELAY = 2                # কয় সেকেন্ড পর welcome দিবে
WELCOME_AUTO_DELETE = True       # Welcome মেসেজ auto delete করবে কি না
WELCOME_DELETE_TIMER = 15        # কয় সেকেন্ড পর মুছে ফেলবে

# 🔍 Auto File Search (Filter feature)
AUTO_FILE_SEARCH = True          # মেসেজে লেখা অনুযায়ী ফাইল খুঁজে দিবে

# ⚙️ Custom Commands
COMMAND_PREFIX = "/"             # কমান্ড prefix (যেমন /start, /ban)
HELP_COMMAND = "/help"           # Help কমান্ড কী হবে
START_MSG = "🎬 মুভি ফিল্টার বটে স্বাগতম!\n🔎 মুভি খুঁজতে শুধু নাম লিখুন।"

# 📛 Others
DELETE_COMMANDS = True           # /start বা /ban দিলে message auto delete হবে কি না
FILE_SEND_LOG = True             # কোন ইউজারকে কী ফাইল পাঠানো হলো, সেটা log করবে
