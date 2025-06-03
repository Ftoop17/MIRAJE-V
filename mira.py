from mirajev import MirajeV

def main():
    print("MIRAJE | V YouTube Downloader")
    url = input("Enter YouTube URL: ")
    
    try:
        downloader = MirajeV(url)
        
        print("\nAvailable resolutions:")
        for stream in downloader.get_video_streams():
            print(f"- {stream['quality']} ({stream['mimeType'].split(';')[0]})")
        
        choice = input("\nEnter resolution (or 'best'): ") or "best"
        
        filename = input("Output filename (default: video.mp4): ") or "video.mp4"
        
        print("\nDownloading...")
        downloader.download(filename=filename, resolution=choice)
        
        print(f"\nDone! Saved as {filename}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()