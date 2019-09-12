class TagCloud:
    def __init__(self):
        self.____tags = {}

    def add(self, tag):
        self.____tags[tag.lower()] = self.____tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.____tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.____tags[tag.lower()] = count

    def __len__(self):
        return len(self.____tags)

    def __iter__(self):
        return iter(self.____tags)


tag = TagCloud()
tag['python'] = 3
tag['JS'] = 2
print(len(tag))
print(tag['python'])
for t in tag:
    print(t)
