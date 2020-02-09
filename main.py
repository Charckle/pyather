import subprocess
import pathlib
import glob
import os

VLC_PATH = "C:/Program Files/VideoLAN/VLC/vlc.exe"
VLC_SET = "--qt-continue=2"

#gets path of the location the script is run in
def get_loc_path():
    my_path = pathlib.Path().absolute()
    
    return my_path

def get_ALL_files_in_path(my_path):
    location_path = str(my_path) + '/**/*.*'
    files = glob.glob(location_path, recursive=True)

    for i in files:
        print(i)

def get_dir_in_path(my_path):
    files = os.listdir(my_path)
    
    d_list = []
    for file in files:
        if os.path.isdir(os.path.join(my_path, file)): 
            d_list.append(file)     

    return d_list

def play_video(video_path):
    process = subprocess.Popen([VLC_PATH, VLC_SET, video_path])

if __name__ == "__main__":
    play_video("Lee_Rosevere_-_01_-_Wireless.mp3")