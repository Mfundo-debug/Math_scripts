import requests

# Set the URL for the Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLScL9CXHAZs8mR-PJogkANdGY9a9yTKNtekyFGNlWFEARwnopw/viewform?usp=sf_link"

# Set the name of the form field for the user's name
name_field = "entry.{field_id}"

# Set the name of the form field for the user's surname
surname_field = "entry.{field_id}"

# Set the name of the form field for the user's email
email_field = "entry.{field_id}"

# Set the name of the form field for the payment
payment_field = "entry.{field_id}"

# Set the URL for the payment gateway
payment_url = "https://www.example.com/pay"

# Set the amount to be paid
payment_amount = 50

# Function to make a payment
def make_payment():
    # Make a request to the payment gateway
    payment_response = requests.post(payment_url, data={'amount': payment_amount})

    # Return the payment response
    return payment_response

# Function to submit the form
def submit_form(name, surname, email):
    # Make a payment
    payment_response = make_payment()

    # Check if the payment was successful
    if payment_response.status_code == 200:
        # Set the form data
        form_data = {
            name_field: name,
            surname_field: surname,
            email_field: email,
            payment_field: payment_amount
        }

        # Make a request to submit the form
        form_response = requests.post(form_url, data=form_data)

        # Return the form response
        return form_response
    else:
        # Return an error message if the payment was not successful
        return "Payment failed"

# Get the user's name, surname, and email
name = input("Enter your name: ")
surname = input("Enter your surname: ")
email = input("Enter your email: ")

# Submit the form
form_response = submit_form(name, surname, email)

# Check if the form was submitted successfully
if form_response.status_code == 200:
    # Print a receipt
    print("Thank you for your payment of {}".format(payment_amount))
else:
    # Print an error message
    print("Error submitting form")
