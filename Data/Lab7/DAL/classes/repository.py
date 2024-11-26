"""Implements repository design principle"""
class Repository:
    """A class that implements the repository design principle"""
    def get_all(self):
        """The GET-ALL repository implementation"""
        raise NotImplementedError

    def get_by_id(self, entity_id):
        """The GET-BY repository implementation"""
        raise NotImplementedError

    def add(self, data):
        """The POST repository implementation"""
        raise NotImplementedError

    def update(self, entity_id, data):
        """The PATCH repository implementation"""
        raise NotImplementedError

    def delete(self, entity_id):
        """The DELETE repository implementation"""
        raise NotImplementedError
