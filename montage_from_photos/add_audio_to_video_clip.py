from moviepy.editor import *

musicclip = AudioFileClip("./testall/_audio_clips/all3merged.mp3")
clip = VideoFileClip("./final_pic_to_vid.mp4")
clip_with_audio = clip.set_audio(musicclip)
clip_with_audio.write_videofile("_output_video_with_3_audio_files.mp4")



