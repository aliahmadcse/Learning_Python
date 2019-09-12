class Text(str):
    def duplicate(self):
        return self+self


# text=Text('Python')
# print(text.lower())
# print(text)
# print(text.duplicate())

class TrackAbleList(list):
    def append(self, object):
        print("Appending...")
        super().append(object)


list = TrackAbleList()
list.append(1)
list.append(2)
print(list)
