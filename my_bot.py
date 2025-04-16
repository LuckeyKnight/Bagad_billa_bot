#git push -u origin main


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

print("starting up bot...")

async def starting_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Billa zone😼🐈‍⬛ \n Play games & Do enjoying stuffs here .....\nClick /help for commands ")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are list of commands:- \n\n/start - To start the Bot👍 \n/help - for help⚙️ \n/trick - TO do a mind trick🧠\n/roll - To roll a dice (if get 1 you won)🎲 \n/drawcard - To draw a random card🃏 \n/rps - To play Rock Paper Scissor🪨📃✂️")

async def trick_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Wanna start a trick, then write any number between 1 to 100....\n if thinked, click /guessed")
async def guessed_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Now add next higher number to it... \n \n if added click /added")
async def added_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("And now add 9 to it...if added click /YaAdded")
async def YaAdded_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Now divide it with 2.\n Then Subract the original number from your answer. \n if you are done with it ....click /done")
async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Congrats your answer is 5 🎉🍾")
    

async def emozi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker("CAACAgIAAxkBAAEB0cJkW4FgyrOn-J6tWr5fvN20PthLCgACrQADVp29Cpi1kJ-NOqRaNAQ")
    
async def green_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker("CAACAgIAAxkBAAEB0cJkW4FgyrOn-J6tWr5fvN20PthLCgACrQADVp29Cpi1kJ-NOqRaNAQ")
    
async def drawcard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    categories = ['Hearts ♥️', 'Diamonds ♦️', 'Clubs ♣️', 'Spades ♠️']
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'joker']
    catagory = random.choice(categories)
    card = random.choice(cards)
    if card == 'joker':
        await update.message.reply_text("You drew a joker, you win!")
    else:
        await update.message.reply_text(f"🃏You Drew {card} of {catagory}")
    
async def roll_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dice_value = random.randint(1,6)
    if dice_value == 1:
        await update.message.reply_text(f"You got {dice_value} 👽👍")
    else:
        await update.message.reply_text(f"🎲 You rolled a {dice_value}!")

async def rps_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        InlineKeyboardButton("Rock", callback_data="rock"),
        InlineKeyboardButton("Paper", callback_data="paper"),
        InlineKeyboardButton("Scissor", callback_data="scissor")
    ]
    
    reply_markup = InlineKeyboardMarkup([[button] for button in buttons])
    await update.message.reply_text("🏞️ Ready to Play Rock Paper Scissor\nChoose one:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choices = ["rock","paper","scissor"]
    bot_choice = random.choice(choices)
    query = update.callback_query
    await query.answer()
    data = query.data
    
    if query.data == "rock" and bot_choice == "paper":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     I Won 😙😏")
    if query.data == "paper" and bot_choice == "scissor":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     I Won 😙😏")
    if query.data == "scissor" and bot_choice == "rock":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     I Won 😙😏")
        
    if query.data == "rock" and bot_choice == "scissor":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     You Won 😒🫡🥀")
    if query.data == "paper" and bot_choice == "rock":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     You Won 😒🫡🥀")
    if query.data == "scissor" and bot_choice == "paper":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     You Won 😒🫡🥀")
        
    if query.data == "rock" and bot_choice == "rock":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     Its a Tie 🤧🤧 \nChoose again")
    if query.data == "paper" and bot_choice == "paper":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     Its a Tie 🤧🤧\nChoose again")
    if query.data == "scissor" and bot_choice == "scissor":
        await query.message.reply_text(f"Your  {data}  & Mine  {bot_choice}\n     Its a Tie 🤧🤧\nChoose again")


def handle_response(text: str) -> str:
    if "hello" in text:
        return "Hello back to you"
    if "how are you" in text:
        return "I am fine"
    return "I don't know"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    if message_type == "group":
        if '@strtjrnybot' in text:
            new_text = text.replace('@strtjrnybot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    application = Application.builder().token("7650851850:AAE2FGNNcaixNKwajk95uVVCiP5fTEpagEw").build()

    # Commands
    application.add_handler(CommandHandler('start', starting_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('trick', trick_command))
    application.add_handler(CommandHandler('hiking', hiking_command))
    application.add_handler(CommandHandler('guessed', guessed_command))
    application.add_handler(CommandHandler('added', added_command))
    application.add_handler(CommandHandler('YaAdded', YaAdded_command))
    application.add_handler(CommandHandler('done', done_command))
    application.add_handler(CommandHandler('roll', roll_command))
    application.add_handler(CommandHandler('drawCard', drawcard_command))
    application.add_handler(CommandHandler('Emozi', emozi_command))
    application.add_handler(CommandHandler('rps', rps_command))

    # # Messages handlers
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # # # Errors
    application.add_error_handler(error)

    # Run bot
    application.run_polling()
