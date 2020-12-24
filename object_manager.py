import id_generator


class Object_manager():
    def __init__(self):
        self._objects = {}  # id:obj
        self._id_generator = id_generator.Usual_id_generator()

    def _get_obj_id(self, obj):
        for id, val in self._objects.items():
            if obj is val:
                return id
        return None

    def add_object(self, obj):
        # get existent id
        if obj in self._objects.values():
            return self._get_obj_id(obj)

        new_id = self._id_generator.get_id()
        self._objects[new_id] = obj
        return new_id

    def get_obj_id(self, obj):
        return self._get_obj_id(obj)

    def get_obj_by_id(self, id):
        if id in self._objects.keys():
            return self._objects[id]
        else:
            return None