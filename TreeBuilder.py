import CommonMark as cm
from glob import glob
import json


class Node:
    def __init__(self,
                 node_path):
        if node_path[-3:] != ".md":
            node_path += '/' + node_path.split('/')[-1] + '.md'
        self.node_id = node_path[:-3]
        with open(node_path, 'r') as node_file:
            self.node_markdown = node_file.read()
            self.note_parsed = cm.commonmark(self.node_markdown)

        self.children = []
        has_children = node_path[:-3].split('/')[-2] == node_path[:-3].split('/')[-1]
        if has_children:
            self.children += [Node(child_path)
                              for child_path in glob('/'.join(node_path.split('/')[:-1])+'/*')
                              if child_path != node_path]

    def __dictionary_representation(self):
        return {'name': self.node_id.split('/')[-1],
                'note': self.note_parsed,
                'children': [child.__dictionary_representation()
                             for child in self.children]
                }

    def json_representation(self):
        return json.dumps(self.__dictionary_representation())


class Tree:
    def __init__(self, tree_directory):
        root_path = tree_directory + '/' + tree_directory + '.md'
        self.root = Node(root_path)
