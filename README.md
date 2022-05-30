https://www.youtube.com/watch?v=pOnKsGiTVuk&ab_channel=FourgeesGaming
# Python / FastAI CNN - Playing any racing game
> This code was used to gather and process data while playing any racing games or side scroller. Currently working with Diddy Kong Racing.
> The network was then trained using the FastAI Libary. The original scope of this project was to fork the code from windows to linux.

## Setup
- I used OBS virtual cam (using loopback driver for linux) and with a game window capture playing at a 800 X 600 resolution fed into open cv2 as a webcam input.
- You can start data collection by running CreateData.py. This code was tested on Ubuntu 20.04.
- Pressing esc will start the screen / key grab. These will be stored in lists until the episode is done. Press h to end and save.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.
- Then I used a script in util folder called CreateImages.py to put then onto a disk drive in folders corresponding to their actions.

## Train
- Use the file called training.py or use the google colab that is provided here. (It's faster and easier)
- Point it at your image directory

## Run Agents
- Fully random agent is RandomAgent.py
- Trained Agent is TrainedAgent.py
- You will have to load in the pkl created from training.

## Inputs (Observations)
- Uses inputs to the nural network (Observations) of pixels in the game.
- 224 X 224
- Line detection (might change it to just b&w, testing this currently)

## Contact!
- Plz don't
