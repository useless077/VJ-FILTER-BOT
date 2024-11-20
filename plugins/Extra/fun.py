# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @Tamilbots
# Ask Doubt on telegram @TamilSupport


from pyrogram import Client, filters

# AESTHETIC------------ https://telegram.me/Josprojects ------------ #

def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["throw", "dart"])
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["roll", "dice"])
)
async def roll_dice(client, message):
    """ @RollADie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["goal", "shoot"])
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


import random

RUN_STRINGS = (
    "A broken of a demeanly filled with darkness \
    Why have you come to remind it ",
    "We have become the lives to be the underwater to the underwater that we do not know.",
    "You want the bad call ... but you need good thunder ....",
    "Oh Bloody Grama Virtues!",
    "Sea MUGGie I Am Going to Pay The Bill.",
    "Want with me!",
    "You are not a male chaff !!",
    "I locked it, and the good beach is done by the good beach.",
    "Kindi ... Kindi ...!",
    "Giving the stems and then showing one and show the ISI Mark",
    "Dayveyeese, Kingfisher ... Childe ...!.",
    "You have made your father for half of the midnight?",
    "This is the King of our work.",
    "I'm fetts to feed ...."
    "Mumak is every Bearby Kachyo ...",
    "Oh it moves it .... When we moves it ...",
    "The self of carpenter is the virtue of a carpenter.",
    "Why not to feel this intelligence in Da Vijaya ...!",
    "Where was this time ...."
    "Save me only ...."
    "I know his father's name is Bhavaniami ....",
    "Da Dasa ...",
    "Uppukam's English Salt Mongo Tree .....",
    "Children ..",
    "Your father to Paul ....",
    "Car Engine Out Completely .....",
    "This is the eye or magnety ...",
    "Before falling in the 4th pegging, I will arrive there.",
    "The drunk rains and wast ...."
    "To tell me I love Yo ...."
    "No, the Meenaka of Verbapur is not ....",
)

REACTIONS = (
    "( ͡° ͜ʖ ͡°)",
    "( . •́ _ʖ •̀ .)",
    "( ಠ ͜ʖ ಠ)",
    "( ͡ ͜ʖ ͡ )",
    "(ʘ ͜ʖ ʘ)",
    "ヾ(´〇`)ﾉ♪♪♪",
    "ヽ(o´∀`)ﾉ♪♬",
    "♪♬((d⌒ω⌒b))♬♪",
    "└(＾＾)┐",
    "(￣▽￣)/♫•*¨*•.¸¸♪",
    "ヾ(⌐■_■)ノ♪",
    "乁( • ω •乁)",
    "♬♫♪◖(● o ●)◗♪♫♬",
    "(っ˘ڡ˘ς)",
    "( ˘▽˘)っ♨",
    "(　・ω・)⊃-[二二]",
    "(*´ー`)旦 旦(￣ω￣*)",
    "( ￣▽￣)[] [](≧▽≦ )",
    "(*￣▽￣)旦 且(´∀`*)",
    "(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ",
    "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆",
    "(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
    "(∩` ﾛ ´)⊃━炎炎炎炎炎",
    "( ・∀・)・・・--------☆",
    "( -ω-)／占~~~~~",
    "○∞∞∞∞ヽ(^ー^ )",
    "(*＾＾)/~~~~~~~~~~◎",
    "((( ￣□)_／",
    "(ﾒ￣▽￣)︻┳═一",
    "ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ",
    "(*`0´)θ☆(メ°皿°)ﾉ",
    "(; -_-)――――――C<―_-)",
    "ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )",
    "(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/",
    "/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)",
    "(`⌒*)O-(`⌒´Q)",
    "(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง",
    "ヾ(・ω・)メ(・ω・)ノ",
    "(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ",
    "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ",
    "｡*:☆(・ω・人・ω・)｡:゜☆｡",
    "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)",
    "(っ˘▽˘)(˘▽˘)˘▽˘ς)",
    "(*＾ω＾)人(＾ω＾*)",
    r"＼(▽￣ \ (￣▽￣) / ￣▽)／",
    "(￣Θ￣)",
    "＼( ˋ Θ ´ )／",
    "( ´(00)ˋ )",
    "＼(￣(oo)￣)／",
    "／(≧ x ≦)＼",
    "／(=･ x ･=)＼",
    "(=^･ω･^=)",
    "(= ; ｪ ; =)",
    "(=⌒‿‿⌒=)",
    "(＾• ω •＾)",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "ଲ(ⓛ ω ⓛ)ଲ",
    "(^◔ᴥ◔^)",
    "[(－－)]..zzZ",
    "(￣o￣) zzZZzzZZ",
    "(＿ ＿*) Z z z",
    "☆ﾐ(o*･ω･)ﾉ",
    "ε=ε=ε=ε=┌(;￣▽￣)┘",
    "ε===(っ≧ω≦)っ",
    "__φ(．．)",
    "ヾ( `ー´)シφ__",
    "( ^▽^)ψ__",
    "|･ω･)",
    "|д･)",
    "┬┴┬┴┤･ω･)ﾉ",
    "|･д･)ﾉ",
    "(*￣ii￣)",
    "(＾〃＾)",
    "m(_ _)m",
    "人(_ _*)",
    "(シ. .)シ",
    "(^_~)",
    "(>ω^)",
    "(^_<)〜☆",
    "(^_<)",
    "(づ￣ ³￣)づ",
    "(⊃｡•́‿•̀｡)⊃",
    "⊂(´• ω •`⊂)",
    "(*・ω・)ﾉ",
    "(^-^*)/",
    "ヾ(*'▽'*)",
    "(^０^)ノ",
    "(*°ｰ°)ﾉ",
    "(￣ω￣)/",
    "(≧▽≦)/",
    "w(°ｏ°)w",
    "(⊙_⊙)",
    "(°ロ°) !",
    "∑(O_O;)",
    "(￢_￢)",
    "(¬_¬ )",
    "(↼_↼)",
    "(￣ω￣;)",
    "┐('～`;)┌",
    "(・_・;)",
    "(＠_＠)",
    "(•ิ_•ิ)?",
    "ヽ(ー_ー )ノ",
    "┐(￣ヘ￣)┌",
    "┐(￣～￣)┌",
    "┐( ´ д ` )┌",
    "╮(︶▽︶)╭",
    "ᕕ( ᐛ )ᕗ",
    "(ノωヽ)",
    "(″ロ゛)",
    "(/ω＼)",
    "(((＞＜)))",
    "~(>_<~)",
    "(×_×)",
    "(×﹏×)",
    "(ノ_<。)",
    "(μ_μ)",
    "o(TヘTo)",
    "( ﾟ，_ゝ｀)",
    "( ╥ω╥ )",
    "(／ˍ・、)",
    "(つω`｡)",
    "(T_T)",
    "o(〒﹏〒)o",
    "(＃`Д´)",
    "(・`ω´・)",
    "( `ε´ )",
    "(ﾒ` ﾛ ´)",
    "Σ(▼□▼メ)",
    "(҂ `з´ )",
    "٩(╬ʘ益ʘ╬)۶",
    "↑_(ΦwΦ)Ψ",
    "(ﾉಥ益ಥ)ﾉ",
    "(＃＞＜)",
    "(；￣Д￣)",
    "(￢_￢;)",
    "(＾＾＃)",
    "(￣︿￣)",
    "ヾ( ￣O￣)ツ",
    "(ᗒᗣᗕ)՞",
    "(ノ_<。)ヾ(´ ▽ ` )",
    "ヽ(￣ω￣(。。 )ゝ",
    "(ﾉ_；)ヾ(´ ∀ ` )",
    "(´-ω-`( _ _ )",
    "(⌒_⌒;)",
    "(*/_＼)",
    "( ◡‿◡ *)",
    "(//ω//)",
    "(￣▽￣*)ゞ",
    "(„ಡωಡ„)",
    "(ﾉ´ з `)ノ",
    "(♡-_-♡)",
    "(─‿‿─)♡",
    "(´ ω `♡)",
    "(ღ˘⌣˘ღ)",
    "(´• ω •`) ♡",
    "╰(*´︶`*)╯♡",
    "(≧◡≦) ♡",
    "♡ (˘▽˘>ԅ( ˘⌣˘)",
    "σ(≧ε≦σ) ♡",
    "(˘∀˘)/(μ‿μ) ❤",
    "Σ>―(〃°ω°〃)♡→",
    "(* ^ ω ^)",
    "(o^▽^o)",
    "ヽ(・∀・)ﾉ",
    "(o･ω･o)",
    "(^人^)",
    "( ´ ω ` )",
    "(´• ω •`)",
    "╰(▔∀▔)╯",
    "(✯◡✯)",
    "(⌒‿⌒)",
    "(*°▽°*)",
    "(´｡• ᵕ •｡`)",
    "ヽ(>∀<☆)ノ",
    "＼(￣▽￣)／",
    "(o˘◡˘o)",
    "(╯✧▽✧)╯",
    "( ‾́ ◡ ‾́ )",
    "(๑˘︶˘๑)",
    "(´･ᴗ･ ` )",
    "( ͡° ʖ̯ ͡°)",
    "( ఠ ͟ʖ ఠ)",
    "( ಥ ʖ̯ ಥ)",
    "(≖ ͜ʖ≖)",
    "ヘ(￣ω￣ヘ)",
    "(ﾉ≧∀≦)ﾉ",
    "└(￣-￣└))",
    "┌(＾＾)┘",
    "(^_^♪)",
    "(〜￣△￣)〜",
    "(｢• ω •)｢",
    "( ˘ ɜ˘) ♬♪♫",
    "( o˘◡˘o) ┌iii┐",
    "♨o(>_<)o♨",
    "( ・・)つ―{}@{}@{}-",
    "(*´з`)口ﾟ｡ﾟ口(・∀・ )",
    "( *^^)o∀*∀o(^^* )",
    "-●●●-ｃ(・・ )",
    "(ﾉ≧∀≦)ﾉ ‥…━━━★",
    "╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ",
    "(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)",
)

TOSS = (
    "Heads",
    "Tails",
)

DECIDE = ("Yes.", "No.", "Maybe.")
GDMORNING = ("Goog morning thala")
GDNIGHT = ("good night bha")
WELCOME_TEMPLATES = ("welcome to our group")
WLC_TXT = (
    "Welcome welcome",
    "Welcome to our group",
    "Ethuku vantha",
)
TRUTH = (
    "Have you ghosted someone?"
    "Have you ever walked in on your parents doing 'it'?",
    "Who was the last person you liked the most? Why?",
    "Have you ever been suspended from school?",
    "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, which would you choose?",
    "What’s the one thing you’re afraid to lose?",
    "Do you like someone as of the moment?",
    "One thing about your best friend you are jealous of?",
    "Would you cheat on your boyfriend for a rich guy?",
    "What is your biggest turn on?",
    "When’s the last time you lied to your parents and why?",
    "Describe your ideal partner.",
    "What’s the scariest thing you’ve ever done?",
    "Have you ever picked your nose and eaten it?",
    "When’s the last time you lied to your parents and why?",
    "Have you ever lied about your age to participate in a contest?",
    "Have you ever been caught checking someone out?",
  
)

DARE = (
    "Show the most embarrassing photo on your phone"
    "Show the last five people you texted and what the messages said",
    "Let the rest of the group DM someone from your Instagram account",
    "Eat a raw piece of garlic",
    "Do 100 squats",
    "Keep three ice cubes in your mouth until they melt",
    "Say something dirty to the person on your leftYou've got company!",
    "Give a foot massage to the person on your right",
    "Put 10 different available liquids into a cup and drink it",
    "*Yell out the first word that comes to your mind",
    "Give a lap dance to someone of your choice",
    "Remove four items of clothing",
    "Like the first 15 posts on your Facebook newsfeed",
    "Eat a spoonful of mustard",
    "Keep your eyes closed until it's your go again",
    "Send a sext to the last person in your phonebook",
    "Show off your orgasm face",
    "Seductively eat a banana",
    "Empty out your wallet/purse and show everyone what's inside",
    "Do your best sexy crawl",
    "Pretend to be the person to your right for 10 minutes",
    "Eat a snack without using your hands",
    "Say two honest things about everyone else in the group",
    "Twerk for a minute",
    "Try and make the group laugh as quickly as possible",
    "Try to put your whole fist in your mouth",
    "Tell everyone an embarrassing story about yourself",
    "Try to lick your elbow",
    "Post the oldest selfie on your phone on Instagram Stories",
    "Tell the saddest story you know",
    "Howl like a wolf for two minutes",
    "Dance without music for two minutes",
    "Pole dance with an imaginary pole",
    "Let someone else tickle you and try not to laugh",
    "Put as many snacks into your mouth at once as you can",
    "Send your most recent selfie.",
    "Send your ugliest selfie.",
    "Send a screenshot of your facebook search history",
    "Send a screenshot of your gallery.",
    "Send a screenshot of your messenger inbox",
    "Tell something very intimate.",
    "Send a screenshot of your twitter inbox",
    "Send a screenshot of your homescreen.",
    "Send a cover of your favorite song. 🎤",
    "Do a lyric prank on someone and send proof.",
    "Confess to your current crush. ❤️",
    "Declare who is your true love.",
    "Send a screenshot of your gallery.",
    "Set your crush’s picture as your dp.",
    "Suggest me more dares.",
)

ABUSE = (
    "போடா 🐕 நாய்",
    "போடா 🐖 பன்றி ",
    "போடா 😤 லூசு",
    "போடா 🦊 நரி",
    "நீ பெரிய முட்டாள்னு எனக்கு எப்பயோ தெரியும்! 😜",
    "லெஃப்ட்ல விட்டா ரைட்ல திரும்பிக்கும் 👊🏻",
    "லூசு மாறி பேசிட்டு இருக்காத! 😏",
    "மூஞ்ச பாரு மூஞ்செலி வாயா 😂",
    "இப்போ என்னவாம்... 😏",
    "என்னப்பா உனக்கு பிரச்சன? 😣",
    "நீந்தாண்ட அது டுபுக்கு 😜",
    "மூடிட்டு போடா வெண்ண! 😂",
    "வேணா சொல்றத கேளு, சொன்னா கேளு வேணா அப்புறம் அழுதுருவ 😢",
    "மண்ட பத்திரம்.🔨⛏",
    "எனக்கு தெரியாது பே 😜",
    "அடிங்கு ஓடி போ நாயே! 🐕",
    "வந்தன்னு வெய் அவ்ளோதான் பாத்துக்க 😠",
    "மூஞ்சியும், மொகரகட்டையும், ஆள பாரு 🙄",
    "ஒரே அடி தான் நீ காலி 😏",
    "ஜிஞ்சர் ஈட்டிங்க் மங்க்கி 🐵",
    "காதலும் கத்திரிக்காயும், போயா வேலைய பாத்துட்டு 😒",
    "என்ன குழந்தாய் 😆...",
    "இது எல்லாம் ஒரு பொழப்பு 🥵 போய் பிச்சை எடு போ",
    "வெட்கமே இல்லையா உனக்கு -த்து 💦💦💦 😂😂🤣",
    "புள்ள குட்டிய படிக்க வெய் போ... 😆",
    "ஒழுங்கா ஓடிரு 👊🏻",
    "இஞ்சி தின்ன கொரங்கு மாறி இருக்க 🐵",
    "ஓ! இது தான் அனியாயத்த கண்டா பொங்குறதா?😁",
    "என்ன கருமம் டா இது 🤮",
    "குருநாதா! இதுக்கு மேல தாங்க முடியாது குருநாதா... 🥶🤬",
    "நீ ஒரு டுபாக்கூர் 😝",
    "ஃப்ராடு தான நீ 😁",
    "நீ மங்குனி அமைச்சர் என்பதை மணிக்கு ஒருமுறை நிரூபித்துக் கொண்டே இருக்கிறாய்! 😂",
    "புடிங்க சார் இவன புடிச்சி ஜெயில்ல போடுங்க சார் ⛓",
    "க்ரீன் க்ரீனா திட்டிருவன் 🤬",
    "ரத்தம் கக்கி சாவு 🙊",
    "காதல் ஒரு காத்து போன பலூன் 😂"
)

SONG = (
    "🎶 ஏதோ ஒன்று என்னை தாக்க யாரோ போல உன்னை பார்க்க... 🎶",
    "🎶 ஹே ரக்கிட் ரக்கிட் ரக்கிட்ட... 🎶",
    "🎶 இனிமே டிக் டாக் எல்லாம் இங்க ஃபேன்ம்மா நேரா டூயட் பாட வாயேன்ம்மா... 🎶", 
    "🎶 காட்டு பயலே கொஞ்சி போடா என்ன ஒருக்கா நீ... 🎶", 
    "🎶 காதல மறக்க நினைச்சு சிரிக்கிறேன் என் காதலி முகத்த நினைச்சு சிரிக்கிறேன் சோகத்தில் லைப்ப நினைச்சு சிரிக்கிறேன் நான் கோவத்த அடக்க முடியல சிரிக்கிறேன்... 🎶", 
    "🎶 ஏ வாத்தி கம்மிங் ஒத்து ஆஹ் ஆஹ் ஏய் ஒத்து தக்க துன்னா டோம்பா டோம்பா... 🎶", 
    "🎶 கதைப்போமா கதைப்போமா கதைப்போமா ஒன்றாக நீயும் நானும்தான் கதைப்போமா கதைப்போமா கதைப்போமா நீ பேச பேச காயம் ஆறுமே... 🎶", 
    "🎶 எதிர் வீட்டு ஹீரோயினி நீ லெமன் மின்ட்டு கூலர்மா நீ ஏதோ கொஞ்சம் கிளாமருதான் நீ அதுகின்னமா... 🎶", 
    "🎶 காத்தோடு காத்தானேன் கண்ணே உன் மூச்சானேன் நீரோடு நீரானேன் உன்கூட மீனானேன்... 🎶", 
    "🎶 தமிழன் என்று சொல்லடா தலை நிமிர்ந்து நில்லடா தரணியை நீ வெல்லடா... 🎶", 
    "🎶 உன்ன நெனச்சு நெனச்சு உருகி போனேன் மெழுகா நெஞ்ச ஒதைச்சு ஒதைச்சு பறந்து போனா அழகா... 🎶", 
    "🎶 யாஞ்சி யாஞ்சி என் நெஞ்சில் வந்து வந்து நிக்குற என்? என்ன சாஞ்சி சாஞ்சி நீ பார்த்து உன்னில் சிக்க வைக்குற என்... 🎶", 
    "🎶 ஏனோ வானிலை மாறுதே மணித்துளி போகுதே மார்பின் வேகம் கூடுதே மனமோ ஏதோ சொல்ல வார்த்தை தேடுதே... 🎶", 
    "🎶 என் கண்ணுகுள்ள ஒரு சிருக்கி கட்டிபுட்டாளே என்ன இருக்கி மனசகட்டி போட மறுத்தாளே ஹய்யோ, ஹய்யையோ... 🎶", 
    "🎶 உனக்கென்ன வேணும் சொல்லு உலகத்தை காட்டச் சொல்லு புது இடம் புது மேகம் தேடி போவோமே... 🎶", 
    "🎶 கடல் தாண்டி போகும் காதலி கை மீறி போகுதே என் விதி நகராமல் நின்று போகுமே என் வாழ்க்கையின் ரதி... 🎶", 
    "🎶 உன் பேரே தெரியாது உன்னை கூப்பிட முடியாது நான் உனக்கோர் பேர் வைத்தேன் உனக்கே தெரியாது... 🎶", 
    "🎶 அடி வெள்ளாவி வச்சுத்தான் வெளுத்தாங்களா உன்ன வெய்யிலுக்கு காட்டாம வளர்த்தாங்களா தலைகாலுப் புரியாம தலைமேல நிற்காம தடுமாறிப் போனேனே நானே நானே...🎶"
 )

JOKE = (
    "தபால்காரர்: இந்த பார்சல குடுக்க அஞ்சு கிலோ மீட்டர் நடந்து வந்தேன் உங்க ஊருக்கு. வீட்டுக்காரர்: ஏன், தபால்ல அனுப்பி இருக்கலாம்ல.?",
    "Pal vali vantha palla pudungalam....Ana... Kaal vali vantha kaala pudunga mudiyuma?! Illa Thalai Vali Vandha, Thaliathan Pudunga Mudiyuma?",
    " Sunday annikku sundai poda mudiyum, aana Monday annikku mandaya pottal vibaraithama aayidum !!!😂😂",
    "Hotela kaasu kodukalana maavata soluvanga aana busla kasu kodukalana bus otta solluvangala?  ", 
    "Thanga chain'a urukkunaa thangam varum.!Velli chain'a urukkunaa VeLLi varum! aana, Cycle chain'a urukkinaa cycle varumaaaa?", 
    "Yerindhu poana Cigarette Saambal sonnadhu Indru Naan Naallai Nee. NO SMOKING Pass it to All.!By Cigarette adikkaadha nallavargall sangam", 
    "Thiruvalluvar 1330 kural ezhidhirundhaalum , avarala oru kuralil thaan paesa mudiyum", 
    "Enna thaan un thalai suthinaalum, un mudhukai nee paakka mudiyumaa?", 
    "School Testla Bit adikalam... College Testla Bit adikalam... Blood Testla Bit addika mudiyuma?", 
    "Kolammavil kolam podalam. Kadalai mavil kadalai poda mudiuma?!", 
    "Life la onnume illa na bore addikum... Thalaila onnume ellana glare addikum...", 
    "7 Paramparaikkku ukkanthu saapida paisa irunthalum... fast food kadaile ninnukittu dhaan saapidanum!", 
    "Engineering Collegela padichu Engineer aagalaam, Presidency collegela padichu president aaga mudiyumaa?!", 
    "Autokku autonu paer irundaalum manual aa thaan drive panna mudiyum...", 
    "Thooka marundhu sappitta thookam varum... Anaa...Irumal marundhu sappitta irumal varathu!", 
    "Vaazha maram thaar podum! Aana adha vachhi road poda mudiyuma?", 
    "Tea cupla tea irukum. Appa World Cupla world irukkuma?", 
    "Paalkova paalil irundhu pannalaam, aana rasagullava rasathil irundhu panna mudiyuma?",
    "திருப்பதிக்கு மொட்டை அடிக்கலாம்னு போனா அங்க ஃபுல்லா ஆம்பளைங்களா மொட்டை அடிச்சு இருந்தாங்க ஏன்? என்னா அது மேல் திருப்பதி",
    "ஒருத்தனுக்கு செம பசியாம் ஸ்ட்ரைட்டா போயிட்டு மழையில நனைந்த உடனே பசி போயிடுச்சாம் ஏன்? ஏன்னா அது அடை மழையாம்",
    "எல்லா காயத்துக்கும் மருந்து போட முடியும் ஆனா ஒரே ஒரு காயத்துக்கு மட்டும் மருந்து போட முடியாது அது என்ன காயம்? ஆகாயம்",
    "என்னதான் ஊரில் வெள்ளம் வந்தாலும் அந்த வெள்ளத்தில் சர்க்கரைப்பொங்கல் பண்ண முடியுமா?!",
    "ஒருத்தர் வேகமா Ration Card எடுத்துட்டு ஒடி போகிறார். அப்போது அவர் அரிசி வாங்குவாரா இல்ல சர்க்கரை வாக்குவாரா? அவரு அரிசி வாங்க மாட்டாரு சர்க்கரையும் வாங்க மாட்டாரு, மூச்சு தான் வாங்குவாரு.",
    "நம்ம வாழ்க்கைல சந்தோஷம் என்பது ராங்கால் மாதிரி எப்பவாச்சும் வரும் ஆனா கஷ்டம் என்பது கம்பெனிக்கால் மாதிரி இம்சை எப்பவும் வரும்"
 )

@Client.on_message(
    filters.command("runs")
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

@Client.on_message(
    filters.command("react")
)
async def react(_, message):
    """ /react strings """
    effective_stringg = random.choice(REACT)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_stringg)
    else:
        await message.reply_text(effective_stringg)

@Client.on_message(
    filters.command("truth")
)
async def truth(_, message):
    """ /truth strings """
    effective_strings = random.choice(TRUTH)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_strings)
    else:
        await message.reply_text(effective_strings)

@Client.on_message(
    filters.command("abuse")
)
async def abuse(_, message):
    """ /abuse strings """
    effective_stringz = random.choice(ABUSE)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_stringz)
    else:
        await message.reply_text(effective_stringz)

@Client.on_message(
    filters.command("dare")
)
async def dare(_, message):
    """ /dare strings """
    effective_stringy = random.choice(DARE)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_stringy)
    else:
        await message.reply_text(effective_stringy)

@Client.on_message(
    filters.command("joke")
)
async def joke(_, message):
    """ /joke strings """
    effective_stringa = random.choice(JOKE)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_stringa)
    else:
        await message.reply_text(effective_stringa)

@Client.on_message(
    filters.command("sing")
)
async def sing(_, message):
    """ /sing strings """
    effective_stringa = random.choice(SONG)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_stringa)
    else:
        await message.reply_text(effective_stringa)
