from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = "san280201"  # <-- Thay đổi nếu cần

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        keyboard = [
            [InlineKeyboardButton("✅ Tôi đã nhắn admin", url=f"https://t.me/{ADMIN_USERNAME}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"👋 Chào {member.full_name}!\n\n"
                f"Vui lòng nhắn tin cho admin @{ADMIN_USERNAME} để được duyệt.\n"
                f"Sau đó bấm nút dưới đây để xác nhận."
            ),
            reply_markup=reply_markup
        )

application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
application.run_polling()


