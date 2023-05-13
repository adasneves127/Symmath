from tree_node import tree_node
from typing import List
from eq_token import token

def get_prec(type: str) -> int:
    prec = 0
    if type == "PLUS" or type == "MINUS":
        prec = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        prec = 2
    elif type == "EXPONENT":
        prec = 3
    return prec

def create_tree_list(token_list: List[token]):
    node_list: List[tree_node] = []
    global_prec = 0
    for token in token_list:
        if token.type == "LPAREN":
            global_prec += 4
        elif token.type == "RPAREN":
            global_prec -= 4
        else:
            new_node = tree_node(token.type, token.value, get_prec(token.type) + global_prec)
            node_list.append(new_node)
    return node_list

def parse(token_list: List[token]):
    root = None
    node_list = create_tree_list(token_list)
    create_tree(node_list)
    
    
def create_tree(node_list: List[tree_node]):
    dummy_node = tree_node("DUMMY", "", 0)
    node_list.insert(0, dummy_node)
    node_list.append(dummy_node)
    for index, node in enumerate(node_list):
        if node.type == "NUMBER":
            prev_op = node_list[index - 1]
            penn_op = node_list[index - 2]
            next_op = node_list[index + 1]
            
            if prev_op.type == penn_op.type == 'MINUS':
                pass