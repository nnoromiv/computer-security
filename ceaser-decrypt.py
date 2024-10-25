def decrypt(key, message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letter in message:
        if letter in alpha:
            num = alpha.find(letter)
            new_num = (num - key) % len(alpha)
            result += alpha[new_num]
        else:
            result += letter
    return result

def main() -> None:
    try:   
        file_name = input("Enter file name: ")
        
        if(file_name == ""):
            print("No file name entered")
            return None
        
        if (len(file_name.split("_")) <= 1):
            print("Not a valid file name. File name must contain _ and a number")
            return None
    
        if (not file_name.endswith(".txt")):
            print("File name must end in .txt")
            return None
        
        if(file_name.split("_")[0] != "encrypted"):
            print("File name must start with encrypted")
            return None
        
        key = file_name.split("_")[1].split(".")[0]
        
        encrypted_file = open(file_name, "r")
    
        if(encrypted_file == None):
            print("File not found")
            return None
        
        encrypted = encrypted_file.read()
        decrypted_value = decrypt(int(key), encrypted)
        
        print(decrypted_value)        
        return decrypted_value
    except KeyboardInterrupt:
        print("Program terminated")
    except ValueError as e:
        print("Key must be an integer", e)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error: ", e) 
    finally:
        encrypted_file.close()
        print("End of program")
    
    return None

if __name__ == "__main__":
    main()