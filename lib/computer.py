
class Computer:

    all = []

    def __init__(self, brand, model, memory_GB = 8, storage_free=1000):
        self._brand = brand
        self._model = model
        self._memory_GB = memory_GB
        self._storage_free = storage_free
        Computer.all.append(self)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not hasattr(self, "brand"):
            self._brand = brand
        else:      
            raise Exception("brand cannot be changed")
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not hasattr(self, "model"):
            self._model = model
        else:      
            raise Exception("brand cannot be changed")

    @property
    def memory_GB(self):
        return self._memory_GB
    
    @memory_GB.setter
    def memory_GB(self, memory_GB):
        self._memory_GB = memory_GB

    @property
    def storage_free(self):
        return self._storage_free
    
    @storage_free.setter
    def storage_free(self, storage_free):
        if 0 <= storage_free <= 1000:
            self._storage_free = storage_free
        else:
            raise Exception("storage_free must be between 0 and 1000")


    def specs(self):
        return f"Memory: {self.memory_GB}, Free Storage: {self.storage_free}"


    def upgrade_memory(self, RAM):
        self.memory_GB += RAM['size']

    def is_disk_full(self, file_size):
        if file_size > self.storage_free:
            return True
        else: 
            return False
        
    def save_file(self, file):
        if not self.is_disk_full(file['size']):
            self.storage_free -= file['size']
            print(f"{file['name']} name has been saved!")
        else:
            raise Exception(f"There is not enough space on disk to save {file['name']}.")


    def delete_file(self, file):
        self.storage_free += file['size']
        print(f"{file['name']} has been deleted.")


    @classmethod
    def brands(cls):
        return [computer.brand for computer in Computer.all]
    
    @classmethod
    def models(cls):
        return [computer.model for computer in Computer.all]
    
    @classmethod
    def largest_memory(cls):
        memory_dict = {}
        for computer in Computer.all:
            memory_dict[computer] = computer.memory_GB
        return max(memory_dict, key = memory_dict.get)
        #map the list to a dictionary so then we can use Max function to find the biggest 

    def __str__(self):
        return f"{self.brand}: {self.memory_GB} RAM : {self.storage_free} GB"

if __name__ == "__main__":
    # you can write test code here
    # or in debug.py
    pass

# SANDBOX

pc = Computer("Dell", "D-10")
mac = Computer("Apple", "Macbook")

up_mem = {"model": "Dell", "size": 8}
file1 = {"name": "photo1", "size": 300}
file2 = {"name": "photo2", "size": 100}


print(mac.memory_GB)
mac.upgrade_memory(up_mem)
print(mac.memory_GB)

print(pc.storage_free)
pc.save_file(file1)
print(pc.storage_free)

print(Computer.largest_memory())
# pc.delete_file(file1)
# print(pc.storage_free)



# print(mac.specs())
# pc.brand = "IBM"