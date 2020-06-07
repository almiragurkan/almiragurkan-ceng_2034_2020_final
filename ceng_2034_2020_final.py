#Almira Gürkan

# /usr/bin/python3
import os, requests, uuid, hashlib

url = [
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

files = []

files_md5 = []

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def download_file(url, file_name=None):
  global files
  # download the file contents in binary format
  r = requests.get(url, allow_redirects=True)
  file = file_name if file_name else str(uuid.uuid4())
  # open method to open a file on your system and write the contents
  open(file, 'wb').write(r.content)
  files.append(file)
  
# Create a child process 
def child_process(): 
  pid = os.fork() 
  #If fork() returns a negative value, the creation of a child process was unsuccessful.
  #fork() returns a zero to the newly created child process.
  #fork() returns a positive value, the process ID of the child process, to the parent.
  if (pid == 0):
    print("Child Process ID:", os.getpid()) 
    for i in range(len(url)):
      download_file(url[i], "downloaded_file_{}".format(i+1))
    for i in files:
      md5_checksum = md5(i)
      if md5_checksum in files_md5:
        print("{} is a duplicated file".format(i))
        continue
      files_md5.append(md5_checksum)

  elif (pid > 0):
    # Wait for the completion of child process using os.wait() method     
    status = os.wait() 
    print("Parent Process ID:", os.getpid())
    # using os.wait() method Parent process 
    #will wait till the completion of child process 
    #and then only it will begin its execution 
  else : 
    print("Error:")

child_process()