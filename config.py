import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16705145")

API_HASH = os.environ.get("API_HASH", "0e6d2bd4de5dc0916f792030a9070042")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5830959729:AAFP9IKxjZPpCdANk6rnDdtXl0867T_VSfk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "anylink_lk") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://anylinks_bot:Anylinks222@cluster0.w4hsbur.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/St21hVq/ANYLINKS-LK.png")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
