# WavSampleSplitter

Hi! **WavSampleSplitter** allows you to easily split WAV files into multiple sounds.

## Options

|Argument|Info|Default|
|-|----|-------|
|-st / --splitThreshold|How many zero values in succession until split detection|2000|
|-zt / --zeroThreshold |How much can data deviate from zero and still be detected as zero|100|

## Usage
### Your sample
First off, you should check if your individual sounds do not overlap and have sufficient spacing at the beginning and in between the notes.

Example:
![ ](/doc/input.JPG)

### Split
To split the WAV file, just drag and drop your sample onto the executable. After a short while you should see the individual files appear.

Example:
![ ](/doc/output.JPG)

Output:
```bash
Sample rate: 44100
Sounds count: 7
Saving as:
     - 1.wav
     - 2.wav
     - 3.wav
     - 4.wav
     - 5.wav
     - 6.wav
     - 7.wav
```

### Automatic naming
If you want to automatically name your files, you can use the following naming convention for the input file:
`name1-name2-name3-name4-....`

Example:
`kick-snare-bass_1-bass_2-bass_3-bass_4-hi_hat.wav`

Output:
```bash
Sample rate: 44100
Sounds count: 7
Saving as:
     - kick.wav
     - snare.wav
     - bass_1.wav
     - bass_2.wav
     - bass_3.wav
     - bass_4.wav
     - hi_hat.wav
```




Bugs:
- Pipeline release => notes are not parsed correctly. always empty