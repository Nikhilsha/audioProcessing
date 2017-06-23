####################################################################################
#			    Musical Note Identification			           #												   
#			       Team-Id: eYRC-BV#4269			           #				   
#									           #									   
####################################################################################

import numpy as np
import wave
import struct

############################## Some Useful Variables ###############################
window_size          =  441      # Size of window to be used for detecting silence
sound_temp_sqr_sum   =  0        # Silence detection parameter
max_notes            =  20       # Maximum number of notes in file, for efficiency
sampling_freq        =  44100	 # Sampling frequency of audio signal
upr_lmt_err          =  1.94     # Maximum upper deviation of output frequency from standard frequency
lwr_lmt_err          = -1.7      # Maximum lower deviation of output frequency from standard frequency

def play(sound_file):
    
    ############sound_file-- a single test audio_file as input argument#############
    print('\n')
    file_length = sound_file.getnframes()
    sound = np.zeros(file_length)
    for i in range(file_length):
        data = sound_file.readframes(1)
        data = struct.unpack("<h", data)
        sound[i] = int(data[0])
    sound = np.divide(sound, float(2**15))
    sound_sqr=np.square(sound)
    
    ############################# Detecting Silence ################################
    block = int(file_length/window_size)
    sound_temp_sqr_sum = np.zeros(block)
    for i in range(block):
        sound_temp_sqr= np.zeros(window_size)
        for j in range(0,window_size):
            sound_temp_sqr[j]=sound_sqr[(i*window_size)+j]
        sound_temp_sqr_sum[i]=sum(sound_temp_sqr)
        #print(i,sound_temp_sqr_sum[i])    #uncomment to see the location of silence
        
    ########################### Calculating Frequencies ############################        
    loc1 = 0
    loc2 = 0
    freq_loc = 0
    freq_s = np.zeros(file_length)
    for i in range(block):
        if sound_temp_sqr_sum[i] == 0.0:
            if i != block-1:
                if sound_temp_sqr_sum[i+1] != 0.0:
                    if loc1 == 0:
                        loc1 = i+1
        if sound_temp_sqr_sum[i] != 0.0:
            if i != block:
                if sound_temp_sqr_sum[i+1] == 0.0:
                    if loc2 == 0:
                        loc2 = i
                        x = loc1*window_size
                        y = loc2*window_size
                        data = np.zeros(file_length)
                        sound_file = wave.open("Audio_"+str(file_number)+".wav")
                        file_length =sound_file.getnframes()
                        data = sound_file.readframes(file_length)
                        data = struct.unpack('{n}h'.format(n=file_length), data)
                        a = data[x:y]
                        loc1 = 0
                        loc2 = 0
                        note = np.array(a)
                        w = np.fft.fft(note)
                        freqs = np.fft.fftfreq(len(w))
                        idx = np.argmax(np.abs(w))
                        freq = freqs[idx]
                        freq_a1= abs(freq * sampling_freq)
                        freq_s[freq_loc]=freq_a1
                        freq_loc = freq_loc+1                
    for i in range(file_length):
        if freq_s[i] !=0:
            #print(i+1,freq_s[i])   # uncomment to see the values of frequencies
            n=i
            
############## Assigning Name to The Frequencies, Displaying Result ##############             
    list1=[1760,3520,7040,1975.53,3951.07,7902.13,1046.50,2093,4186.01,1174.66,2349.32,
           4698.62,1318.51,2637.02,5274.04,1396.91,5587.65,1567.98,3135.96,6271.93]
    list2=["A6","A7","A8","B6","B7","B8","C6","C7","C8","D6","D7","D8","E6","E7",
           "E8","F6","F8","G6","G7","G8"]
    list3=freq_s
    k=0
    j=0
    for j in range(n+1):                   
        k=0 
        for k in range(max_notes):          
                x=list1[k]
                y=list3[j]
                diff_1=(x-y)
                if (lwr_lmt_err<=diff_1<upr_lmt_err): 
                    print(list2[k], end=' ')   #IMPORTANT# Displaying Result  ##
        k=k+1
    j=j+1
    return

############################### Read Audio File ################################
for file_number in range(1,6):
    file_name = "Audio_"+str(file_number)+".wav"
    sound_file = wave.open(file_name)
    play(sound_file)

