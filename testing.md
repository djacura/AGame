# Testing

1. [**Development Testing**](#development-testing)
2. [**Manual Testing**](#manual-testing)
   - [**Account testing**](#account-testing)
   - [**Merchandise store testing**](#merchandise-store-testing)
   - [**Games Testing**](#games-testing)
   - [**Subscription Testing**](#subscription-testing)
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

---

## Account testing

This section is all about how I tested the Account part of the website from user stories

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

### Bugs 

- No bugs were found during this testing section although did have an issue with displaying subscription even though subscription did
not exist yet so changed it so that all user that sign up get a free account straight away so this does not happen
and also changed the view on the profile page to reflect this.

---

## Merchandise store testing

This section is how I tested the Merchandise store part of the website

#### User stories

- As a User I want to be able to see a specific category of product in the store so I can find what I want.
- As a User I want to be able to Search for a Product by Name or description So that I can find a specific prouduct I want.
- As a User I want to be able to Easily see what I have searched for So that I can decide wether I want the product.
- As a User I want to be able to View individual Product Details So it can See the Price, description and information.
- As a User I want to be able to View the total cost of my purchase at any time So I can avoid spending too much.

#### Tests

- checked the merchandise store and clicked on the category heading link
- typed search term in the search bar at the top of the page
- then also searched for terms only in description of product
- clicked on multiple prouducts to go to the product detail page
- Checked that you could see all valid product details listed
- Checked that you could see the Total cost after adding products to your cart#
- Checked that adding an item to the cart added an item to the cart
- Checked that you could remove or update item in the cart
- Checked that clicking on the cart link at the top took you to the cart

#### Test result

- after clicking the category link the products from that category successfully listed on the screen
- This then successfully listed out the products that matched this search criteria
- successfully managed to find products that matched searh criteria in description text
- after logging in which you have to do to view product details could successfully see product details
- Could successfully see all product details incl Price, description and other information
- Added multiple items to the cart and successfully changed the total amount in cart to User
- successfully managed to add an item to the cart
- successfully managed to change the amount of an item in the cart and also remove that item altogether
- link successfully took you to the cart and also so did the buttons on the toast

### bugs

- No Bugs were found during testing of this section of the website.

---

## Games Testing

This section is about how I tested the games section of the website

#### User Stories

- As a User I want to be able to view a list of games I can play so I can see what I want to play.
- As a User I want to be able to View the indiviudal games that I can play So that I can download them and play.

#### Tests

- Clicked on the Game link in the top nav bar
- Checked that could not see games details as needed to be a Pro member
- Signed up for a subscrition to be able to play the games
- Checked that could then see a list of the games to be able to play
- Checked could see the games details page
- Checked could click the button to play the Game
- Checked could search for a game that I wanted to play

#### Test result

- The link successfully took me to the games section of the website 
- before subscription went through, successfully saw toast that said you have to be a Pro member to view games
- Then signed in successfully and successfully subscribed to the website
- then clicked on games and successfully viewed game detail page
- All game details successfully loaded correctly
- Clicked the button to play the game but nothing happened as links not real
- successfully searched for games on webiste using game name or description term

### Bugs

- No bugs were found during this section although originally had it so that you could not see the games at all without a subscrition, but
found this was not good as users could not see what games they could play without subscribing to the website so some users would not sign up
as they did not know what they could potentially play. 

#### Fixes

- so to fix this I changed the format so you could not see game details without a subscription membership and this was a better format.
and allowed the user to be able to see the games they could play before subscribing they were more likely to subscribe, this
also came from user testing as well.

---

## Subscription Testing

in this section I tested the aspects of the subscription part of the website.

#### User Stories

- As a User I want to be able to View the subscriptions available to me So that I can see how much it costs
- As a User I want to be able to cancel my subscription at any point So that I no longer pay for it.
- As a User I want to be able to view my subscription status so that I can see if it is active or not.

#### Tests

- Checked that when signing up for an account that a free account was created
- Checked that when logged in that my profile showed a free account status
- Checked that when logged in clicking on subscriptions took the user to the subscriptions page
- Checked that the Correct Price was shown for each Subscription tier
- Checked that clicking on subscribe that it took the user to the subscription payment page
- Chcked that after subscribing the membership status changed
- Checked that the user could successfully cancel thier Subscription

#### Test result

- When signing up for an account on the Profile page the correct Free account was shown
- When logged in could see the subscriptions link in the top nav (could not see this if not logged in)
- successfully Redirected user to the subscriptions payment page and loaded correct subscription details
- the correct Price was loaded for each subscription and so was the correct subscription info for each tier
- The subscription payment went through successfully and sent the user an email invoice and redirected them to their profile page
- This then also showed the correct subscription status and also then showed the subscription date and next payment date and cancel subscription button
- Clicking on the cancel subscription button successfully loaded the cancel modal
- Clicking on confirm cancel subscription cancelled the subscription and then showed the correct tier in the Profile

### Bugs

- No bugs were encountered during this stage of testing.

---

