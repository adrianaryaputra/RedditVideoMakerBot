import random 
import os

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.fx.all import volumex
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

backsound_folder = "assets/backsounds/"
backsound_file = random.choice(os.listdir(backsound_folder))
backsound_path = backsound_folder + backsound_file
print(f"backsound_file: ", backsound_path)


audioclip = AudioFileClip(backsound_path).set_duration(10)
print(audioclip.duration)
# audioclip.write_audiofile('test.mp3')