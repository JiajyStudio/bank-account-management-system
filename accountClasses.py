"""Represents a single account's data"""
class AccountData:
    def __init__(self, accNum, accName, balance):
        self.accNum = accNum
        self.accName = accName
        self.balance = float(balance)
    
    def __repr__(self):
        return f"{self.accNum}: {self.accName}: {self.balance}"

"""A node in the BST"""
class AccountEntry:
    def __init__(self, account_data):
        self.account = account_data
        self.left = None
        self.right = None
    
    def getAccount(self):
        return self.account
    
    def setAccount(self, newAccount):
        self.account = newAccount
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, newLeft):
        self.left = newLeft
    
    def getRight(self):
        return self.right
    
    def setRight(self, newRight):
        self.right = newRight

"""Manages the binary search tree of accounts"""
class Account:
    def __init__(self):
        self.root = None

    def add_NewAcc(self, accNum, accName, balance=None):
        account_data = AccountData(accNum, accName, float(balance))
        newEntry = AccountEntry(account_data)
        self.root, inserted = self._insert(self.root, newEntry)
        if inserted:
            print(f"Account {accNum} added: {accName}")

    def _insert(self, node, entry):
        if node is None:
            return entry, True  # Just return the new AccountEntry

        if entry.account.accNum < node.account.accNum:
            node.left, inserted = self._insert(node.left, entry)
        elif entry.account.accNum > node.account.accNum:
            node.right, inserted = self._insert(node.right, entry)
        else:
            print("Account already exists. Please Try Again!")
            return node, False
        return node, inserted
    
    def searchAcc(self, accNum):
        return self._search(accNum, self.root, 0)
    
    def _search(self, accNum, curNode, depth):
        if curNode == None:
            #print(f"\n⚠️{accNum} is not found in the tree!")
            return None, depth
        elif accNum == curNode.account.accNum:
            #print(f"\n✅ Found: {accNum} found at depth {depth}.")
            return curNode, depth
        elif accNum > curNode.account.accNum:
            #print(f"🔍 Searching right of {curNode.account.accNum} (depth {depth})...")
            return self._search(accNum, curNode.right, depth + 1)
        elif accNum < curNode.account.accNum:
            #print(f"🔍 Searching left of {curNode.account.accNum} (depth {depth})...")
            return self._search(accNum, curNode.left, depth + 1)
    
    def deposit(self, accNum, depositAmount):
        node, _ = self._search(accNum, self.root, 0)
        if node:
            node.account.balance += float(depositAmount)
            print(f"Deposited {depositAmount} to {accNum}.\nNew balance: {node.account.balance}")
        else:
            print("Account not found for deposit.")
    
    def withdrawal(self, accNum, withdrawAmount):
        node, _ = self._search(accNum, self.root, 0)
        if node:
            if node.account.balance < float(withdrawAmount):
                print("Insufficient balance.")
                return
            else:
                node.account.balance -= float(withdrawAmount)
                print(f"Withdrawn {withdrawAmount} from {accNum}.\nNew balance: {node.account.balance}")
        else:
            print("Account not found for withdrawal.")
    
    def check_Balance(self, accNum):
        node, _ = self._search(accNum, self.root, 0)
        if node:
            print(f"\nAccount Number: {node.account.accNum}\nAccount Name: {node.account.accName}\nBalance: {node.account.balance}")
        else:
            print("Account not found.")
    
    def delete_Acc(self, accNum):
        self.root, deleted = self._delete(self.root, accNum)
        if deleted:
            print(f"Account {accNum} deleted.")
        else:
            print("Account does not exist. Please Try Again!")
    
    def _delete(self, node, accNum):
        if node is None:
            return node, False
        if accNum < node.account.accNum:
            node.left, deleted = self._delete(node.left, accNum)
        elif accNum > node.account.accNum:
            node.right, deleted = self._delete(node.right, accNum)
        else:
            # Node found
            #Case1: No children
            if node.left == None and node.right == None:
                return None, True
            
            #Case2: 1 child
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            
            # Node with two children
            successor = self._successor(node.right)
            node.account = successor.account
            node.right, _ = self._delete(node.right, successor.account.accNum)
            return node, True
        return node, deleted
    
    def _successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inOrder(self, curNode):
        #Performs an in-order traversal -> Left, Root, Right
        result = []
        if curNode:
            result.extend(self.inOrder(curNode.left))
            result.append(str(curNode.account))
            result.extend(self.inOrder(curNode.right))
        return result
    
    def preOrder(self, curNode):
        #Performs a pre-order traversal -> Root, Left, Right
        result = []
        if curNode:
            result.append(str(curNode.account))
            result.extend(self.preOrder(curNode.left))
            result.extend(self.preOrder(curNode.right))
        return result
    
    def postOrder(self, curNode):
        #Performs a post-order traversal -> Left, Right, Root
        result = []
        if curNode:
            result.extend(self.postOrder(curNode.left))
            result.extend(self.postOrder(curNode.right))
            result.append(str(curNode.account))
        return result