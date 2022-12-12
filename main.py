from scipy.io import wavfile
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-st', '--splitThreshold')
parser.add_argument('-zt', '--zeroThreshold')
parser.add_argument('-f', '--filePath')

args = parser.parse_args()

splitWhenNZeros = 2000 if args.splitThreshold is None else args.splitThreshold # maybe better to use time based value. like 1 second (can be calculated with samplerate)
zeroThreshold = 100 if args.zeroThreshold is None else args.zeroThreshold

filePath = args.filePath
fileName = filePath.split('/')[len(filePath.split('/'))-1]
basePath = '/'.join(filePath.split('/')[:-1]) + "/"

def isInThreshold(data):
    return (data[0] > zeroThreshold*-1 and data[0] < zeroThreshold) and (data[1] > zeroThreshold*-1 and data[1] < zeroThreshold)

samplerate, data = wavfile.read(filePath)
print("Sample rate: " + str(samplerate))

# get index where to split data
splitIndexes = []
counter = 0
for index in range(0, len(data)):
    lastCounterVal = counter
    counter = counter + 1 if isInThreshold(data[index]) else 0
    if lastCounterVal > splitWhenNZeros and counter == 0:
        splitIndexes.append(index-1)
splitIndexes.append(len(data))

# split data by index
splittedValues = []
lastIndex = 0
for index in splitIndexes:
    newData = data[lastIndex:index]
    splittedValues.append(newData)
    lastIndex = index

# first should always be filled with zeros, can be deleted
splittedValues = splittedValues[1:]
    
# remove zeros from each sample at the end
newValues = []
for sample in splittedValues:
    newSample = []
    block = True
    for i in range(len(sample)-1,-1,-1):
        if not isInThreshold(sample[i]):
            block = False
        if not block:
            newSample.append(sample[i])
    newValues.append(newSample)
newValues = [val[::-1] for val in newValues]

print("Sounds count: " + str(len(splittedValues)))
print("Saving as: ")

fileNames = fileName.replace('.wav', '').split('-')
for i in range(0, len(newValues)):
    fileName = fileNames[i]
    if len(fileNames) != len(newValues):
        fileName = str(i)
    print("     - " + str(fileNames[i]) + '.wav')
    wavfile.write(basePath + str(fileNames[i]) + '.wav', samplerate, np.array(newValues[i], dtype=np.int16))