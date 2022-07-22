# PP4 - Full Stack Toolkit - The Unconventional Programmer

## Introduction
The Unconventional Programmer is a blog/reddit style website targetted at aspiring and junior developers. This site aims to share useful resources that will help people who have taken unconventional routes into programming and are at the start of their careers. It is a site that allows users to share their personal experiences via either creating a blog post themselves or commenting on existing ones.

The website was built in Django using Python, JavaScript, CSS and HTML. Users are able to create, edit, read and delete posts. On login a profile is automatically created for them which users can click into and edit/update. They are able to upload images for their blogs as well as a profile picture. Users can also comment on and like/unlike posts.

The site provides role based permissions for users to interact with the central dataset. Included is user authentication and Full CRUD functionality for blog posts. 

![Mockup](docs/mockups/site-mockup.png)

## Live Site
[Click here to view live site](https://the-unconventional-programmer.herokuapp.com/)

## Table of Contents
- [User Experience (UX)](#user-experience)
    - [Site Goals](#site-goals)
    - [Epics](#epics)
    - [User Stories](#user-stories)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Colour Scheme](#color-scheme)
    - [Fonts](#fonts)
- [Agile](#agile)
- [Database Schema](#database-schema)
- [Features](#features)


## User Experience
### Site Goals
- To provide users with a place to find helpful resources about early careers in programming
- To provide users a place to share their own knowledge and experiences
- To provide users a place where they can feel part of a community of like minded individuals
- To show users that they are not on their own and their are many people in the same shoes as them and feeling like them
- To show users that it get's better and that coding is a fantastic career choice

__Sites Ideal Users__
- Career changers currently studying at a coding bootcamp
- Junior developers who are right at the beginning of their work journey
- Graduates of programming related degree's
- People looking to share their experience and knowledge with those less experienced

### Epics
6 Epics were created which were further developed into 20 User Stories. The details of each epic along with the associated user stories can be found in the kanban board [here](https://github.com/users/Jbachtiger/projects/2). 

1. Initial Django Setup [#1](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/1)
2. User Profile [#5](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/5)
3. Sign in/Sign Out [#12](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/12)
4. Blog Post [#17](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/17)
5. Site Owner Goals [#24](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/24)
6. Site Search [#15](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/15)

### User Stories 
20 User stories were created from the 6 Epics and assigned the classifications of Must-have, Should-have, Could-have and Won't have. Each user story also includes acceptance criteria and tasks that need to be completed in order for that story to be closed. 

Below are links to each of the individual user stories that were completed within the projects initial release.

1. Initial Django Setup
    - Install Django and supporting libraries [#2](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/2)
    - Keep secret keys secure [#3](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/3)
    - Early deployment of site to Heroku [#4](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/4)

2. User Profile
    - Register for an account [#6](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/6)
    - User can view their profile [#7](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/7)
    - User can edit their profile [#8](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/8)

3. Sign in/Sign Out
    - User account Sign in/Sign out [#13](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/13)
    - Features applicable to signed in users only [#14](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/14)

4. Blog Post
    - Create a blog post [#18](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/18)
    - View a blog post [#19](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/19)
    - Update a blog post [#20](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/20)
    - Delete a blog post [#21](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/21)
    - Like/Unlike button [#22](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/22)
    - Comment [#23](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/23)

5. Site Owner Goals
    - Responsive templates [#26](https://github.com/Jbachtiger/ci-pp4-the-unconventional-programmer/issues/26)


For ease of reading, I have also listed all the completed user stories below:

- As a developer, I can set up Django and install all the supporting libraries to get started with the project, so that I am ready to start development
- As a developer, I can set up the Django development environment to secure the secrete keys, so that I do not expose the secret keys to the public or a party that should not see them
- As a developer, I can deploy the site to Heroku, so that I can confirm that everything is working before the development of the site and enable continuous testing with the production environment
- As a user I can create an account by registering my details so that I can comment and like posts
- As a user I can see the details of my user profile so that I can see my info and what others can see about me
- As a user I can edit my profile so that I can keep my information up to date
- As a user I can sign in and sign out of my account so that I can keep my account secure and private
- As a site owner I will restrict some features of the site to registered users only so that it encourages users to create an account with the site
- As a user I can create a blog post so that I can share my ideas and experience
- As a user I can read the blogs on the site so that I can benefit from the information shared
- As a user I can update a blog I have created so that I can correct mistakes I've made
- As a user I can delete a blog post I have written so that I can remove it from the site
- As a user I can like or unlike blog posts so that valuable blog posts are recognised as good content
- As a user I can comment on blogs so that I can have a community discussion around the topic and gain further insights
- As a site owner I can create my site to be fully responsive so that it provides a good user experience on all devices

## Design
### Wireframes
Before coding commenced, a set of wireframes were created to help me visualise roughly what my website would look like on desktop, tablet and mobile. It provided a starting point for me in terms of design. The finialised project went through many iterations and has changed from the inital wireframes however, inspiration was taken from these wireframes. 

- Homepage
![Homepage](docs/wireframes/homepage.png)

- Blog Page
![Blog Page](docs/wireframes/blog-page.png)

- Profile
![Profile](docs/wireframes/profile.png)

- Sign-in
![Sign-in](docs/wireframes/sign-in.png)

- Sign-up
![Sign-up](docs/wireframes/sign-up.png)

### Color Scheme
- The colour scheme has been carefully chosen to ensure accessibility for all
- The colours compliment each other and ensure text is easily read
- The colours are consistent throughout the website and are used for specific purposes
- The main colours used throughout the website are:

![Colour Palette](docs/colour-palette/colour-pallette.png)

As well as #8C6D89(light purple), #fff (white).

### Fonts
The font used in this project was Roboto with a backup of sans-serif. It was chosen for it's easy readabilty for users. Fonts were imported using Google Fonts.

## Agile
Throughout this project an agile approch was taken to developing the website. Each activity was broken down into smaller bite-sized more manageable actions from initially creating 6 Epics, which were then broken down into smaller User stories. Each of the user stories then had an acceptance criteria and list of tasks to complete. This made the overall project much more managable to build. GitHub labels were used to categorise the User Stories using the MoSCoW Prioritisation technique. This clealy defined what tasks were most important to complete and where the focus should be.

As mentioned above, a kanban board was created using GitHub Projects [here](https://github.com/users/Jbachtiger/projects/2) to help keep track of all the tasks including Todo, In Progress, Done and Future Development.

![Kanban First Stage](docs/kanban/kanban-board.png)

![Kanban Second Stage](docs/kanban/kanban-board-1.png)

![Kanban Third Stage](docs/kanban/kanban-board-2.png)

![Kanban Fourth Stage](docs/kanban/kanban-board-3.png)

## Database Schema
Smart Draw was used to create a database schema to visulise the types of custom models this project might require. This schema was used as a guide to what needed to be added into each model. In the end only the Blog Post, Comment and Profile models were used. AllAuth was also used for the authentication system. This uses the built in Django User Model.

![Database Schema](docs/database-schema/database-schema.png)

## Features
### Homepage

A simplistic homepage which clearly shows the sites purpose. The user is able to look through various blog posts until they find one that interests them. The purpose of this section is to introduce the site, have minimal distractions so the users attention is immediately drawn to the blog posts.

![Homepage](docs/features/hompage-website.png)

### Navbar

The navigation bar is featured on all pages, is responsive and has active links functionality so the user knows which link they are on by hovering on it in the navbar. It is identical on all pages and is easy to user to provide a good user experience. For mobile view the navbar reduces to a burger menu. The purpose of this feature is to allow users to navigate all pages easily across all devices without having to use a back button to get to the next page. Their is also authentication in place which will change what displays on the navbar depending on whether a user is logged in or not.

- Logged out Navbar

![Navbar](docs/features/logged-out-navbar.png)


- Logged in Navbar

![Navbar](docs/features/navbar.png)

### Footer

The footer section includes links to relevant social links which all open up in a new tab to allow easy navigation for the user. They also have a hover effect added to them to make them stand out more and obivious to click. The copyright section is in place for legal reasons and the date is automatically updated using JavaScript. The footer is a good way to encourage users to connect via social media.

![Footer](docs/features/footer.png)

### Blog Posts - List View

The blog posts on the homepage are displayed in a single list view and provide a summary of what the blog contains. This provides user some quick information to see if they would like to find out more information about it including who submitted it, when it was published, the topic of the post, a short summary and how many likes it has received. This fields have all been included to provide the user a better experience and be able to make an informed decision as to whether they would like to continue into the blog post to read it.

![Blog Post - List View](docs/features/blog-post-list-view.png)

### Pagination

The blog posts have had pagination functionality added to them so that 3 posts are displayed on each page. This has been implemented to improve the user experience and not overwhelm the user with information and blog posts. 

![Pagination](docs/features/pagination.png)

### Blog Post

Each post has a title followed by a submitted by field. There are also Edit and Delete buttons which have been put at the top of the page to ensure the user doesn't miss them. The main content is then added using the WYSIWYG CKeditor which provides basic styling and image uploads. At the bottm of the blog post there is a section for users to leave comments and talk to each other as well as a like/unlike option. The purpose of the blog layout is to make it as easy as possible for user to read the content, digest it and then contribute to it in the form of comments and likes. 

![Read Post](docs/features/read-post.png)

### Comments

Each blog post has a comment section where users can post their comments for that specific blog. The user can see the number of comments that have been made on the post, the name of the user who wrote each comment and when that comment was published. Users can only make a comment when signed in and will be prompted to sign-in or sign-up to in order to leave comments. This is a great way for users to interact with each other and the publisher, discuss the topic and ask/answer questions.

- Not signed into account

![Comments](docs/features/comments.png)

- Signed into account

![Comments](docs/features/comment-1.png)

### Likes

The user also has the ability to like and unlike blog posts. The purpose of this is to proivde useful feedback to the community on how popular/good a post is by rewarding that post with likes. If a user changes their mind they are able to remove their like from a post. Each like is counted on the blog page as well as on the homepage where the blog list sits. If a post is unliked by a user this is reflected in the count.

- Like

![Like](docs/features/like.png)

- Unlike

![Unlike](docs/features/unlike.png)

### Login / Logout / Sign-up

Django Allauth was installed and used to create the register, sign-in and sign-out functionality meaning the project would have the authentication foundations in place to expand functionality in future. These pages are needed to provide authenication and to allow users access to content that is restricted to those who have created a login. 

- Login

![Login](docs/features/login.png)

- Logout

![Logout](docs/features/logout.png)

- Sign-up

![Register](docs/features/register.png)

### Create a Post

If the user is logged in they can create a post. Current fields being captured include title, title tag, summary (which is used to display on the homepage), body (using the ckeditor) and topic. 

![Create a Post](docs/features/create-a-post.png)

### Edit a Post

If the user is logged in they can edit a post they have created but not anyone elses. Same fields are included as with create a post.

![Edit a Post](docs/features/edit-a-post.png)

### Delete a Post

Once a user has created a post they have the ability to delete their own post. They can do this by access the blog which they have created and wish to delete and clicking the delete button at the top of the page. They will then be taken a page asking them if they are sure they wish to delete their blog and to click confirm or go back to their blog page. 

![Delete a Post](docs/features/delete-a-post.png)

### Profile

Once a user registers, they will have a profile page automatically created for them. The link to their profile page will appear in the navigation bar once logged in. If they navigate to this page, they will be able to update their username, email address, add a bio and upload an image. The purpose of this page is to proivde users with more control over their account and start to be able to customise their data. 

![Profile](docs/features/profile-signed-in.png)

### Messages

To provide users with more feedback after they take certain actions, a messaging system has been added to let users know their desired actions have occured. For example:

-  Login

![Login](docs/features/login-message.png)

- Logout

![Logout](docs/features/logout-message.png)

- Profile Updated

![Profile Updated](docs/features/profile-message.png)

These messages last for 2 seconds before automatically being timed out. Alternatively the user can click a little x to remove them.



