from pyBluzelle.main import Bluzelle
import time
b = Bluzelle()
b.connect("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
res = b.create("gg","1234")
res = b.read("gg")
print(res)
res = b.delete("gg")
res = b.read("gg")
print(res)
