
CAMERA = 1       # 0001
MICROPHONE = 2   # 0010
STORAGE = 4      # 0100
LOCATION = 8     # 1000
 
approved_apps = [
    "coding app",
    "math app",
    "reading app",
    "science app"
]
 

student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to access: ").lower()
 
print("\n--- Identity Operator Check ---")
 

if type(student_name) is str:
    print("The student name is stored as text.")
 

if type(requested_app) is not int:
    print("The requested app is not stored as a number.")
 
 
print("\n--- Membership Operator Check ---")
 

if requested_app in approved_apps:
    print(requested_app, "is an approved student app.")
else:
    print(requested_app, "is not an approved student app.")
 

restricted_apps = [
    "gaming app",
    "shopping app",
    "social media app"
]
 
if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")
 
 
print("\n--- App Permission Settings ---")
 

student_permissions = CAMERA | MICROPHONE | STORAGE
 

print("Permission value:", student_permissions)
print("Permission bits:", bin(student_permissions))
 


if student_permissions & CAMERA:
    print("Camera permission: Enabled")
 
if student_permissions & MICROPHONE:
    print("Microphone permission: Enabled")
 
if student_permissions & STORAGE:
    print("Storage permission: Enabled")
 
if student_permissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")
 
 
print("\n--- Bit Shift Demonstration ---")
 

next_permission = CAMERA << 1
 
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))
 
previous_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))
 
 
print("\n--- Final Access Result ---")
 
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)
