from zipfile import ZipFile

FLAG = 0

# Method to attempt to extract the zip file with a given password
# zf_handleis a ZipFile object representing the encrypted zip file
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print(f"Password is {password.decode().strip()}")
        FLAG=1
    except Exception:
        pass
     

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            for pwd in f:
                # Attempt to extract the zip file using each password
                attempt_extract(zf, pwd.strip())

    if FLAG == 0:
        print("[+] Password not found in list")
            
            

if __name__ == "__main__":
    main()