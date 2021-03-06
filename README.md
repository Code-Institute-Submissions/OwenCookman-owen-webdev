[Owen Cookman Web Developer](https://owen-cookman-web-dev.herokuapp.com/)
======
[![Build Status](https://travis-ci.com/OwenCookman/owen-webdev.svg?branch=master)](https://travis-ci.com/OwenCookman/owen-webdev)



The webpage was created to advertise myself as a web developer, showcasing my portfolio of previous projects 
which should be regularly updated as more projects are finished, giving those who visit the website an introduction to 
myself, the work I have done, a way to contact me for consultations and also a way to hire and pay me as a freelance 
developer.



## UX

The website is aimed at potential clients who would like to hire me as a developer.

### User Stories

As a visitor I expect:
1. To read about the developer and learn about their background
2. To see the developers portfolio of work to understand what they are capable of
3. To be able to contact the developer with any questions that I may have
4. To navigate the website easily
5. The information to be laid out in an easy to view format

As a User I expect:
1. To read about the developer and learn about their background
2. To see the developers portfolio of work to understand what they are capable of
3. To be able to contact the developer with any questions that I may have
4. To navigate the website easily
5. The information to be laid out in an easy to view format
6. To be able to hire the developer
7. To be able to see what options are available to me
8. To be able to select the options that I like
9. To be able to pay the developer for their services
10. To be able to keep in contact with the developer during the development process
11. To be able to provide feedback to the developer on their services

As the Developer I expect:
1. Visitors to my website to be able to learn about my background
2. To showcase my portfolio of work where possible to show visitors what I can offer
3. Visitors to be able to sign up to my website and become users
4. Visitors to be able to contact me with any queries they may have
5. Users to be able to see what packages I have on offer
6. Users to be able to select which package they want
7. Users to be able to give a description of their business and what their expectations are
8. To be able to keep constant contact with users who have hired me
9. Users to be able to pay me for my services
10. Users to be able to provide feedback where possible

### Styling Choices

#### Colours
I wanted to aim for a **neutral** colour palette with this website as my clients could be looking to build websites with 
a whole range of **themes**. This led me to look at neutral colour **groups**. I settled on a dark navy blue for the **nav** and 
**footer** elements, this would **seperate** them from other sections of the page.
 I decided to keep the page background **white** while content would appear on an **opaque field**. This allowed content 
 to be **stacked** within itself making the field around the inner content **darker** which would seperate **generated** content 
 even though they are generated in the same container for example when a user asks multiple questions.

#### Fonts
I decided to go with the [**Inria Sans**](https://fonts.google.com/specimen/Inria+Sans) font as it still looked **professional** and neat but also different from what is seen
on a lot of other web pages, I noticed that this **paired** well with the [**Roboto**](https://fonts.google.com/specimen/Roboto) font so I decided that any **titles** or **headers**
would be styled with [**Inria Sans**](https://fonts.google.com/specimen/Inria+Sans) and any other blocks of text would use [**Roboto**](https://fonts.google.com/specimen/Roboto). This further breaks content up and keeps 
the page looking interesting.

#### Favicon
The favicon was taken from [**PNG Fuel**](https://www.pngfuel.com/free-png/fdyur) I was looking for a **simple** icon that
would explain exactly what the website **involves**, the **laptop** with the </> symbol for **code** was perfect in showing that I 
am a **developer**. 


### Wireframes 

Please click [here](wireframes) to view my first draft Wireframes, these were originally made using Balsamiq Mock-ups.

#### Changes
The **'About Me'** page and **'What I do'** page were later combined on to the **index** page as this would be the landing point where
this information could be displayed to **sell** myself as a **developer** rather than having two small separate pages.


## User/Admin interaction
As there is no set price or time frame for a website to be built these could vary from website to website the superuser must 
interact with data submitted by a user so that the user can perform certain actions for example:

1. A user creates an order through the "Order" page
2. The Developer(Superuser) looks at the data submitted through the Admin panel, assesses how long and complex the build is and 
contacts the user via email with a price
3. A price is agreed upon so the Developer returns to the Admin panel and updates the orders "Price" field with the agreed price 
and checks the "Pay deposit" field
4. The user can then go to their profile page and look at the status of their order where a button to pay the deposit will be, 
clicking the button will take them through the steps of paying and once paid the Deposit paid field is automaticallly checked
5. When the developer has completed their work and the user is happy with the finished product. The developer can return to the 
Admin panel and check the "Pay final" field
6. The user can then return to their profile and make their final payment, this will automatically check the "Final paid" field



## Features

### Theme
The original **Theme** was taken from the **Bootswatch** themes library, the theme **Sandstone** was used and then styled with **CSS** to 
**customize** it further such as the **fonts** used and the changes made to the **navbar**, The **buttons** provided were kept the same
as the colours worked well with my **palette** but the **font** used in the **button** was **changed** to match the other text on the page.

### Index Page/Introduction
The **Index** page serves as the main **selling** page of the website, it includes a Large **call to action** button so a **user** can get 
straight to the steps needed to **hire me** as a **developer**. The button will **link** them directly to the `contact.html` page which is
a **login required** page. If the user is not logged in or registered they will be **redirected** to the `login.html` page which also 
contains a clear **link** to the `register.html` page.

Below the call to action button is a section of **icons** that show the **foundation** of what I can offer, clicking these icons will
open up a **modal** from the `modals.html` file that contain more **information** about each area. The **modals** open through the use of 
**jQuery**, each **icon** is given an **ID** that corresponds to its **modal**, **jQuery** waits for the icon to be **clicked** and runs the **function**
to **show** the **modal**.

The **modals** have been styled to appear **opaque**, as a lot of the features on the pages use opaque **backgrounds** that **layer** on top of
each other I wanted to continue that **theme** here and used a different colour so that the modal still **stood apart** from the rest of
the page. The text was coloured **white** so that anything that could be seen through the modal didn't draw the eye too much and **distract**
from the text.

On **smaller devices** this section is **hidden** and **replaced** with an **accordion** to make the page more **compact** so that the user can view
each section piece by piece.

As the **About Me** and **What I Do** sections are large areas of text and the user may only want to read them if they want to learn
more about me they have been placed within **collapses**, allowing the user to **show** and **hide** each separately.

An **animated** chevron has been added to give the user a que to **open** or **close** the **collapses**. This was animated through the use
of **CSS** styles and **jQuery**. jQuery waits for the element to be **clicked** and **toggles** a **class** which provides the animation.  

### Portfolio
The **Portfolio** page was originally planned to be made **dynamic** which is why it is sat in its own **app** but due to time constraints
it was not possible to implement this feature and this has been added to the "Possible Features To Implement" section.
The page displays all of my past **projects** and allows **users** to see what I have **learned** and what I am capable of **building**.
Each **image** shows the home page of each **project** and links to the **deployed** website. Included is a **link** to each **github** repository
and **information** about the **projects**.

### User Authentication
Visitors to the website can choose to **register**, this will allow them access to the `contact.html` page where they can fill out the
**order form** and **request** a website to be built. They will also have access to their **user profile** where order requests are **displayed**
along with **invoices** and any **questions** they have asked through the **"Contact Me"** page.

## User Profile
The **user profile** takes the user's **email** address and sends a **query** to the **database** to return the users **information**, It then takes
the user's **ID** and makes a **filter** request to the **database** for any **order**, **invoice** and **question** objects where the **client** field is
the same as the user's **ID**. These are then **rendered** on to the page through **template** rendering.

## Order Page
The **order page** uses the `ContactForm` model form which uses the `order` model, when the user fills out a **valid** form this **data** is saved
to the **database** along with some **unseen** fields, these fields are `client`, `date`, `price`, `pay_deposit`, `deposit_paid`, `pay_final` and `final_paid`
**client** is set with the value of the user's `ID`, the `date` uses `auto_now_add=True` to set the date and time to
when the form was saved to the **database**. 

`pay_deposit`, `deposit_paid`, `pay_final` and `final_paid` are all **Boolean** fields set to `False`
that are checked to **manipulate** data **displayed** on the **user's profile** as well as the **invoices** given when a **payment** is made. Finally
`price` is a **float field** that **defaults** to 0.0, this field is there to be **set** when a **price** is settled, it is used to display the
**cost** of the website on the **user's profile** as well as passed to **Stripe** for **payments**.

As the **developer** I would look at this **data** on the **admin panel**, assess how long the build would take and how **complex** it is 
(possibly contacting the user for any more information), settle on a price with the user, **update** the `price` field and set the 
`pay_deposit` field to `True`. This will then allow the user to **pay** the deposit through the **orders** section on their **profile** page
which is **half** of the amount **set** as the **price**.

### Contact Me Page
The **contact me** page is a simple **form** that takes the visitors **name**, **email** address and a **message**. This page is not **restricted** to 
users who are **logged in** as I want **anyone** to be able to ask a **qustion** or get in touch for any other reason, there is a **link** to 
this page in the **footer** so anyone can get in touch from **anywhere** on the website. The fields are saved to the **database** which are 
viewable through the **admin panel** for the case of visitors who are **not logged in** asking questions and also to **reply** to questions 
as there is a hidden **Answer** field. When a user asks a question their **ID** is also saved in a hidden `client` field which is allowed 
to be **blank** when a none logged in visitor asks a question. The `client` field is then used to **display** questions and answers on the
user's **profile page**, these questions can then be **edited** or **deleted** by the user.

### Stripe Payments
When a user has created an **order** and an agreement on **price** has been made the `pay_deposit` field in the `order` object will be set 
to `True`. This will **display** the price and a **pay deposit** button in the **"your orders"** section of the user's **profile**. clicking the
button will take the user through to a **summary** page which will show them a summary of what they are **paying** for as well as giving
them the option to **print** the page. The print page button uses **jQuery**, when the button is clicked a `window.print()` is run as part
of the click **function**. Clicking the **"Make Payment"** button will tke the user to the **payment** page where they can enter their card 
details which are passed to **Stripe** along with a **variable** `to_pay` which is set to **half** of the `price` value. If the payment
was taken **successfully** the `deposit_paid` field is set to `True`, the process is repeated again for `pay_final`. 

## Invoices
Once a user's **payment** is taken successfully an **invoice** is then created, using the `invoice` model the values are **populated** by 
drawing **information** from other **objects**, the `business_name`, `start_date` and `client` are taken from the `order` object. The 
`amount_charged` is taken from the `to_pay` variable and the `card_type`, `last4` and `stripe_receipt` are taken from the `customer` object
that is returned by **Stripe**. This **information** is then stored in the **database** to be made available through the **user's profile**.

### Footer
The **footer** was styled in the same colours as the **navbar** to frame the webpage. It contains a **link** to the `question.html` page so that
the page can be reached from **anywhere** on the website. It also incudes a **"signature"** and a link to my **LinkedIn** profile through a 
**LinkedIn** icon taken from **font awesome**. More social media platforms can be added to this section as they are created.


## Possible Features To Implement
- A more detailed contact form using check boxes that could give an estimated cost of the website build to the client
- A built in chat system allowing text communication to be handled completely on the website for example the chat system used
by Tutor support at CI
- The content on the portfolio page to be rendered from the database, with new entries uploaded from the admin panel
- Email notifications when visitors/users ask a question and invoices/confirmations sent to users email



## Technologies Used

### Languages
- This project uses **HTML**, **CSS**, **JavaScript** and **Python** programming languages

### Frameworks & Libraries
-[**Django 3.0.4**](https://www.djangoproject.com/)
- [**Stripe**](https://stripe.com/gb)
- [**Bootstrap**](https://getbootstrap.com/)
- [**FontAwesome**](https://fontawesome.com/)
- [**Google Fonts**](https://fonts.google.com/)
- [**Popper.js**](https://popper.js.org/)

### Tools
- [**GitPod**](https://www.gitpod.io/) was used as the development IDE
- this projects wireframes were created on [**Balsamiq**](https://balsamiq.com/)
- The build was tested with [**Travis Continuous Integration**](https://travis-ci.org/)

### Databases
- An SQLite database was used in development
- A PostgreSQL database is used in deployment


## Testing

To view the testing carried out on this project please click [here](TESTING.md) for my separate testing file


## Bugs

During the development process I ran in to a few issues, these are listed below along with how they were overcome:

**Bug 1**
When running the command python3 manage.py runserver the page 
would return 403 forbidden.

This was due to clearing browsing data to load new styles also 
clearing any permissions for GitPod.

**Bug 2**
When trying to save the contact form to the database an error 
stating column "client_id" of relation "comms_order" does not 
exist.

This was due to renaming a model field called user to client and
was fixed by deleting the database and its migrations and 
starting migrations fresh.

**Bug 3**
While deploying the project I received an error that the 
database is not configured correctly.

To fix this problem a file called runtime.txt was created in 
the root directory, this told Heroku what version of Python to 
use.

**Bug 4**
When attempting to pay via stripe on the deployed website I would
recieve a database error.

This was due to the stripe receipt url max length being set to 100
the SQLite database would allow the url to be stored even though it
was above 100 characters but the postgreSQL database used in
deployment would not.



## Deployment

The GitPod IDE was used to develop this project and all work was added, committed and 
pushed to a GitHub repository which was linked with Heroku.

### How to run the project locally
**Note:** some of the commands below may differ depending on your chosen IDE and Operating system, 
the commands below will work with python 3 installed on a Windows operating system. Some IDEs will
require "`pip3`" instead of "`pip`" or "`python3`" instead of "`python`" for example.

1. Ensure that you have PIP, Python 3 and Git installed on your machine

2. Save a copy of [this](https://github.com/OwenCookman/owen-webdev) repository by clicking the "Clone 
or Download" button at the top of the page and select "Download Zip" to extract the Zip file to your chosen folder 
    2. If you have Git installed, use the below command to clone the repository:

    `git clone https://github.com/OwenCookman/owen-webdev`

3. Open a terminal session in the unzipped folders directory

4. Create a virtual environment by running the below command

`python -m .venv venv`

5. Activate the Virtual environment with the below command

`.venv/Scripts/acivate`

6. Install required modules by running the below command

`pip -r requirements.txt`

7. inside the root directory create a file named env.py, at the top of the document type `import os` 
and add the environment variables shown in the heroku deployment using the following syntax:

`os.environ.setdefault("SECRET_KEY", "add your secret key here")`

Run the application with the below command

python manage.py runserver

Visit the website at http://127.0.0.1:5000



### How to deploy the project to Heroku
**Note:** You will require a publishable and secret key from [Stripe](https://stripe.com/gb).

1. In the terminal, run `python manage.py collectstatic` to collect static files for deployment on Heroku.

2. run the below command: 
    
    `Pip install whitenoise`

3. Go to your settings.py file and add `'whitenoise.middleware.WhiteNoiseMiddleware'`to the MIDDLEWARE section.

4. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

5. Create a `Procfile` using the terminal command `echo web: python app.py > Procfile`
    5. Please note that if you are using a Windows operating system the `Procfile` may not format 
    properly, please create another file named `Procfile` and copy the contents of the terminal 
    generated `Procfile` over to it, then delete the generated `Procfile`.
    As this project uses Gunicorn the Procfile I used appears like this:

    `web: gunicorn webdev.wsgi:application`

6. `git add` and `git commit` both `requirements.txt` and `Procfile` then `git push` your staged files to GitHub.

7. Create a new app on [Heroku](https://www.heroku.com) by clicking the "New" button on the Dashboard, give the new 
app a name and set the region to your local region.

8. From the new applications dashboard click the "Deploy" tab and in the "Deplyoment Method" section select GitHub and 
confirm that it is connecting to the correct GitHub repository.

9. Click on the "Resources" tab and in the search bar search for "postgres", select "Heroku Postgres" when it appears.
Select "Hobby Dev - Free" and click "Provision", go to the "settings tab and click the button "Reveal Config Vars" in the
config vars section to see that a config var "DATABASE_URL" has been set.

10. Continuing in the cofig vars section set the below config vars.

    | Key | Value |
    |---|---|
    | DATABASE_URL | `Database URL should have been set in the previous step` |
    | DEBUG | FALSE |
    | SECRET_KEY | `<Your Secret Key Here>` |
    | STRIPE_PUBLISHABLE | `Your publishable stripe key` |
    | STRIPE_SECRET | `Your secret Stripe Key` |
    

11. Go to the "Deploy" tab and scroll down to the "Manual Deploy" section check that the master branch is selected and 
click "Deploy Branch".

12. Go to the "Overview" tab, after a few minutes the top two logs should read "Deployed" and "Build Succeeded".

13. Select the button "Open App" in the top right corner and wait for the home page to load.



## Acknowledgements
- My family and friends for testing this project and reporting back to me with any issues.

- My mentor [Simen Daehlin](https://www.linkedin.com/in/simendaehlin/) for his brilliant tutelage

- [Joke Heyndels](https://github.com/Wings30306) for her guidance in squashing particularly tricky bugs 
