import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def main():
    st.title("Video Upload and Camera Access")

    # Option to upload video file
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Display uploaded video
        st.video(uploaded_file)

    # Option to access camera
    use_camera = st.checkbox("Use camera")

    if use_camera:
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()