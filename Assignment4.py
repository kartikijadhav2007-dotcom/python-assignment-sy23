secret = input("Enter the secret message: ")
coded = input("Enter the coded message: ")

if secret in coded:
    print("Secret message found!")
else:
    print("Secret message not found!")