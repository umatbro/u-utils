import json
import collections


# TODO processing trees

def tree():
    """
    Tree implementation from 'Mastering Python' book.

    Usage::

      sports = tree()
      sports['olympic']['athletics']['water sports'] = 'Swimming 400m'
      sports['other']['extreme'] = 'Wrestling'

    :return: tree object
    """
    return collections.defaultdict(tree)


def tree_dumps(tree, indent=2, sort_keys=True):
    return json.dumps(tree, sort_keys=sort_keys, indent=indent)
