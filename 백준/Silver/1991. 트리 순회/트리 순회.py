N = int(input())

def preorder(root):
    global trees,preanswer
    left, right = trees[root]
    preanswer.append(root)
    if left!='.':
        preorder(left)
    if right!='.':
        preorder(right)

def inorder(root):
    global trees, inanswer
    left, right = trees[root]
    if left!='.':
        inorder(left)
    inanswer.append(root)
    if right!='.':
        inorder(right)
        
def postorder(root):
    global trees, postanswer
    left, right = trees[root]
    if left!='.':
        postorder(left)
    if right!='.':
        postorder(right)
    postanswer.append(root)

trees=dict()
for _ in range(N):
    root, left, right = input().split()
    trees[root]=[left,right]
preanswer=[]
inanswer=[]
postanswer=[]
preorder("A")
inorder("A")
postorder("A")
print(''.join(preanswer))
print(''.join(inanswer))
print(''.join(postanswer))
