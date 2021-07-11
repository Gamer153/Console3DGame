from object import Object


class World:
    objects = list() # type: list [Object]

    def __init__(self) -> None:
        pass

    def add_object(self, object):
        self.objects.append(object)

    def add_objects(self, *objects):
        for obj in objects:
            self.add_object(obj)

    def remove_object(self, index):
        try:
            del self.objects[index]
        except:
            pass
    
    def find_object_by_id(self, id, all_objects = False) -> 'Object | list [Object]':
        objects = list()
        for i in range(self.objects):
            id_ = self.objects[i].id
            if id_ == id:
                if all_objects:
                    objects.append(self.objects[i])
                else:
                    return self.objects[i]
        return objects
