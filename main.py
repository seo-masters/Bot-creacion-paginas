from app.layouts import GeoLayout

website_info = {
    "websiteName": "Example Website",
    "webpageTitle": "Home Page",
    "service": "Web Development",
    "location": {
        "city": "New York",
        "state": "NY"
    },
    "mapUrl": "https://www.example.com/map"
}


def main():
    r = GeoLayout(website_info)
    r.buildLayout()

if __name__ == "__main__":
    main()
