# Testing

1. [**Development Testing**](#development-testing)
2. [**Manual Testing**](#manual-testing)
   - [**Responsive**](#responsive)
   - [**Navbar and Footer**](#navbar-and-footer)
   - [**Home**](#home)
   - [**Shop, Shopping Cart and  Checkout**](#shop-shopping-cart-and-checkout)
   - [**Blogs**](#blogs)
   - [**Member selection, Programs list and Subscription payment**](#member-selection-orograms-list-subscription-payment)
   - [**Dashboard**](#dashboard)
   - [**Login**](#login)
   - [**The Admin**](#the-admin)
3. [**Automated Testing**](#automated-testing)
4. [**Bugs**](#bugs)
5. [**Validation**](#validation)

---

## Development Testing

Using Django Framework comes with a very useful Debug function, that when When Debug is True. If there is an error in the code the live server will stop and print out an error code. \
This is printed out in the terminal and on the localhost. And because of this feature a lot of the bugs get fixed as they happen. so there arent that many which is good.

---

## Manual Testing

So with the manual testing section of this I went through each of the user stories which I had come up with and checked each one to 
make sure that the website works the way that it should.

#### User Story 1
- As a User I want to be able to view a list of games I can play so I can see what I want to play.

#### Test
- Clicked on the Game link in the top nav bar
- Then signed in as you have to be logged in to see the games section

#### Test result
- The test passed could login and view all the games on the website.

---

## Account testing

#### User stories
- As a User I want to be able to Easily Register for an Account so I can View my profile.
- As a User I want to be able to Easliy login and logout so I can Access my personal profile.
- As a User I want to be able to Easily Recover my Password So I can regain Access to my Account.
- As a User I want to be able to Recieve an Email Confirming After Registering on the site So I can Verify my Registration was successful.
- As a User I want to be able to Have a Personlized account So I can view my order history and save my personal Information.

#### Tests
- Clicked on the link to sign up for an account
- filled in my details to sign up
- the website then sent an email to confirm registration of account
- then logged back into website
- Clicked on my profile account link in my account at top nav bar
- Clicked on the reset password link in profile admin
- clicked on profile link to see order history
- updated personal details and clicked on the update information button
- clicked the logout button link in top nav bar

#### Test result
- the link correctly sent me to the signup form to signup for an account
- the details were okay and form validation was working as username was too short and email already exsisted
- The email was recieved to confirm email address
- successfully managed to login to website with details at signup
- the link successfully took me to my profile with all 3 blocks displaying correct information
- The link correctly took me to the reset password section and reset my password successfully
- the link successfully took me to my profile with the order history displaying correctly (if orders are present)
- details were successfully updated and changed and recieved success toast with correct message displayed
- successfully logged the user out and directed back to the homepage

No bugs were found during this testing section although did have an issue with displaying subscription even though subscription did
not exist yet so changed it so that all user that sign up get a free account straight away so this does not happen
and also changed the view on the profile page to reflect this.

---

