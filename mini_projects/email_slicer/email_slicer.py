while True:
    email = input("Please enter your email address: ").strip() # Obtaining user emaill address via input // strip() method is removing whitespace from beginning and end of string.

    if email.count('@') == 1 and len(email[email.index('@')]) > 0 and len(email[email.index('@') + 1:]) > 3:

        username = email[:email.index('@')] # using index() method slice out username with range up until @ symbol then storing as username.
        domain = email[email.index('@')+1:] # same method for domain but setting range after the @ symbol. 
        print("Your username: {}\n Your domain: {}".format(username, domain))  # Displaying output to user

    else:
        print("Invalid email: Please utilize the acceptable format hello@email.com")