import c8_module as p

print("-----------------------------")
p.make_pizza(16, 'pepporni')
p.make_pizza(12,'mushroom', 'green pepper', 'ham')
print("-----------------------------")

def greet_user(username):
    """Display a simple gr
    eeting."""
#    print(f"Hello!, {username.title()}")
greet_user('jessie')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')