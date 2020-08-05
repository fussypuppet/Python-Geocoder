import os
from dotenv import load_dotenv
import geocoder

load_dotenv()

theseSites = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge'
]

for thisSite in theseSites:
    thisPlace = geocoder.bing(thisSite, key=os.getenv('BING_KEY'))
    print(f'{thisSite} is located at ({round(thisPlace.lat,4)}, {round(thisPlace.lng,4)})')
