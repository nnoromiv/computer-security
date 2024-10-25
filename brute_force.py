def brute_force(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    
    for shift in range(len(alpha)):
        result = ""
        
        for letter in message:
            if letter in alpha:
                num = alpha.index(letter)
                new_num = (num - shift) % len(alpha)
                result += alpha[new_num]
            else:
                result += letter
                
        print(f"Shift {shift}: {result}")
        
def main() -> None:
    try:
        file_name = input("Enter file name: ")
        
        if(file_name == ""):
            print("No file name entered")
            return None

        encrypted_file = open(file_name, "r")
    
        if(encrypted_file == None):
            print("File not found")
            return None
        
        encrypted = encrypted_file.read()
        brute_force(encrypted)
        
    except KeyboardInterrupt:
        print("Program terminated")
    except ValueError:
        print("Key must be an integer")
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