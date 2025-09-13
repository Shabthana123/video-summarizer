import os

# 🔧 Fix OpenMP duplicate runtime issue
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunked_summarize

def video_to_summary(video_path: str, 
                     model_size: str = "base",
                     summarizer_model_name: str = "facebook/bart-large-cnn",
                     use_chunking: bool = False) -> str:
    
    #  1 extract audio from video
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)
    
    # 2 transcribe audio to text
    transcript = transcribe_audio(audio_path, model_size)
    
    # 3 summarizing tanscript
    if use_chunking:
        final_summary = chunked_summarize(text = transcript,
                                          summerize_func= lambda txt: summarize_text(
                                              text=txt, model_name=summarizer_model_name
                                          ),
                                          max_chunk_size=2000)
    else:
        final_summary = summarize_text(text=transcript, model_name=summarizer_model_name)
    
    # 4 clean up temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)
    
    return final_summary



    
if __name__ == "__main__":
    video_file = "sample_video.mp4"  # Replace with your video file path
    summary = video_to_summary(video_file, 
                               model_size="base",
                               summarizer_model_name="facebook/bart-large-cnn",
                               use_chunking=True)
    print("Final Summary:")
    print(summary)