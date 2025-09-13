import streamlit as st
import os
from main import video_to_summary

def main():
    st.title("Video to Summary Application")
    
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])
    
    use_chunking = st.checkbox("Use Chunking for Summarization", value=False)
    
    if video_file is not None:
        with open("uploaded_video.mp4", "wb") as f:
            f.write(video_file.read())
        
        if st.button("Generate Summary"):
            with st.spinner("Processing..."):
                summary = video_to_summary(video_path="uploaded_video.mp4", 
                                           use_chunking=use_chunking)
            st.success("Summary Generated!")
            st.text_area("Final Summary:", value=summary, height=300)
        
        if os.path.exists("temp_video.mp4"):
            os.remove("temp_video.mp4")

# 👇 This makes Streamlit actually run the UI
if __name__ == "__main__":
    main()