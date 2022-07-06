class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, objecct):
        print("Append called")
        super().append(object)


text = Text("Python")
print(text.duplicate())

list = TrackableList()
list.append("1")
