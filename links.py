class Objlist:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        new_obj = Objlist(obj)
        if self.head is None:
            self.head = self.tail = new_obj
        else:
            self.tail.set_next(obj)
            new_obj.set_prev(self.tail)
            self.tail = new_obj

    def remove_obj(self):
        if self.head is None:
            return

        current = self.head
        while current:
            if current == self.tail:
                self.tail = current.__prev
                if self.tail:
                    self.tail.__next = None
            return
        current = current.__next

    def get_data(self):
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list
