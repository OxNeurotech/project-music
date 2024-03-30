NEUROSITY_EMAIL=""
NEUROSITY_PASSWORD=""
NEUROSITY_DEVICE_ID=""

from neurosity import NeurositySDK
neurosity = NeurositySDK({
    "device_id": NEUROSITY_DEVICE_ID,
})

neurosity.login({
    "email": NEUROSITY_EMAIL,
    "password": NEUROSITY_PASSWORD
})

import sys 
import time 
import csv

def add_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)




calm = []
def callback(data):
    calm.append(data['probability'])
    print(data['probability'])
    

listening = input("are you listening to a song, white noise, or nothing? 0 for nothing, 1 for white noise, 2 for song: ")
if(int(listening)==2):
    songname = input("what is the name of the song?: ")
    songID = input("what is the ID of the song?: ")
    length = int(input("How long, in seconds, is the song?: "))
else:
    songname = "none"
    songID = "none"
    length = int(input("How long dyu wanna listen for?: "))


print("starting data collection in 2 seconds, please play the song")
time.sleep(2)
print("starting now")
unsubscribe = neurosity.calm(callback)
time.sleep(length)
unsubscribe()
print("song completed. ")

if(int(listening)==2):
    liked = int(input("Do you particularly like this song? I.e. would you listen to it on purpose? Enter 1 or 0: "))
    disliked = int(input("Do you particularly hate this song? I.e. does it make your ears bleed? Enter 1 or 0: "))
    spectrum = float(input("How much do you like/dislike this song between 0 and 1?"))
else:
    liked = 0
    disliked = 0
    spectrum = 0

file_path = '/home/aditya/Documents/projectmusic_calm.csv'
new_data = ["placeholder",listening, liked, disliked, spectrum, songname, songID, calm]
#new_data = [str(channel1),str(channel2),str(channel3),str(channel4),str(channel5),str(channel6),str(channel7),str(channel8)]
# we can do eval(str(dict)) = dict
# this is because delimiter issue
add_to_csv(file_path, new_data)
print("task completed and added to csv. exitting")

    
