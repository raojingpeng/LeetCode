# Note: This is a companion problem to the System Design problem: Design TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#


class Codec:
    # 当时想到 md5 base64 但是感觉都没办法做 最后参考题解自己实现了一下
    def __init__(self):
        self._chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-"
        self._mapping = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ''.join(random.sample(self._chars, 6))
        while self._mapping.get(key):
            key = ''.join(random.sample(self._chars, 6))
        self._mapping[key] = longUrl
        return 'http://tinyurl.com/%s' % key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self._mapping.get(shortUrl[19:])
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
