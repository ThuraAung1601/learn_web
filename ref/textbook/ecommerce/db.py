from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
import persistent
from BTrees.OOBTree import OOBTree

# Initialize ZODB
storage = FileStorage('myshoppingapp.fs')
db = DB(storage)
connection = db.open()
root = connection.root

# Initialize catalog if it doesn't exist
if not hasattr(root, 'catalog'):
    root.catalog = OOBTree()
    transaction.commit()
