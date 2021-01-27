import streamlit as st
import pytube


def video_download(url, quality):
    try:
        if quality is '720p':
            st.write(pytube.YouTube(url).title)
            youtube_video = pytube.YouTube(url).streams.filter(adaptive=True).first()
        else:
            youtube_video = pytube.YouTube(url).streams.first()
        youtube_video.download(r"C:")
        st.write("Download Complete")
    except:
        st.write("This link is not valid")


def playlist_downloader(link, quality):
    try:
        youtube = pytube.Playlist(link)
        video_urls = youtube.video_urls
        for url in video_urls:
            video = pytube.YouTube(url)
            st.text(video.title)
            if quality is '720p':
                video_d = video.streams.filter(adaptive=True).first()
            else:
                video_d = video.streams.first()
            video_d.download(r"C:")
            st.write("Download Complete")
        st.write("All download is complete")

    except:
        st.write("This link is not valid")

def main():
    st.title("YouTube Downloader")
    link = st.text_area("Youtube Link")
    choice = st.selectbox("Youtube", ['YouTube Video', 'YouTube Play list'])
    quality = st.selectbox("Quality", ['720p', '360p'])
    if choice is 'YouTube Video':
        if st.button("Download Video"):
            video_download(link, quality)
    else:
        if st.button("Download Full Playlist"):
            playlist_downloader(link, quality)

if __name__ == '__main__':
    main()