MIRAJE-V — это Python библиотека, предназначенная для загрузки видео с YouTube. Она проста в использовании и предлагает мощный функционал для работы с видеофайлами.

## Установка

Вы можете установить MIRAJE-V с помощью pip:

bash
pip install mira-je-v

## Использование

Для того чтобы начать использовать MIRAJE-V, выполните следующие шаги:

1. Импортируйте библиотеку:
    python
    from mirajev import MirajeV
    
2. Создайте объект загрузчика

    
3. Загрузите видео по его URL

    
## Возможности

- Загрузка видео в различных качествах.
- Поддержка загрузки аудиодорожек.
- Удобный интерфейс для работы с загруженными видео.

## Примеры

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


## Вклад

Если вы хотите внести свой вклад в развитие MIRAJE-V, пожалуйста, создайте форк репозитория и отправьте пул-реквест с вашими изменениями.

## Лицензия

Этот проект лицензируется под MIT License. Для получения дополнительных сведений смотрите файл [LICENSE](LICENSE).

## 📱 Контакты  
Разработчик: thetemirbolatov
- **VK**: [thetemirbolatov](https://vk.com/thetemirbolatov)  
- **Instagram**: [@thetemirbolatov](https://instagram.com/thetemirbolatov)  
- **Telegram**: [@thetemirbolatov](https://t.me/thetemirbolatov)  
- **GitHub**: [ftoop17](https://github.com/ftoop17)  

⭐ **Если вам нравится проект, поставьте звезду на GitHub!** ⭐  

