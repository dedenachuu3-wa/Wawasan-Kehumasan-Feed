import xml.etree.ElementTree as ET
from datetime import datetime

# Nama file input (artikel) dan output (feed)
ARTIKEL_FILE = "artikel-pr.txt"  # pastikan ekstensinya benar
OUTPUT_FILE = "feed.xml"

def read_articles(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    articles = []
    for line in lines:
        if line.strip():
            title, link = line.split("|", 1)
            articles.append({"title": title.strip(), "link": link.strip()})
    return articles

def generate_feed(articles):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Wawasan Kehumasan Feed"
    ET.SubElement(channel, "link").text = "https://dedenachuu3-wa.github.io/"
    ET.SubElement(channel, "description").text = "Kumpulan artikel Wawasan Kehumasan"
    ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

    for art in articles:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = art["title"]
        ET.SubElement(item, "link").text = art["link"]
        ET.SubElement(item, "pubDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

    tree = ET.ElementTree(rss)
    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    arts = read_articles(ARTIKEL_FILE)
    generate_feed(arts)
    print("feed.xml generated successfully!")
