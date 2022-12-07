from collections import deque


class Base:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
    
class File(Base):
    def __init__(self, name, parent, size):
        Base.__init__(self,name, parent)
        self.size = size
    
    
    
class Dir(Base):
    def __init__(self, name, parent):
        Base.__init__(self,name, parent)
        self.sub_directories = {}
        self.files = {}
    
    def add_dir(self, name):
        if name not  in self.sub_directories: 
            self.sub_directories[name] = Dir(name,self)
        
    
    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = File(name,self,size)
    
    


def parse(in_file):
    cur_dir = None
    root = Dir("/",None)
    with open(in_file) as file:
        for line in file:
            line = line.rstrip()
            contents = line.split()
            if contents[0] == "$":
                command = contents[1]
                if command == "cd":
                    dir_name = contents[2]
                    if dir_name == "/":
                        cur_dir = root
                    elif dir_name == "..":
                        cur_dir = cur_dir.parent
                    else:
                        cur_dir = cur_dir.sub_directories[dir_name]
                
                elif command == "ls":
                    pass
            else:
                # must be result of ls
                if contents[0] == "dir":
                    cur_dir.add_dir(name= contents[1])
                else:
                    cur_dir.add_file(name= contents[1], size= int(contents[0]))
    return root

def populate_dir_size(dir):
    dir.size = sum([f.size for f in dir.files.values()])
    if dir.sub_directories:
        for sub in dir.sub_directories.values():
            dir.size += populate_dir_size(sub)
    return dir.size


def part_1(root, limit):
    ans = 0
    # dfs
    stack = [root]
    while stack:
        dir = stack.pop()
        if dir.size <= limit:
            ans += dir.size
        for sub in dir.sub_directories.values():
            stack.append(sub)
    return ans

def part_2(root, limit = 70000000, needed = 30000000):
    ans = float('inf')
    free_space = limit - root.size
    deficit = needed - free_space
    if deficit <= 0:
        return 0
    # bfs
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            dir = queue.popleft()
            ans = min(ans, dir.size)
            for sub in dir.sub_directories.values():
                if sub.size >= deficit:
                    queue.append(sub)
    return ans

    

if __name__ == "__main__":
    root = parse("input.txt")
    populate_dir_size(root)
    print(f"part_1: {part_1(root, 100000)}") 
    print(f"part_2: {part_2(root)}")