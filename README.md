# Read_Gif_OpenCV_Python
Read a GIF using OpenCV and convert it into still pictures. You can then print the pictures to make a flipbook :) 

BEFORE EXECUTION, READ IN THE GIF USING THE FOLLOWING COMMAND:
gif = cv2.VideoCapture('test_gif.gif')

The script has two functions:

def convert_gif_to_frames(gif): converts gif into a list of all frames/stills 

def output_frames_as_pics(frame_list): takes the output from convert_gif_to_frames, reduces the list by half to avoid overpopulation and outputs all images into a new folder in your working directory
