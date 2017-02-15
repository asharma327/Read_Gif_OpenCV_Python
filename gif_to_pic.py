import cv2
import os

'''This is the command to read in the GIF. You need Videocapture which makes a cv2 Video Object'''
gif_soccer = cv2.VideoCapture('test_gif.gif')


def convert_gif_to_frames(gif):

    frame_num = 0
    frame_list = []
    while True:
        try:
            # Try to read a frame
            okay, frame = gif.read()
            frame_list.append(frame)
            if not okay:
                break
            frame_num += 1
        except KeyboardInterrupt:  # press ^C to quit
            break

    return frame_list


def output_frames_as_pics(frame_list):

    frame_list_reduce = frame_list[0::2]

    path = os.getcwd()

    if not os.path.exists(path + '/Picturebook_Pics'):
        os.makedirs(path + '/Picturebook_Pics')

    for frames_idx in range(len(frame_list_reduce)):
        cv2.imwrite(os.path.join(path + '/Picturebook_Pics', str(frames_idx+1) + '.png'), frame_list_reduce[frames_idx])

    pass





