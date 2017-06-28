# audioProcessing

This project lets you do extaction of notes present in audio.



### Prerequisites


```
1) python
2) numpy
3) struct
4) wave
```

### Installing

A step by step series of examples that tell you have to get a development env running

```
1) python: download from https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe and install.
2) numpy: open cmd and install this module by using the following command "pip install numpy"

```

And repeat

```
until finished
```



## add audio files 


```
1) save audio file in the same folder as Audio_1, Audio_2 similaraly add more files and change range in code 
  example: if you have 5 audio files than use  "for file_number in range(1,6):"

for file_number in range(1,6):
    file_name = "Audio_"+str(file_number)+".wav"
    sound_file = wave.open(file_name)
    play(sound_file)
    
```

### Result

Run 4269_Audio_Processing.py.py file.
```
F8 B8 E6 E6 C7 G6 A6 A8 B7 G8 D8 F6 E6 A6 D8 
``` 

## License

This project is completed under IIT Bombay.

## Acknowledgments

* my all group members sanjeev, mayank and gaurav.



