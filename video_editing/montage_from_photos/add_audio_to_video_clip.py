from moviepy.editor import *

# musicclip = AudioFileClip("Study and Relax.mp3").subclip(0, 6)
# make 20% louder and have fade for 1 second
# musicclip = AudioFileClip("./testall/_audio_clips/27654745671174")#.afx(afx.volumex, 1.2).afx(afx.audio_fadein, 1.0)
musicclip = AudioFileClip("./testall/_audio_clips/all3merged.mp3")

clip = VideoFileClip("./final_pic_to_vid.mp4")
clip_with_audio = clip.set_audio(musicclip)
# final_clip = concatenate_videoclips([clip_v2, clip2, clip3, clip4])
# final_clip.write_videofile("output_3.mp4")
clip_with_audio.write_videofile("_output_video_with_3_audio_files.mp4")

# musicclip = VideoFileClip("./testall/_audio_clips/27654745671174")
# musicclip2 = VideoFileClip("./testall/_audio_clips/27654745733642002")
# musicclip3 = VideoFileClip("./testall/_audio_clips/27654746272614001")
# stitched_audio_clips = concatenate_videoclips([musicclip, musicclip2, musicclip3])
# clip_with_all3_audio = clip.set_audio(stitched_audio_clips)
# clip_with_all3_audio.write_videofile("_output_3_concat_audio.mp4")


