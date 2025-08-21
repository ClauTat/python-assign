#file = open ('new file.pdf' , 'w')
#file.write("Heehee!! done it again yeyeeee")

#reading a file
#file = open("new file.pdf" , 'r')
#data =file.read()
#print(data)
def read_and_modify_file():
    filename = input("wello wello: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
        
        # Step 3: Modify the content (example: uppercase all text)
        modified_content = content.upper()

        # Step 4: Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
read_and_modify_file()
