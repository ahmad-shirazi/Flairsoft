from src.application import uploader, data_gather, text_fetcher


def main():
    while True:
        data_gather.run()
        uploader.run()
        text_fetcher.run()
