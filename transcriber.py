import subprocess # to execute shell commands
import os # allow interaction with the operating system
import whisper  # openai speech-to-text library
# import imageio_ffmpeg  

def extract_audio(video_path: str, audio_path:str = "temp_audio.wav") -> str:
    """
    Extracts audio from a video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.
        audio_path (str): Path to save the extracted audio file.

    Returns:
        str: Path to the extracted audio file.
    """
    
    if os.path.exists(audio_path):
        os.remove(audio_path)
    
    # ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()  # get full path to ffmpeg binary
    
    command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",  # audio quality to highest
        "-map", "a",  # select audio stream/track from the video
        audio_path,
        "-y"  # overwrite output file if it exists
    ]
    
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return audio_path

def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    """
    Transcribes audio using OpenAI's Whisper model.

    Args:
        audio_path (str): Path to the input audio file.
        model_size (str): Size of the Whisper model to use (e.g., "tiny", "base", "small", "medium", "large").

    Returns:
        str: Transcribed text from the audio.
    """
    
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    transcribe =  result["text"]
    return transcribe

