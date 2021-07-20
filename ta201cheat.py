import discord 
import pyautogui
import keyboard  # using module keyboard

const_Api = '756337173724266657'
const_Chan = 756211540495040583
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def ss():
	screenshot = pyautogui.screenshot()
	screenshot.save("screen.png")

async def execute():
	channel = client.get_channel(const_Chan)
	ss()
	await channel.send(file=discord.File('screen.png'))
	await channel.send('?poll test run "a" "b" "c" "d"')

client.run(const_Api)   # const is my api you own api

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        keyboard.press_and_release('ctrl+/'):  # if key 'q' is pressed 
            print('You Pressed A ctrl!')
            continue  # finishing the loop
    except:
        continue

