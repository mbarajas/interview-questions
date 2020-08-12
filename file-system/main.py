class SystemItem:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

class Directory(SystemItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    def mkdir(self, name):
        self.children.append(name)
        return Directory(name, self.name)

    def touch(self, name):
        self.children.append(name)
        return File(name, self.name)

class File(SystemItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.content = ''



root = Directory('/', None)
home = root.mkdir('/home')
test_file = home.touch('/home/test.txt')
test_file.content = 'This is the first test file'
test_file2 = home.touch('/home/test2.html')
documents = home.mkdir('/home/documents')
print(root.name)
print(home.name)
print(home.parent)
print(home.children)
print(test_file.name)
print(test_file.parent)
print(test_file.content)
