import os
import glob
import gtts
from gtts import gTTS
import pandas as pd
from pydub import AudioSegment, audio_segment

#This function is used to generate the skeleton
def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')

    #1. Generate "Kripiya dhyan dijiye"
    #This is the time duration in mili seconds
    start=0000 
    finish=3000
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format="mp3")

    #4. Generate "ke rasthe"
    start=9000
    finish=9900
    audioProcessed=audio[start:finish]
    audioProcessed.export('4_hindi.mp3',format="mp3")

    #6. Generate "ko jane wali apna nirdaridh samay" 
    start=10600
    finish=13300
    audioProcessed=audio[start:finish]
    audioProcessed.export('6_hindi.mp3',format="mp3")

    #8. Generate "minute par platform number"
    start=16000
    finish=17800
    audioProcessed=audio[start:finish]
    audioProcessed.export('8_hindi.mp3',format="mp3")

    #10. Generate "se jayegi"
    start=18500
    finish=22000
    audioProcessed=audio[start:finish]
    audioProcessed.export('10_hindi.mp3',format="mp3")


#This function generate the Train name and number to hindi language
def textToSpeechHindi(text, filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)


#This function used to merge all the mp3 which are generated
def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

#This function used to generate announcement
def generateAnnouncement(filename):
    excelFile=pd.read_excel(filename)
    print(excelFile)
    for index, item in excelFile.iterrows():

        #2. Generate Train name and number
        textToSpeechHindi(item['Train no.']+"  "+item['Train_name'],'2_hindi.mp3')

        #3. Generate via 
        textToSpeechHindi(item['Via'],'3_hindi.mp3')

        #5. Generate To city
        textToSpeechHindi(item['To'],'5_hindi.mp3')

        #7. Generate time 
        textToSpeechHindi(item['Timings'],'7_hindi.mp3')

        #9. Generate time 
        textToSpeechHindi(item['Platform'],'9_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,11)]   #This generate the mp3 of Train number,name , via city , destination city , timings and platform

        announcement=mergeAudios(audios)
        announcement.export(f"Announcement_{item['Train no.']}.mp3",format="mp3")
    

#It is the main function of our project
if __name__ == "__main__":
    for filename in glob.glob("D:\python\railway_announcement\Announcement*"):
        os.remove(filename) 
    print("\n")
    print("Generating Skeleton...Wait for a while...")
    generateSkeleton()
    print("Skeleton Generated Successfully.")
    print("Generating Announcement...Wait for a while...")
    generateAnnouncement("time.xlsx")
    for i in range(1,11):
        os.remove(f"{i}_hindi.mp3")
    print("Announcement Generated Successfully.")  
    print("\n")      