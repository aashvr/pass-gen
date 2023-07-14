import random
import string


def get_password_options():
    options = {}
    try:
        options['length'] = int(input("Enter the password length: "))
        options['include_letters'] = input("Include letters? (y/n): ").lower()
        options['include_numbers'] = input("Include numbers? (y/n): ").lower()
        options['include_special_chars'] = input(
            "Include special characters? (y/n): ").lower()

        if options['length'] <= 0:
            raise ValueError(
                "Invalid input. Please enter a positive integer for length.")

        if options['include_letters'] not in ['y', 'n'] or options['include_numbers'] not in ['y', 'n'] or options['include_special_chars'] not in ['y', 'n']:
            raise ValueError(
                "Invalid input. Please enter 'y' for yes or 'n' for no. ONLY")

    except ValueError as e:
        print("Error:", e)
        options = get_password_options()  # Prompt again in case of error

    return options


def generate_password_with_options(options):

    try:
        # Initialize the password string
        password = ""

        # Include letters
        if options['include_letters'].lower() == 'y':
            password += string.ascii_letters

        # Include numbers
        if options['include_numbers'].lower() == 'y':
            password += string.digits

        # Include special characters
        if options['include_special_chars'].lower() == 'y':
            password += string.punctuation

        # Generate a password of the specified length
        password = ''.join(random.choice(password)
                           for _ in range(options['length']))

        return password
    except Exception as e:
        print(e)


def main():
    options = get_password_options()
    password = generate_password_with_options(options)
    print("Generated Password:", password)


if __name__ == '__main__':
    main()
