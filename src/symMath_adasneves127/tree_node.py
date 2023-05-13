from eq_token import token
class tree_node:
    def __init__(self, type, value, precedence):
        self.value = value
        self.type = type
        self.prec = precedence
        self.parent = None
        self.left_child: None | tree_node  = None
        self.right_child: None | tree_node = None