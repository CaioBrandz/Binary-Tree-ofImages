from abc import ABC, abstractmethod
import cv2
import glob


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na arvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a arvore esta vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o no raiz da arvore"""
        pass


class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def __str__(self):
        return self._data.__str__()


class BinaryTree(TreeADT):

    def __init__(self, data=None):
        self._root = Node(data)

    def empty(self):
        if self._root._data is not None:
            return False
        else:
            return True

    def root(self):
        return self._root

    def insert(self, elem):
        node = Node(elem)
        if self.empty():
            self._root = node
        else:
            self.__insert_children(self._root, node)

    def __insert_children(self, root, node):

        r_height = root._data.shape[0] # retorna a altura da imagem presente na raiz
        n_height = node._data.shape[0] # retorna a altura da imagem presenta no nó a ser adicionado

        if n_height <= r_height: # modificado para a condicional da altura das data
            if not root._left:
                root._left = node
                root._left._parent = root
            else:
                self.__insert_children(root._left, node)
        else:
            if not root._right:
                root._right = node
                root._right._parent = root
            else:
                self.__insert_children(root._right, node)

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, lista):
        if not root:
            return
        self.__in_order(root._left, lista)
        lista.append(root._data)
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root._data)
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data)
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])


if __name__ == '__main__': # apertar a, s ou d para seguir uma das ordens

    t = BinaryTree()
    lenght =0 # controlar o tanto de imagens, logo o tanto de indices que um array vai ter (no caso, 16)

    for file in glob.glob("images/*.png"): #carregando todas as imagens e adicionando a arvore binaria
        a= cv2.imread(file)
        t.insert(a)
        lenght +=1

    l = t.traversal(True, True, True)

    x = 0 # indice de um dos 3 metodos, seguindo o transversal
    y = 0 # indice do array de um dos metodos

    while True:
        cv2.imshow('aperte a,s ou d continuadamente', l[x][y]) #mostrar a imagem da posicao x,y
        key = cv2.waitKeyEx()

        if key == 97:  # in order na letra a (apertando continuadamente a)
            if y < lenght -1 and x == 0:  # passar os indices in order
                y += 1
            elif x != 0:  # Se verdadeiro: ao apertar vai para o primeiro elemento da in order
                print('--começo da IN order--')
                x = 0
                y = 0
            print(y)

        elif key == 115:  # pre order na letra s (apertando continuadamente s)
            if y < lenght -1 and x == 1:  # passar os indices pre order
                y += 1
            elif x != 1:  # Se verdadeiro: ao apertar vai para o primeiro elemento da pre order
                print('--começo da PRE order--')
                x = 1
                y = 0
            print(y)

        elif key == 100:  # POST order na letra d (apertando continuadamente d)
            if y < lenght -1 and x == 2:  # passar os indices post order
                y += 1
            elif x != 2:  # Se verdadeiro: ao apertar vai para o primeiro elemento da post order
                print('--começo da POST order--')
                x = 2
                y = 0
            print(y)
        else:
            break
