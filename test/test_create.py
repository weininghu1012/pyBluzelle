from pyBluzelle.main import Bluzelle
import time
b = Bluzelle()
b.connect("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
b.create("gg","1234")
#time.sleep(1)
b.read("gg")
b.delete("gg")
#time.sleep(1)
b.read("gg")