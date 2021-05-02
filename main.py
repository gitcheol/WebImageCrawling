import argparse
from webImageCrawler import WebImageCrawler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Image Crawler")

    parser.add_argument("--platform", default="daum",type=str, dest="platform")
    parser.add_argument("--counter", default=3 ,type=int, dest="counter")

    args = parser.parse_args()

    crawler = WebImageCrawler(platform=args.platform ,counter=args.counter)
    crawler.crawl_imgs()
