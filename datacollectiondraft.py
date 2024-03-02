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


channel1 = []
channel2 = []
channel3 = []
channel4 = []
channel5 = []
channel6 = []
channel7 = []
channel8 = []
channel1 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel2 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel3 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel4 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel5 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel6 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel7 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }
channel8 = { 
        "alpha":[],
        "beta":[],
        "delta":[],
        "gamma":[],
        "theta":[]
    }    

def callback(data):
    frequencies = ["alpha","beta","delta","gamma","theta"]

    freqdict = {
        "alpha" : data['data']['alpha'],
        "beta" : data['data']['beta'],
        "delta" : data['data']['delta'],
        "gamma" : data['data']['gamma'],
        "theta" : data['data']['theta']
    }
   

    for frequency in frequencies:
        channel1[frequency].append(freqdict[frequency][0])
        channel2[frequency].append(freqdict[frequency][1])
        channel3[frequency].append(freqdict[frequency][2])
        channel4[frequency].append(freqdict[frequency][3])
        channel5[frequency].append(freqdict[frequency][4])
        channel6[frequency].append(freqdict[frequency][5])
        channel7[frequency].append(freqdict[frequency][6])
        channel8[frequency].append(freqdict[frequency][7])
    #print(channel1)
    


songname = input("what is the name of the song?: ")
songID = input("what is the ID of the song?: ")
length = int(input("How long, in seconds, is the song?: "))

print("starting data collection in 2 seconds, please play the song")
time.sleep(2)
print("starting now")
unsubscribe = neurosity.brainwaves_power_by_band(callback)
time.sleep(length)
print("song completed. ")
liked = int(input("Do you particularly like this song? I.e. would you listen to it on purpose? Enter 1 or 0: "))
disliked = int(input("Do you particularly hate this song? I.e. does it make your ears bleed? Enter 1 or 0: "))
spectrum = float(input("How much do you like/dislike this song between 0 and 1?"))
file_path = '/home/aditya/Documents/projectmusic_newdelim.csv'
new_data = [songname, liked,disliked,spectrum, songID, str(channel1),str(channel2),str(channel3),str(channel4),str(channel5),str(channel6),str(channel7),str(channel8)]
#new_data = [str(channel1),str(channel2),str(channel3),str(channel4),str(channel5),str(channel6),str(channel7),str(channel8)]
# we can do eval(str(dict)) = dict
# this is because delimiter issue
add_to_csv(file_path, new_data)
print("task completed and added to csv. exitting")

    
