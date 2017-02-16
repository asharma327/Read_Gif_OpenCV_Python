import cv2
import os

'''This is the command to read in the GIF. You need Videocapture which makes a cv2 Video Object.
Add your GIF file name in the parameter of this function.
'''
gif_kiss = cv2.VideoCapture('kiss.gif')


def convert_gif_to_frames(gif):

    # Initialize the frame number and create empty frame list
    frame_num = 0
    frame_list = []

    # Loop until there are frames left
    while True:
        try:
            # Try to read a frame. Okay is a BOOL if there are frames or not
            okay, frame = gif.read()
            # Append to empty frame list
            frame_list.append(frame)
            # Break if there are no other frames to read
            if not okay:
                break
            # Increment value of the frame number by 1
            frame_num += 1
        except KeyboardInterrupt:  # press ^C to quit
            break

    return frame_list


def output_frames_as_pics(frame_list):

    # Reduce the list of frames by half to make the list more managable
    frame_list_reduce = frame_list[0::2]
    # Get the path of the current working directory
    path = os.getcwd()
    # Set then name of your folder
    '''Replace this name with what you want your folder name to be'''
    folder_name = 'Picturebook_Pics_Kiss'
    # If the folder does not exist, then make it
    if not os.path.exists(path + '/' + folder_name):
        os.makedirs(path + '/' + folder_name)

    for frames_idx in range(len(frame_list_reduce)):
        cv2.imwrite(os.path.join(path + '/' + folder_name, str(frames_idx+1) + '.png'), frame_list_reduce[frames_idx])

    pass
