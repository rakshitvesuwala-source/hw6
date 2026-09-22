# ====================================
# SWIMMING POOL ENTRY CHECKER
# ====================================

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

# Collect inputs (1 number and 2 yes/no questions)
age = int(input("1. Enter your age: "))
swimmer = input("2. Are you a strong swimmer? (yes/no): ").strip().lower()
adult_present = input("3. Is an adult supervising you? (yes/no): ").strip().lower()

print("\n--- Verdict Report ---")


if swimmer != "yes" and swimmer != "no" and adult_present != "yes" and adult_present != "no":
    print("Error: Both of your yes/no answers were invalid. Please type 'yes' or 'no'.")
    exit()
elif swimmer != "yes" and swimmer != "no":
    print("Error: Your answer to the swimmer question must be 'yes' or 'no'.")
    exit()
elif adult_present != "yes" and adult_present != "no":
    print("Error: Your answer to the adult supervision question must be 'yes' or 'no'.")
    exit()



if age < 0:
    age_group = "Invalid"
    print("Age group: Invalid age entered.")
elif age < 12:
    age_group = "Child"
    print("Age group: Child")
elif age < 18:
    age_group = "Teen"
    print("Age group: Teen")
else:
    age_group = "Adult"
    print("Age group: Adult")



if age >= 12 and swimmer == "yes":
    deep_pool_allowed = True
    print("Deep Pool Status: Access Granted.")
else:
    deep_pool_allowed = False
    print("Deep Pool Status: Access Denied.")



if age_group == "Child" or swimmer == "no":
    print("Shallow End Warning: Please stay in the shallow end or stay close to the edge.")

is_adult_here = (adult_present == "yes")

if not is_adult_here:
    print("Lifeguard Reminder: No adult is present. Please listen closely to the lifeguard on duty.")

print("\nFINAL VERDICT:")
if age_group == "Invalid":
    print("Cannot determine entry due to invalid age input.")
elif deep_pool_allowed and is_adult_here:
    print("You are fully cleared for the deep competition pool with adult supervision.")
elif deep_pool_allowed and not is_adult_here:
    print("You are cleared to swim solo in the deep pool.")
elif (age_group == "Child" or swimmer == "no") and not is_adult_here:
    print("You must remain in the shallow end under direct view of the lifeguard.")
else:
    print("Standard recreational swim entry approved.")
