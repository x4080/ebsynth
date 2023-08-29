# Center Block
# ./bin/ebsynth -style result0001.png -guide source0001.png source0004.png -weight 2 -guide map.png map.png -weight 1 -output result0004.png
################ MAKE CHANGES HERE #################
keyframeDir = "keyframes"              # path to the input sequence PNGs
inputDir = "source"              # path to the input sequence PNGs
outputDir = "outputs"              # path to the input sequence PNGs
fileFormat = "%04d"        # name of input files, e.g., %03d if files are named 001.png, 002.png
fileExt = "png"            # extension of input files (without .), e.g., png, jpg
keyframe = "keyframe"           # keyframe for style
FIRST = 1                       # number of the first PNG file in the input folder
CENTER = 5                      # number of the last PNG file in the input folder
LAST = 10
####################################################

firstFrame = CENTER
lastFrame  = FIRST
frameStep  = -1

firstOutputFrame=firstFrame-1

inputFiles = inputDir + "/" + fileFormat + "." + fileExt
outputFiles = outputDir + "/" + fileFormat + "." + fileExt
keyframeFile = keyframeDir + "/" + fileFormat + "." + fileExt

print("cp %s %s"%(keyframeFile%(firstFrame),outputFiles%(firstFrame)))
print("./bin/ebsynth -style %s -guide %s %s -weight 2 -guide map.png map.png -weight 1 -output %s"%(keyframeFile%(firstFrame),inputFiles%(firstFrame),inputFiles%(firstFrame-1),outputFiles%(firstFrame-1)))

for frame in range(firstOutputFrame,lastFrame,frameStep):
  print("./bin/ebsynth -style %s -guide %s %s -weight 2 -guide map.png map.png -weight 1 -output %s"%(outputFiles%(frame),inputFiles%(frame),inputFiles%(frame+frameStep),outputFiles%(frame-1)))

## next
firstFrame = CENTER
lastFrame  = LAST
frameStep  = +1

firstOutputFrame=firstFrame+1

inputFiles = inputDir + "/" + fileFormat + "." + fileExt
outputFiles = outputDir + "/" + fileFormat + "." + fileExt
keyframeFile = keyframeDir + "/" + fileFormat + "." + fileExt

print("./bin/ebsynth -style %s -guide %s %s -weight 2 -guide map.png map.png -weight 1 -output %s"%(keyframeFile%(firstFrame),inputFiles%(firstFrame),inputFiles%(firstFrame+1),outputFiles%(firstFrame+1)))

for frame in range(firstOutputFrame,lastFrame,frameStep):
  print("./bin/ebsynth -style %s -guide %s %s -weight 2 -guide map.png map.png -weight 1 -output %s"%(outputFiles%(frame),inputFiles%(frame),inputFiles%(frame+frameStep),outputFiles%(frame+1)))