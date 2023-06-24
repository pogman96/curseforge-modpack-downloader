import os

from dotenv import load_dotenv

from cfdownloader import ModpackDownloader


def main():
    load_dotenv()
    API_KEY = os.getenv("CURSEFORGE_API")

    downloader = ModpackDownloader(API_KEY)
    downloader.download_modpack()


if __name__ == "__main__":
    main()