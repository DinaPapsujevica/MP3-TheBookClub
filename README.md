# The Book Club

Milestone Project 3 - Python and Data Centric Development

The website is created with the purpose to motivate people to read more books and share their opinions about the books they read.
The site will be targeted at the people who love to read books and people who doubt what to read.
Nowadays there is a huge choice of books for different ages, interests, and topics. Any one of us can get confused in this sea of books.
That is why book review and recommendation sites are here to help solve it. 
Existing user book reviews will help to choose and understand which could be your next book to read.
Go to website ...

## UX

### Mockup

![The Book Club mockup]()

### User stories

As a first time visitor, I want 
- to immediately understand what is the purpose of this website
- to see the content without being register
- to be able to see the content by Categories
- to be able to register easily without needing to input a lot of personal information
- to see that website is active and when is the latest book review added 

As a returning user, I want 
- to Log In and Log Out easily
- to be able to add new book review easily
- to be able to edit or delete my book reviews
- to upload my own images using URL
- to have my dashboard and see all my reviews
- to Delete my profile easily

As a site owner/admin I want
- to be able to edit and delete content created by users
- to be able to add, edit and delete categories

### Design Choices

The overall feel of the website is clean and not crowded. 
As a main element of the website, I chose a bright background image with a girl on it.
The image gives the right mood and fits the headline.

#### Fonts

A website is made with Bootstrap, all fonts were given by default. 

#### Colours

As the background image was chosen in bright color itself, all other element colors are chosen neutral. For example, text color is white,
buttons and icons are nude/brown shade, the color name is Contessa.
This color was chosen because the same shade is a girl's sweater. This color match gives an overall clean feeling.
The only elements which differ are Edit and Delete buttons. 
They were left with their original color from Bootstrap, emphasizing these call-to-action buttons.

#### Icons

All icons used were chosen for their meaning and purpose so that everyone can understand them. 
The icon color is the same as the buttons and fits with the design.

Website consists of 5 sections:

- **Landing page**
- **Log In**
- **Register**
- **Profile**
- **Add Book** 
- **Manage Categories**

Wireframes are available here:

![Landing page](static/wireframes/w-1.png)
![Landing page](static/wireframes/w-2.png)
![Landing page](static/wireframes/w-4.png)
![Landing page](static/wireframes/w-3.png)
![Landing page](static/wireframes/w-5.png)

## Features

### Existing Features

Navbar on top helps user to navigate through the website. If you are logged-in user your Navbar shows more options than for the first-time visitor.
Web site Name in the left corner always brings the user back to the Landing page.
On the medium and small sizes, the user can open the navbar from the burger icon on the right top of the website. 

### Landing page

The Landing page includes a background image that gives an overall mood and is eye-catching with its main element-girl with the book in her hands.
Above the main element - the girl, there is the headline and inviting, call to action button, which takes the user to the Register page.
As a user, you can see randomly chosen other user book reviews. Reviews are listed in the column on the left side for the desktop version and in the center for the mobile version.
For the desktop version, reviews are listed on the left side and category list on the right side from the girl image.  
For the mobile version, reviews and categories are listed in the center.
As a user, you can see all book categories which is added by the website's admin. 
By pressing on one of the categories you are taken to another page with a book list which was added to this category by users.

### Log In

As a user, you can see Log In form with Username and Password input fields. 
You must be a registered user to be able to Log In.
If the user is not registered yet, below the Log In form, there is a link that brings the user to the Register form.
After pressing Log In button, the user has been directed to a Profile page.

### Register

As a new user, you can Register to a webpage by filling the Register form with Username and Password input fields.
If the user uses an already existing username, flashes the message, that the Username already exists.
If registration was successful, the user has been directed to the Profile page.

### Profile

As a user, you can see your Profile page where you can see and manage all your added book reviews.  
User's reviews are listed in a row and gives you the option to Edit or Delete it.
As a user, you are able to add a new book review by pressing the button Add Book which is located above the list.
After pressing the button, the user has been directed to Add New Book Review form.

### Add Book

As a user, you are able to add a new book review by filling out the form. All input fields must be filled in to be able to submit the form.
You are able to Cancel this action by pressing the Cancel button below the form.
Canceling this action clean form will be displayed.

### Manage Categories

As an admin, you are able to manage existing Categories.  
If you are logged in with an admin username, your Navbar shows the option Manage Categories.
Pressing the link, an admin has been directed to the categories page, where all categories are listed in columns and offers the option Edit or Delete them.
As an admin, you are able to Add, Edit, or Delete the Category by pressing the call-to-action buttons.
Pressing the button Add Category admin can see a form that needs to be filled in and submitted.
After submitting admin has been directed back to the category page where the added category has been listed together with others. 
All categories are listed in alphabetical order.


### Features left to implement

- In the future, I would like to add a section with books that are most reviewed. Section name could be - Most read books by our users.
- I would like to implement that visitors can see how many active users this website has.
- Every time when admin adds a new Category, this Category automatically adds to the list on Landing page.

## Technologies Used

- HTML
- CSS 
- JavaScript
- Python+Flask
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- jQuery
- MongoDB

## References

- Code institute video projects, especcially Mini Project by Tim Nelson
- [W3scools.com](https://www.w3schools.com/)
- [Stackoverflow](https://stackoverflow.com/)
- [WebFX](https://www.webfx.com/blog/web-design/responsive-background-image/) 

## Testing

For testing code validity i used:

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JavaScript Validator](https://jshint.com/)
* [Python Validator](http://pep8online.com/)


## Deployment

To deploy website to Heroku, I take following steps:
- Create a requirements.txt file by writing terminal command pip freeze --local > requirements.txt.
- Create Procfile using terminal command echo web: python app.py > Procfile.
- Log In into my Heroku.com account and click "New" > "Create New App" button in my dashboard. Give it a name and set the region to Europe.
- From the dashboard, click "Deploy" and choose GitHub as Deployment method. That will setup automatic deployment from GitHub repository.
- Add my repository name and confirm it by clicking "Connect".
- From the dashboard, click "Settings" > "Reveal Config Vars".

KEY | VALUE
----|-----
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | <your_secret_key>
MONGO_URI | mongodb+srv://<username>:<password>@<cluster_name>.6wwxi.mongodb.net/<database_name>?retryWrites=true&w=majority
MONGO_DBNAME | <database_name>

- Back in terminal write command git add requirements.txt and git commit -m "Add requirements.txt", 
the same with Procfile - git add Procfile and git commit -m "Add Procfile" and then git push the project to GitHub.
- In the heroku dashboard click "Deploy". 
 

## Credits

### Content

All the content on this website was written by me.

### Media

Background image was taken from [Shutterstock](https://www.shutterstock.com/da/image-photo/beautiful-young-woman-warm-sweater-book-1656315796).

### Acknowledgements

- I received inspiration for this project from Code Institute Mini Project by Tim Nelson 
- Code Institute tutor assistance
- Slack community


Website is created for educational use!
