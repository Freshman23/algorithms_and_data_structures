""" Задание №2.
    Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter, defaultdict


class MyNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        if self.data[0] is None:
            disp_str = f'Node({self.data[1]}, ' \
                       f'left:{(f"Leaf{self.left.data}", f"Node({self.left.data[1]})")[self.left.data[0] is None]}, ' \
                       f'right:{(f"Leaf{self.right.data}", f"Node({self.right.data[1]})")[self.right.data[0] is None]})'
        else:
            disp_str = f'Leaf{self.data}'
        return disp_str


def build_huffman_tree(code_str: str) -> MyNode:
    node_lst = [MyNode(item) for item in Counter(code_str).most_common()]

    while len(node_lst) > 1:
        node_1 = node_lst.pop()
        node_2 = node_lst.pop()
        com_node = MyNode((None, node_1.data[1] + node_2.data[1]), node_1, node_2)

        index = -1
        if len(node_lst) >= 1:
            for ind, node in enumerate(node_lst):
                if com_node.data[1] > node.data[1]:
                    index = ind
                    break

        if index == -1:
            node_lst.append(com_node)
        else:
            node_lst.insert(index, com_node)

    return node_lst[0]


def build_huffman_table(huf_dict: defaultdict, huf_btree: MyNode, code: str = ''):
    if huf_btree.data[0] is not None:
        huf_dict[huf_btree.data[0]] = code
    else:
        build_huffman_table(huf_dict, huf_btree.left, code=f'{code}0')
        build_huffman_table(huf_dict, huf_btree.right, code=f'{code}1')


def huffman_encoding(str_to_encode: str, with_spaces: bool = False):
    huffman_table = defaultdict(str)
    build_huffman_table(huffman_table, build_huffman_tree(str_to_encode))
    huffman_table = dict(huffman_table)
    print(f'Encoding dictionary:\n{huffman_table}')

    encoded_str = ''
    if with_spaces:
        for char in str_to_encode:
            encoded_str += f'{huffman_table[char]} '
        encoded_str = encoded_str[:-1]
    else:
        for char in str_to_encode:
            encoded_str += huffman_table[char]
    print(f'Encoded string:\n{encoded_str}')


while True:
    inp_str = input('*' * 50 + '\n' + 'Input text to encode by Huffman algorithm or press [Enter] to exit:\n')
    if inp_str != '':
        huffman_encoding(inp_str, True)
    else:
        print('The encoding is over.')
        break
