import os
from telegram import Bot

# اطلاعات توکن و آیدی کانال را وارد کنید
TOKEN = "7427591070:AAEx0pIVlIx4iaWnM_RkMq5YS7AJrRWvVUE"
CHANNEL_ID = "@super_mind_3"
AUDIO_FOLDER = "D:\project\python-small-project\SuperMinds3Audio\Workbook"

def upload_audio_files():
    bot = Bot(token=TOKEN)
    
    # لیست فایل‌ها در پوشه
    files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(('.mp3', '.wav'))]
    
    for file_name in files:
        file_path = os.path.join(AUDIO_FOLDER, file_name)
        try:
            # ارسال فایل به کانال
            bot.send_audio(chat_id=CHANNEL_ID, audio=open(file_path, 'rb'))
            print(f"{file_name} با موفقیت آپلود شد.")
        except Exception as e:
            print(f"خطا در آپلود {file_name}: {e}")

if __name__ == "__main__":
    upload_audio_files()
