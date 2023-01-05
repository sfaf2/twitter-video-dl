import src.twitter_video_dl.twitter_image_dl as tidl
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a image from a twitter url and save it in jpg."
    )

    parser.add_argument(
        "twitter_url",
        type=str,
        help="Twitter URL to download.  e.g. https://twitter.com/GOTGTheGame/status/1451361961782906889"
    )

    parser.add_argument(
        "file_name",
        type=str,
        help="Save twitter image to this filename. e.g. twitterimg.jpg"
    )

    args = parser.parse_args()

    file_name = args.file_name if args.file_name.endswith(".jpg") else args.file_name + ".jpg"

    tidl.download_image(args.twitter_url, file_name)