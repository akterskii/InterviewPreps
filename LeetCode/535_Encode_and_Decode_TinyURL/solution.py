class Codec:
    def __init__(self):
        self.dict_ = {}
        self.current = [0, 0, 0, 0, 0, 0]
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() + "1234567890"
        self.init = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = []
        for i in self.current:
            key.append(self.letters[i])
        key = "".join(key)
        
        self.dict_[key] = longUrl
        
        self.current[0] += 1
        for i in range(len(self.current)):
            if self.current[i] == len(self.letters):
                self.current[i] = 0
                self.current[i + 1] += 1
        
        return self.init + key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[len(self.init):]
        return self.dict_[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))