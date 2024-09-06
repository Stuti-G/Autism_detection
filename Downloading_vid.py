import os
import yt_dlp

def read_urls_from_txt(file_path): 
    """Reads YouTube video URLs from a .txt file."""
    try:
        with open(file_path, 'r') as file: 
            urls = [line.strip() for line in file if line.strip()] 
        return urls
    except Exception as e:
        print(f"Error reading URLs from file: {file_path}")
        print(str(e))
        return []

def download_youtube_video(url, output_folder): 
    """Downloads a YouTube video to the specified output folder."""
    ydl_opts = { 
        'format': 'best', 
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'), 
        'quiet': True,  
        'no_warnings': True,   
        'ignoreerrors': True,  
        'geo_bypass': True,  
        'noplaylist': True,  
        'cookies': 'path/to/cookies.txt',  
    } 
    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
            info_dict = ydl.extract_info(url, download=True) 
            return ydl.prepare_filename(info_dict) 
    except Exception as e: 
        print(f"An error occurred while downloading the video: {url}") 
        print(str(e))
        return None

def main():
    """Main function to read URLs from a file and download YouTube videos."""
    file_path = '/content/drive/MyDrive/Autisim_Detection/test_vids.txt'
    output_folder = '/content/drive/MyDrive/Autisim_Detection/test_videos' 
    
    urls = read_urls_from_txt(file_path)
    
    if not urls:
        print("No URLs found to download.")
        return

    for url in urls:
        print(f"Downloading video from: {url}")
        video_path = download_youtube_video(url, output_folder)
        
        if video_path:
            print(f"Video downloaded successfully: {video_path}")
        else:
            print(f"Failed to download video: {url}")

if __name__ == '__main__':
    main()
