
from array import array
from collections import defaultdict
from email import message
from glob import glob
from multiprocessing.dummy import Array
from threading import local
import telebot
import time
import re;
from geopy.geocoders import Nominatim
from telebot import types
from requests import delete
import telebot
import time
from geopy.geocoders import Nominatim
from telebot import types

#2066771132:AAFlCE6BvDffTdxxWlyp70GBSl3RM1ZqczM //test_bot
#2065941048:AAG708pdvBxJpHTx27416c76MaNEkTzGz1o //satka
#5840423885:AAEEaF8f8Lf8tdQTF9nsjPR2cQnqFOnLTZs
bot = telebot.TeleBot('5840423885:AAEEaF8f8Lf8tdQTF9nsjPR2cQnqFOnLTZs')


markup = types.InlineKeyboardMarkup(row_width=3)
markup2 = types.InlineKeyboardMarkup(row_width=3)
markup3 = types.InlineKeyboardMarkup(row_width=3)
markup4 = types.InlineKeyboardMarkup(row_width=3)
markup5 = types.InlineKeyboardMarkup(row_width=3)
markup6 = types.InlineKeyboardMarkup(row_width=3)
markup7 = types.InlineKeyboardMarkup(row_width=3)
markup8 = types.InlineKeyboardMarkup(row_width=3)
markup9 = types.InlineKeyboardMarkup(row_width=3)
markup10 = types.InlineKeyboardMarkup(row_width=3)
markup11 = types.InlineKeyboardMarkup(row_width=3)

markupmain = types.ReplyKeyboardMarkup(resize_keyboard=True)

item1 = types.KeyboardButton("F.A.Q")
item2 = types.KeyboardButton("Links")
item3 = types.KeyboardButton("Litepaper")
item4 = types.KeyboardButton("Map")
item7 = types.InlineKeyboardButton("Next [2/12]", callback_data='next1')
item8 = types.InlineKeyboardButton("Next [3/12]", callback_data='next2')
item9 = types.InlineKeyboardButton("Next [4/12]", callback_data='next3')
item10 = types.InlineKeyboardButton("Next [5/12]", callback_data='next4')
item11 = types.InlineKeyboardButton("Next [6/12]", callback_data='next5')
item12 = types.InlineKeyboardButton("Next [7/12]", callback_data='next6')
item13 = types.InlineKeyboardButton("Next [8/12]", callback_data='next7')
item14 = types.InlineKeyboardButton("Next [9/12]", callback_data='next8')
item15 = types.InlineKeyboardButton("Next [10/12]", callback_data='next9')
item16 = types.InlineKeyboardButton("Next [11/12]", callback_data='next10')
item17 = types.InlineKeyboardButton("Next [12/12]", callback_data='next11')
app = Nominatim(user_agent="Diplom")

markup.add(item7)
markup2.add(item8)
markup3.add(item9)
markup4.add(item10)
markup5.add(item11)
markup6.add(item12)
markup7.add(item13)
markup8.add(item14)
markup9.add(item15)
markup10.add(item16)
markup11.add(item17)
markupmain.add(item1, item2, item3, item4)


def get_location_by_address(address):
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)

def test_send_message_with_markdown(self):
    tb = telebot.TeleBot(TOKEN)
    markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """
    ret_msg = tb.send_message(CHAT_ID, markdown, parse_mode="Markdown")
    assert ret_msg.message_id

@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
	try:
		if call.message:
			if call.data == 'next1':
				picn1 = 'https://ibb.co/G5mJhgZ'
				bot.send_photo(call.message.chat.id, picn1, caption='*A glimpse into the future [2/12]*\n\nWe need to anticipate where technology will lead us. PARAVERSE will first be \naccessible through the camera of *your smartphone*.\n\nThe future of PARAVERSE does not rely \non smartphones as this will be a *hardware-independent platform*.\nWith the advent of Augmented Reality \nGlasses, PARAVERSE will be completely \nimmersive, allowing users to fully interact and explore seamlessly a virtual \nworld overlaid on top of reality.\nFor years, *Google, Apple, Meta and Microsoft* have been heavily investing ', parse_mode='Markdown', reply_markup=markup2)
			if call.data == 'next2':
				picn2 = 'https://ibb.co/SXZ33hs'
				bot.send_photo(call.message.chat.id, picn2, caption='*A ONE-STOP PLATFOR [3/12]*\n\nThe PARAVERSE platform will feature a *map* of the \nworld, allowing users to easily navigate and discover the AR Lands composing it. We plan to integrate a native marketplace where users can buy \nand sell *AR Lands* as well as other digital assets.\nThe app will also gradually provide a range of other features.\n\n*Find-to-Earn (F2E)* will be introduced at launch, along with a system of quests to \ngamify the PARAVERSE experience.\n*Finally, as AR technology* continues to evolve, we \nare also anticipating the future by planning to port \nthe PARAVERSE platform to AR Glasses devices when they hit the market.\n\nThis will bring our vision of a fully immersed *AR Metaverse to life*.', parse_mode='Markdown', reply_markup=markup3)
			if call.data == 'next3':
				picn3 = 'https://ibb.co/t8vtZ4N'
				bot.send_photo(call.message.chat.id, picn3, caption='*AR Lands introduction [4/12]*\n\nIn PARAVERSE, the real world is augmented with a virtual layer divided into hexagonal Augmented Reality Lands.\nThese AR Lands are linked to specific real-world locations via GPS coordinates.\n\nTo ensure true ownership and control over AR Lands, PARAVERSE leverages the power of NFTs on the Ethereum blockchain.\n This means that each AR Land is unique, verifiable and secure. It also allows ownership\n of a virtual AR Land to be easily transferable, enabling users to trade them.\nAs space is a limited resource in the real world, the number of AR Lands will also be limited\n\nFinally, AR Lands are not equal in PARAVERSE. \nThey are divided into 5 levels of rarity, from the rarest to the most common: *Legendary, Epic, Rare, Uncommon, and Common.*\nThe rarity of an AR Land affects its size, location and the benefits provided to the owner', parse_mode='Markdown', reply_markup=markup4)
			if call.data == 'next4':
				picn4 = 'https://ibb.co/1qcYKY0'
				bot.send_photo(call.message.chat.id, picn4, caption='*Genesis City [5/12]*\n\nThe launch of PARAVERSE will be a gradual process, with cities being integrated into our AR Metaverse in batches.\nThis gradual integration will be marked by Genesis events.\n\nAn Introduction to PARAVERSE Genesis events will include several Genesis Cities each time, and those are key to the PARAVERSE world. They mark the integration of a country into PARAVERSE by overlaying the virtual world on the real world\n\nThe *first Genesis* event will include 4 Genesis Cities : *Seoul, Tokyo, New York and Paris*, which means that PARAVERSE will first be launched *in South Korea, Japan, the United States and France*', parse_mode='Markdown', reply_markup=markup5)
			if call.data == 'next5':
				picn5 = 'https://ibb.co/vkh6X5H'
				picn51 = 'https://ibb.co/h7gJXWX'
				picn52 = 'https://ibb.co/9rPGzRW'
				bot.send_photo(call.message.chat.id, picn5, caption='*AR LANDNOMICS [6/12]*\n\nThe LANDNOMICS of the 1st Genesis event:\nA total of *1,200 Genesis AR Lands*, distributed as follows:', parse_mode='Markdown')
				time.sleep(2)
				bot.send_photo(call.message.chat.id, picn51, caption='*800* will be given to whitelisted members of our community for free (*Free Mint*), *396* will be kept for PARAVERSE’s ecosystem growth and 4 are Legendary AR Lands that will be put to auction.\nThe distribution is equally divided between the 4 Genesis Cities: *Seoul, Tokyo, New York and Paris*', parse_mode='Markdown')
				time.sleep(2)
				bot.send_photo(call.message.chat.id, picn52, caption='*Distribution of AR Lands rarity in Seoul*\nSame distribution for Tokyo, New York and Paris', parse_mode='Markdown', reply_markup=markup6)
			if call.data == 'next6':
				picn6 = 'https://ibb.co/mBKpTMK'
				bot.send_photo(call.message.chat.id, picn6, caption='*Land Exploration [7/12]*\n\nOnce a Genesis event is complete, meaning all the allocated Genesis AR Lands have been minted, *PARAVERSE is officially launched in countries where a Genesis City is based*\nThis means that, all over a country, unknown AR Lands will be waiting to be discovered and acquired by explorers.\n\nIn other words, *users will be able to discover and mint these AR Lands through PARAVERSE’s Exploration feature.*\n\n*Legendary AR Lands* cannot be obtained through Exploration. *Only Epic, Rare, Uncommon and Common AR Lands* can be acquired this way.The rarity level of a newly explored AR Land will be *revealed after minting*.\nAcquiring an AR Land through Exploration will be possible in several ways, and it will require *the use of PARAVERSE tokens*.\nDetailed information about the Exploration feature will be provided at a later stage.', parse_mode='Markdown', reply_markup=markup7)
			if call.data == 'next7':
				picn7 = 'https://ibb.co/VmGSLt8'
				bot.send_photo(call.message.chat.id, picn7, caption='*Benefits of owning an AR Land [8/12]*\n\nRegardless of rarity, owning an AR Land opens the doors to a world of benefits.\n\n*1. Complete control over the content* (AR digital assets) displayed on your AR Land, allowing you to create AR experiences, organize contests and events, etc.\n\n*2. Earn PARAVERSE tokens:*\n- Earn tokens based on users’ activity on your AR Land.\n- In the future, earn tokens by renting your AR Land to users and companies.\n\n*3. Your AR Land’s value*: the more entertaining the content on your AR Land is, the more users might visit, which means the potential value of your land can increase\n\nHowever, that is just the tip of the iceberg.\n*The level of rarity of an AR Land affects its size, location and the benefits granted to its owner*.\nHere is a table of the benefits given to the owners of AR Lands acquired during the *1st Genesis event.*', parse_mode='Markdown', reply_markup=markup8)
			if call.data == 'next8':
				picn8 = 'https://ibb.co/6tYjhZp'
				bot.send_photo(call.message.chat.id, picn8, caption='*Find-to-Earn (F2E) [9/12]*\n\n*Find-to-Earn* (F2E) is a treasure hunt feature in PARAVERSE using AR, geolocation and blockchain technology. \nThis provides a unique experience for all users as they *explore, find treasures and potentially earn tokens and NFTs* from it.\n\nTo engage in F2E, *users must have AR Glasses NFTs* which allow them to locate and find treasures. The tier and characteristics of a user’s AR Glasses have a direct impact on their ability to efficiently discover NFTs and tokens.\nThe AR Glasses also have *5 tiers*, from the rarest to the most common:*Cosmos, Galaxy, Stellar, Solar and Lunar*.\nEvery newly registered PARAVERSE user will receive *Lunar AR Glasses for free*.\nHigher tiers AR Glasses can be obtained from the AR Glasses Box.\nThose are airdropped to the 1,200 AR Lands owners after a snapshot is taken some time after the Genesis event', parse_mode='Markdown', reply_markup=markup9)
			if call.data == 'next9':
				picn9 = 'https://ibb.co/7kBNNhQ'
				bot.send_photo(call.message.chat.id, picn9, caption='*A community-driven AR Metaverse. [10/12]*\n\nWe believe in *the power of community*.\nUltimately, we aim to build a dynamic community where everyone can contribute to and benefit from PARAVERSE.\nOur ecosystem will be designed to encourage collaboration and reward creativity, bringing together 3D creators, artists, brands, users and AR Land owners\n\n*Users - Explore and interact with the world*\nUsers will first be able to engage in AR treasure hunts through our F2E featureand display their NFTs in AR in PARAVERSE.\nLater, users will be able to immersethemselves in a world of endless AR experiences, from art to entertainment.*Brands and companies - Connect with customers through AR technology.*\n\nPARAVERSE offers *a brand new communication and advertising channel* to showcase products and services through AR exhibitions, promotions and other marketing activities.\n\nCompanies can own their own AR Lands or pay to rent an AR Land in the locations they wish to communicate and advertise.', parse_mode='Markdown', reply_markup=markup10)
			if call.data == 'next10':
				picn10 = 'https://ibb.co/VgTQr39'
				picn10_1 = 'https://ibb.co/jwBvMdv'
				bot.send_photo(call.message.chat.id, picn10, caption='*PARAVERSE TOKEN [11/12]*\n\nPARAVERSE will have its own native token to support its economy (name and ticker are TBA).\n\n*Our native token will be used for all transactions within PARAVERSE*, including trading AR assets, upgrading AR Glasses, exploring and acquiring unknown AR Lands, and much more. We can’t wait to share more, but further information will be revealed at a later stage in 2023, so stay tuned!', parse_mode='Markdown')
				time.sleep(2)
				bot.send_photo(call.message.chat.id, picn10_1, caption='*PARAVERSE TEAM*\n\nPARAVERSE is a project run by *Imagineers, a leading AR company in Korea* with over 30 partnerships. We’re leveraging our expertise in AR technology to launch PARAVERSE. Our team is composed of more than 10 employees and the CEO is *JinSung Kim (Neo)*.', parse_mode='Markdown', reply_markup=markup11)
			if call.data == 'next11':
				picn11 = 'https://ibb.co/3FwBrsM'
				bot.send_photo(call.message.chat.id, picn11, caption='*JOIN,\nSUPPORT,\nAND CONTRIBUTE \nTO PARAVERSE\n[12/12]*\n\nIf PARAVERSE piques your interest, *follow us on social media for more information* and to keep up with our latest announcements. \nIf you have questions or suggestions related to our project, contact us through our official Discord.Thank you for your support.\n\nBe sure to look at the "Links", there will be all the links\nThank you for watching to the end, I worked on the bot: XXXXXEW', parse_mode='Markdown', reply_markup=markupmain)
	except Exception as e:
		print(repr(e))


def is_part_in_list(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return True
    return False

@bot.message_handler(commands=['start'])
def welcome(message):
	chatid = message.chat.id
	bot.send_message(message.chat.id, "Hello, *{0.first_name}*!\nNow I will tell you a little information about such a project as *Paraverse*.\n\nSupply: *1 200 NFT*\nMint date: *TBA*\nPrice: *Free*\nBlockchain: *Ethereum*".format(message.from_user, bot.get_me()),parse_mode='Markdown',reply_markup=markupmain)
	time.sleep(2)
	bot.send_message(message.chat.id, "I also recommend you to visit the Twitter of the project https://twitter.com/paraverse_world")
	bot.send_message(message.chat.id, "And don't forget about the discord https://discord.com/invite/paraverse")
	#time.sleep(2)
	#bot.send_message(message.chat.id, "Мне нравится: \n1.Ухаживать за животными\n2.Обслуживать машины, приборы (следить, регулировать)", reply_markup=markups1)
	
FAQ = ["F.A.Q"]
link = ["Link","link","Links"]
litepaper = ["LitePaper", "litepaper", "Litepaper"]
maps = ["map","maps"]

#\n\nLinks:\nWebsite:https://www.paraverse.world/ \nTwitter:https://twitter.com/paraverse_world \nDiscord:https://discord.com/invite/paraverse

@bot.message_handler(content_types=['text'])
def tgbot(message):

	if message.chat.type == 'private':
		if is_part_in_list(message.text, FAQ) :
			pic1 = 'https://ibb.co/mDtv46Q'
			bot.send_photo(message.chat.id, pic1, caption='What is a Paraverse? 👀 \n- Perverse is a collection of *1,200 earths*, an augmented reality metaverse that will change the way we interact with the world.\n\nMint Date?\n- The date of minting is not yet known, approximately the end of *April* or the beginning of *May*.\n\nWhat is the mint price?\n- *Free*',parse_mode='Markdown', reply_markup=markupmain)
		elif is_part_in_list(message.text, link):
			pic3 = 'https://ibb.co/pZ9Svjf'
			bot.send_photo(message.chat.id, pic3, caption='Links:\nWebsite: https://www.paraverse.world/ \nTwitter: https://twitter.com/paraverse_world \nDiscord: https://discord.com/invite/paraverse \n\nTeams:\nfour4dj: https://twitter.com/four4dj\nAirJ: https://twitter.com/Jehyn_SBT\nCas: https://twitter.com/lami220529\nJQuan: https://twitter.com/Marting55305594\n\nAdvisor:\nBigRat: https://twitter.com/HoneyRatDAO\n\nModerators:\nZoe: https://twitter.com/Xiangwei614\nKaban: https://twitter.com/APustoxin\nCryptoBoy: https://twitter.com/Crypto_Boy911\nYeioa: https://twitter.com/Yeioaaaa\n꺼비: https://twitter.com/seulkirowoon\nFORTUNE: https://twitter.com/Olamile39718043\n\nThe creator of the bot: https://twitter.com/xx_xxxxxew', reply_markup=markupmain)
		elif is_part_in_list(message.text, maps):
			bot.send_message(message.chat.id, 'The developers of the Paravers project are located at the address "Ttukseom-ro 13-gil 38, Seongdong-gu, Seoul", you can personally come to them and discuss with them!')
			location = get_location_by_address("Ttukseom-ro 13-gil 38, Seongdong-gu, Seoul")
			latitude = location["lat"]
			longitude = location["lon"]
			bot.send_location(message.chat.id, latitude, longitude)
		elif is_part_in_list(message.text, litepaper):
			pic4 = 'https://ibb.co/1GCN11N'
			bot.send_photo(message.chat.id, pic4, caption='*Introduction [1/12]*\n\nIntroducing PARAVERSE, an Augmented Reality Metaverse that will transform \nthe way we interact with the world.\nWe are harnessing the power of *cutting-edge technologies* like Augmented \nReality, blockchain and geolocation to create an unparalleled experience that \nblends the digital and physical realms.\n\nMinority Report (2002) envisioned a future where AR technology is completely \nintegrated into our daily lives.\nFast forward to 2023 and the augmented world is within reach.\nWe are now closer than ever to *realizing* this vision and PARAVERSE \naims to be a catalyst for this revolution, driving the growth and widespread \nadoption of the augmented world.'.format(message.from_user, bot.get_me()),parse_mode='Markdown',reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'I do not know what to answer 😢', reply_markup=markupmain)

@bot.message_handler(content_types=['text'])
def tgbot(message):
	bot.send_message(message.chat.id, 'I do not know what to answer 😢', reply_markup=markupmain)


def delete(message):
      bot.delete_message(message.chat.id, message.message_id)


# RUN
bot.polling(none_stop=True)