"""
We have a file that works as key-value storage,
each line is represented as key and value separated by = symbol,
example:
name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be
treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys
and values accessible as collection items and as attributes.
Example: storage['name'] # will be string 'kek' storage.song_name
# will be 'shadilay' storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted
to read it entirely into memory.
"""


class KeyValueStorage:
    """A wrapper class for a file that works as a key-value storage,
    allowing to access its keys and values as
    a collection items and as attributes

    :param path: path to the file (key-value storage)
    :type path: str
    """
    def __init__(self, path):
        """Constructor method
        """
        self.path = path
        self._load()

    def __getitem__(self, key):
        """Returns a value of a specific key
        either as a collection item or as an attribute

        :param key: specifies a key whose value should be returned
        :return: a value of a specific key
        :raises: AttributeError if object doesn't have such an attribute
        :rtype: str or int
        """
        return self.__dict__[key]

    def _load(self):
        """A method that reads every line from file
        and adds keys and their values
        to the object's attributes storage

        :rtype: None
        """
        with open(self.path) as file:
            for line in file:
                key, value = line.replace('\n', '').split('=')
                if key.isdigit():
                    raise ValueError('The key should be a string')
                elif key in self.__dict__:
                    continue
                else:
                    if value.isdigit():
                        self.__dict__[key] = int(value)
                    else:
                        self.__dict__[key] = value
