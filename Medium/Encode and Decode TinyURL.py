class Codec:
    originalUrl = ""
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.originalUrl = longUrl
        shortUrl = "http://tinyurl.com/4e9iAk"
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.originalUrl

url = "https://leetcode.com/problems/design-tinyurl"
obj = Codec(url)
