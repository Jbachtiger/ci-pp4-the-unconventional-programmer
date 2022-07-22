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







