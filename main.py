import subprocess
import pathlib
from modules import pylavor
import glob
import os
import mimetypes

VLC_PATH = "C:/Program Files/VideoLAN/VLC/vlc.exe"
VLC_SET = "--qt-continue=2"

def is_video(file):
    mimetypes.init()
    mimestart = mimetypes.guess_type(file)[0]
    
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
    
        if mimestart == 'video':
            return True
        
        else:
            return False

def is_audio(file):
    mimetypes.init()
    mimestart = mimetypes.guess_type(file)[0]
    
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
    
        if mimestart == 'audio':
            return True
        
        else:
            return False

#gets path of the location the script is run in
def get_loc_path():
    my_path = str(pathlib.Path().absolute())
    
    return my_path

def get_ALL_files_in_path(my_path):
    location_path = str(my_path) + '/**/*.*'
    files = glob.glob(location_path, recursive=True)

    return files

def get_all_video_files(my_path):
    all_videos = [i for i in get_ALL_files_in_path(get_loc_path()) if is_video(i)]
    
    return all_videos

def get_dir_in_path(my_path):
    files = os.listdir(my_path)
    
    d_list = []
    for file in files:
        if os.path.isdir(os.path.join(my_path, file)): 
            d_list.append(file)     

    return d_list

def add_main_dir(m_dir):
    #check if given directory exists
    if not os.path.isdir(m_dir):
        return False
    
    #if it exists
    else:
        json_maste_file = "master_dirs.json"
        master_directories = {}

        if not os.path.isfile("data/" + json_maste_file):
            master_directories = {}
            pylavor.json_write("data", json_maste_file, master_directories)

        else:
            master_directories = pylavor.json_read("data", json_maste_file)

            #check if the directory is already on the list
            for i, b in master_directories.items():
                if i == m_dir:
                    return False
            
        #check all files in the master folder
        all_directories_in_master = get_dir_in_path(m_dir)
        master_directories[m_dir] = all_directories_in_master

        pylavor.json_write("data", json_maste_file, master_directories)

def get_files_from_all_masters():

    json_maste_file = "master_dirs.json"
    master_directories = {}

    if not os.path.isfile("data/" + json_maste_file):
        master_directories = {}
        pylavor.json_write("data", json_maste_file, master_directories)

    else:
        master_directories = pylavor.json_read("data", json_maste_file)

        #check if the directory is already on the list
        for i, b in master_directories.items():
            if i == m_dir:
                return False
        
    #check all files in the master folder
    all_directories_in_master = get_dir_in_path(m_dir)
    master_directories[m_dir] = all_directories_in_master

    pylavor.json_write("data", json_maste_file, master_directories)

def play_video(video_path):
    process = subprocess.Popen([VLC_PATH, VLC_SET, video_path])

if __name__ == "__main__":
    print([i for i in get_ALL_files_in_path(get_loc_path()) if is_video(i)])
    
    #print(is_audio())
    #add_main_dir(get_loc_path())
    #play_video("Lee_Rosevere_-_01_-_Wireless.mp3")
