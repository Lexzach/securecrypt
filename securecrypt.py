from cryptography.fernet import Fernet
import time
import os
import subprocess
import sys

publicKey = "5qSW6IMKejDeXqFRxHtWZqV6eaqPura7klInzwxjgtk="
print("Copy decrypt/encrypt results to clipboard? [y/n]")
answer = input()
if answer == "y":
    clipboardCopy = True
def clipboard(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
while 1==1:
    os.system('cls||clear')
    print("Erasing all variables for security...")
    time.sleep(0.2)
    key = ""
    print("Local key generator erased")
    time.sleep(0.01)
    keyFromFile = ""
    print("Local key from file erased")
    time.sleep(0.01)
    encryptedText = ""
    print("Encrypted text erased")
    time.sleep(0.01)
    encodedText = ""
    print("Encoded text erased")
    time.sleep(0.01)
    textToEncrypt = ""
    print("Raw text erased")
    time.sleep(0.01)
    answer = ""
    print("User selection erased")
    time.sleep(0.01)
    fileToEncrypt = ""
    filetoEncryptEndless = ""
    print("User selected file to encrypted erased")
    time.sleep(0.01)
    fileEncryptor = ""
    print("File encryptor erased")
    time.sleep(0.01)
    encryptedFileText = ""
    print("Encrypted file text erased")
    time.sleep(0.01)
    fileToDecrypt = ""
    filetoDecryptEndless = ""
    finalFile = ""
    print("User selected file to decrypted erased")
    time.sleep(0.01)
    fileDecryptor = ""
    print("Display key erased")
    time.sleep(0.01)
    displayKey = ""
    print("File decryptor erased")
    time.sleep(0.01)
    decryptedFileText = ""
    print("Decrypted file text erased")
    time.sleep(0.01)
    decryptedText = ""
    print("Raw decrypted text erased")
    time.sleep(0.01)
    textToDecrypt = ""
    print("User input text to decrypt erased")
    time.sleep(0.01)
    print("DONE!")
    time.sleep(0.2)
    os.system('cls||clear')
    print(" ___                       ___               _   ")
    print("/ __| ___ __ _  _ _ _ ___ / __|_ _ _  _ _ __| |_ ")
    print("\__ \/ -_) _| || | '_/ -_) (__| '_| || | '_ \  _|")
    print("|___/\___\__|\_,_|_| \___|\___|_|  \_, | .__/\__|")
    print("                                   |__/|_|       ")
    print("Made by Lexzach - v1.3")
    print("")
    print("Generate Key [g] - Encrypt [e] - Decrypt [d]")
    answer = input()
    if answer == "g":
        key = Fernet.generate_key()
        displayKey = str(key)
        os.system('cls||clear')
        print("Display key? (The key is encrypted in the key.aes file, it will be hard to extract the key if not viewed now.) [y/n]")
        answer = input()
        displayKey = str(displayKey[2:])
        displayKey = str(displayKey.replace("'", ''))
        if answer == "y":
            print("")
            print("SECRET KEY:")
            print("")
            print(displayKey)
            print("")
            print("")
            print("press enter to continue...")
            input()
        os.system('cls||clear')
        coder = Fernet(publicKey)
        displayKey = displayKey.encode()
        key = coder.encrypt(displayKey)
        print("Write key to file? (This file will be created the same directory as this program) [y/n]")
        answer = input()
        if answer == "y":
            if os.path.isfile("key.aes") == True:
                os.system('cls||clear')
                print("A KEY HAS ALREADY BEEN DETECTED! IF YOU CONTINUE, IT WILL BE OVERWRITTEN!")
                time.sleep(1)
                print("")
                print("Type 'continue' to continue (Case sensitive.)")
                answer = input()
                if answer == "continue":
                    file = open('key.aes', 'wb')
                    file.write(key)
                    file.close()
                    print("")
                    print("Old key overwritten with new key")
                    print("")
                    print("press enter to exit to main and erase all local variables...")
                    input()
                else:
                    print("Confirmation failed. Key has NOT been overwritten.")
                    print("")
                    print("press enter to exit to main and erase all local variables...")
                    input()
            else:
                file = open('key.aes', 'wb')
                file.write(key)
                file.close()
                print("File written")
                print("")
                print("press enter to exit to main and erase all local variables...")
                input()
    if answer == "e":
        os.system('cls||clear')
        try:
            file = open('key.aes', 'r')
            keyFromFile = file.read()
            keyFromFile = str(keyFromFile)
            file.close()
            coder = Fernet(publicKey)
            keyFromFile = keyFromFile.encode()
            keyFromFile = str(coder.decrypt(keyFromFile))
            keyFromFile = str(keyFromFile[2:])
            keyFromFile = str(keyFromFile.replace("'", ''))
        except:
            print("Fatal error: No key detected.")
            print("Would you like to generate a new key? [y/n]")
            answer = input()
            if answer == "y":
                key = Fernet.generate_key()
                displayKey = str(key)
                os.system('cls||clear')
                print("Display key? (The key is encrypted in the key.aes file, it will be hard to extract the key if not viewed now.) [y/n]")
                answer = input()
                displayKey = str(displayKey[2:])
                displayKey = str(displayKey.replace("'", ''))
                if answer == "y":
                    print("")
                    print("SECRET KEY:")
                    print("")
                    print(displayKey)
                    print("")
                    print("")
                    print("press enter to continue...")
                    displayKey = ""
                    input()
                os.system('cls||clear')
                coder = Fernet(publicKey)
                displayKey = displayKey.encode()
                key = coder.encrypt(displayKey)
                print("Write key to file? (This file will be created the same directory as this program) [Y/N]")
                answer = input()
                if answer == "y":
                    if os.path.isfile("key.aes") == True:
                        os.system('cls||clear')
                        print("A KEY HAS ALREADY BEEN DETECTED! IF YOU CONTINUE, IT WILL BE OVERWRITTEN!")
                        time.sleep(1)
                        print("")
                        print("Type 'continue' to continue (Case sensitive.)")
                        answer = input()
                        if answer == "continue":
                            file = open('key.aes', 'wb')
                            file.write(key)
                            file.close()
                            file = open('key.aes','rb')
                            keyFromFile = file.read()
                            file.close()
                            print("")
                            print("Old key overwritten with new key")
                            print("")
                            print("press enter to exit to main and erase all local variables...")
                            input()
                        else:
                            print("Confirmation failed. Key has NOT been overwritten.")
                            print("")
                            print("press enter to exit to main and erase all local variables...")
                            input()
                    else:
                        file = open('key.aes', 'wb')
                        file.write(key)
                        file.close()
                        file = open('key.aes','rb')
                        keyFromFile = file.read()
                        file.close()
                    file = open('key.aes', 'r')
                    keyFromFile = file.read()
                    keyFromFile = str(keyFromFile)
                    file.close()
                    coder = Fernet(publicKey)
                    keyFromFile = keyFromFile.encode()
                    keyFromFile = str(coder.decrypt(keyFromFile))
                    keyFromFile = str(keyFromFile[2:])
                    keyFromFile = str(keyFromFile.replace("'", ''))
            else:
                sys.exit(0)
        os.system('cls||clear')
        coder = Fernet(keyFromFile)
        print("File or Text? [f/t]")
        answer = input()
        if answer == "t":
            os.system('cls||clear')
            print("Enter text to encrypt:")
            textToEncrypt = input()
            encodedText = textToEncrypt.encode()
            textToEncrypt = ""
            encryptedText = str(coder.encrypt(encodedText))
            encodedText = ""
            encryptedText = encryptedText[2:]
            encryptedText = str(encryptedText.replace("'", ''))
            if clipboardCopy == True:
                clipboard(encryptedText)
            print("")
            print("")
            print(str(encryptedText))
            print("")
            print("")
            print("press enter to exit to main and erase all local variables...")
            input()
        if answer == "f":
            os.system('cls||clear')
            print("Enter name of file to encrypt (INCLUDING ENDING) [File must be in same directory as this program]")
            filetoEncrypt = input()
            print("")
            print("Encrypting file...")
            try:
                with open(filetoEncrypt, 'rb') as f:
                    fileEncryptor = f.read()
                encryptedFileText = coder.encrypt(fileEncryptor)
                with open("encrypted." + filetoEncrypt, "wb") as f:
                    f.write(encryptedFileText)
            except:
                print("Fatal error: File provided does not exist.")
                print("press enter to close...")
                input()
                sys.exit(0)
            print("File encryption successful!")
            print("File created named 'encrypted." + filetoEncrypt + "' in the same directory as the program.")
            print("")
            print("press enter to exit to main and erase all local variables...")
            input()
    if answer == "d":
        os.system('cls||clear')
        try:
            file = open('key.aes', 'r')
            keyFromFile = file.read()
            keyFromFile = str(keyFromFile)
            file.close()
            coder = Fernet(publicKey)
            keyFromFile = keyFromFile.encode()
            keyFromFile = str(coder.decrypt(keyFromFile))
        except:
            print("Fatal error: No key detected. Relaunch program and generate a new key!")
            print("press enter to close...")
            input()
            sys.exit(0)
        keyFromFile = str(keyFromFile[2:])
        keyFromFile = str(keyFromFile.replace("'", ''))
        decoder = Fernet(keyFromFile)
        print("File or Text? [f/t]")
        answer = input()
        if answer == "t":
            os.system('cls||clear')
            print("Enter text to decrypt:")
            textToDecrypt = input()
            textToDecrypt = textToDecrypt.encode()
            try:
                decryptedText = decoder.decrypt(textToDecrypt)
            except:
                print("Fatal error: Invalid key!")
                print("press enter to close...")
                input()
                sys.exit(0)
            decryptedText = decryptedText.decode()
            textToDecrypt = ""
            if clipboardCopy == True:
                clipboard(decryptedText)
            print("")
            print("")
            print(str(decryptedText))
            print("")
            print("")
            print("press enter to exit to main and erase all local variables...")
            input()
        if answer == "f":
            os.system('cls||clear')
            print("Enter name of file to decrypt (INCLUDING ENDING) [File must be in same directory as this program]")
            fileToDecrypt = input()
            try:
                with open(fileToDecrypt, 'rb') as f:
                    fileDecryptor = f.read()
                try:
                    decryptedFileText = decoder.decrypt(fileDecryptor)
                    print("Decrypting file...")
                except:
                    print("File decryption failed!")
                    print("Fatal error: Invalid key!")
                    print("press enter to close...")
                    input()
                    sys.exit(0)
                fileToDecrypt = fileToDecrypt[10:]
                with open("decrypted." + fileToDecrypt, "wb") as f:
                    f.write(decryptedFileText)
            except:
                print("Fatal error: File provided does not exist.")
                print("press enter to close...")
                input()
                sys.exit(0)
            print("File decryption successful!")
            print("File created named 'decrypted." + fileToDecrypt + "' in the same directory as the program.")
            print("")
            print("press enter to exit to main and erase all local variables...")
            input()