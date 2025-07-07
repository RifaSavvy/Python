# Get user inputs
is_sunny_input = input("Is it sunny outside? (yes/no): ").strip().lower()
have_umbrella_input = input("Do you have an umbrella? (yes/no): ").strip().lower()

# Convert inputs to boolean values
is_sunny = is_sunny_input == 'yes'
have_umbrella = have_umbrella_input == 'yes'

# Determine if you should go outside
should_go_outside = is_sunny or have_umbrella
if should_go_outside:
    print("You should go outside!")
else:
    print("You should not go outside!")

# Determine if you should carry an umbrella
should_carry_umbrella = not is_sunny or have_umbrella
if should_carry_umbrella:
    print("You should carry the umbrella!")
else:
    print("You should not carry the umbrella!")


