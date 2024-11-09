import os
import json

def add_to_zshrc(env_vars):
    # Get the path to ~/.zshrc dynamically
    zshrc_path = os.path.join(os.path.expanduser("~"), ".zshrc")
    # Open ~/.zshrc and append environment variables
    with open(zshrc_path, "a") as file:
        for key, value in env_vars.items():
            file.write(f"\nexport {key}='{value}'")
    print("Environment variables added to ~/.zshrc. Please run 'source ~/.zshrc' to apply changes.")

def parse_input(option):
    env_vars = {}
    if option == "1":
        # Comma-separated input
        user_input = input("Enter environment variables as comma-separated values (e.g., VAR1=value1,VAR2=value2): ")
        pairs = user_input.split(',')
        for pair in pairs:
            key, value = pair.split('=')
            env_vars[key.strip()] = value.strip()
    elif option == "2":
        # JSON dictionary input
        user_input = input("Enter environment variables as a JSON dictionary (e.g., {\"VAR1\": \"value1\", \"VAR2\": \"value2\"}): ")
        env_vars = json.loads(user_input)
    elif option == "3":
        # Single environment variable input
        user_input = input("Enter a single environment variable in VAR=value format: ")
        key, value = user_input.split('=')
        env_vars[key.strip()] = value.strip()
    else:
        print("Invalid option selected.")
    return env_vars

def main():
    print("Choose an option for adding environment variables:")
    print("1. Comma-separated values (e.g., VAR1=value1,VAR2=value2)")
    print("2. Python dictionary (e.g., {\"VAR1\": \"value1\", \"VAR2\": \"value2\"})")
    print("3. Single environment variable (e.g., VAR1=value1)")
    
    option = input("Enter the option number (1, 2, or 3): ")
    env_vars = parse_input(option)
    
    if env_vars:
        add_to_zshrc(env_vars)

if __name__ == "__main__":
    main()
