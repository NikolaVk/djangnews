# DjangNews

You can view the live website here. [link](https://djangnews.herokuapp.com/)

This is a news website where users can read the latest news articles. The articles are grouped within certain categories so it's easier for the user
to find what they may be looking for. There is also a search bar if the user wished to define a certain article they might be looking for aswell. The user
can make an account if they wish to, but is not necesary, however if the user wishes to join in on the conversation on a certain article by commenting on
the posts they have to make an account. Also to be able to leave a like on articles. The site is responsive so can be user on a laptop/desktop to a tablet
and mobile. 

## Table of contents
1. [UX](#UX)
2. [Features](#Features)
3. [Technologies Used](#Technologies)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)

## User Experience (UX)

- ## main goal

    - create a news website where users can join the conversation and/or give their opinion

-   ## User stories

    -   #### First Time Visitor Goals
        1. As a first time visitor I want to know what type of site is this. Expected users would be people 
           who we're looking through the web searching for an article or found themselfs scrolling through Google
           when they stumbled onto this site
        2. As a first time user I want to be able to find the right article or category I was searching for with ease.
        3. As a first time user I want to be able to easely navigate through the site

    -   #### Returning Visitor Goals
        1. As a returning visitor I want to see the site being updated on the latest news.

    -   #### Frequent User Goals
        1. As a frequent user I want to be able to make an account so I can comment my opinion on
            a certain article and/or join a conversation.

    ## Design
    -   ### Colour Scheme
        This website knows only 3 different colors. A black, white for the background and text and a very small percentage 
        of red. This is used within the logo and certain hover animations. The black and white make the site easely readable
        for everyone and the red adds a little variation wher is possible

        <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643168415/readme/colorscheme_t1gqru.png" centre centre no repeat>
    -    ### Typography
        The font comes form a bootstrap class "--bs-font-sans-serif" with bold added within the css which makes for a simple yet 
        clear and readable content. 
    -    ### Imagery
        Every category has an added image which at the same time acts as a heading for the category pages which makes it
        easier for the user to see if they switched pages.


## Features

- ### General

    - The computer nav bar contains everything a user needs. Starting from left there is the clickable homepage logo, 
    beside it the home button just to be sure. Beside the home button the user can see the categories with breaking news
    being outside the dropdown menu as it's mostly very important news and within the dropdown besids it the user finds all
    the other categories that the site features. This dropdown menu also has a hover feature so the user only needs to hover 
    over it with their mouse. In the centre the user will find a search bar where specific posts can be found.
    On the right side if the user is not logged in they will see a Register and Login button, however if the user does have an 
    accound and is logged in they will find a Logout button only. The entire navbar also has a sticky class which makes it always
    stay on screen as the user scrolls down altho is has some weird issues.

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643170942/readme/header-pc_iqpg5e.png" centre centre no repeat>


    - Underneath all the posts the computer user will find a footer which also contains all categories, but widouth a dropdown menu,
      instead all categories are center beside each other across the footer for easy acces to a different category. Beneath the categories
      there are some added social platform links. 

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643170942/readme/footer.pc_x5x5ps.png" centre centre no repeat>

    - With the mobile user the header rescales so the user is introduced with the hamburger menu on the right side of the header
      also with the logo still being a clickable home button on the left side. Within the hamburger menu the user will find the 
      same buttons, but the home button being on top following the breaking news, categories dropdown menu, the search bar and lastly
      the register/login or logout buttons. This nav also has the same sticky class, also sadly with the same issue.

    - It's the same story with the footer. All the categories are still reachable within the footer only will be stacked on top
      of each other. Only the social links remain horizontal.

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643171659/readme/header-footer-mobile_ct73gt.png" centre centre no repeat>
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643172173/readme/headerham-mobile_jsljmr.png" centre centre no repeat>

- ### Homepage 
    - The homepage is paginated with a maximum of 9 articles per page. Every post on the homepage features an image, title, excerpt,
      when the article is posted, the author and in which category it falls in. The posts are sorted by the time they are posted.
      This means the user will always see the newest articles on top of the page. All this also includes all the category pages
      accept the category page has a fitting image to let the user know they are viewing a specific category.

    <img src="" centre centre no repeat>
    <img src="" centre centre no repeat>

- ### Searchbar 
    - Like mentioned earlier the site contains a search bar which is made to be more specific in what the user wants to read.
      A search will bring the user to a page with the articles the user was looking for or the page will display an error message.

    <img src="" centre centre no repeat>

- ### Register, login and logout
    - The user is able to create an account on this page. This gives the user acces to leaving a comment and liking a certain 
      article. The user is requested to fill a username and password. An email is optional.

- #### Register page
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643174542/readme/register_gavyma.png" centre centre no repeat>
- #### Login page
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643174542/readme/login_xwueih.png" centre centre no repeat>
- #### Logout page
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643174542/readme/logout_nzw9g9.png" centre centre no repeat>

- ### Commenting 
    - As just mentioned the user is able to leave comments and like articles. Besides this if a user wishes to delete their comment
      this is possible with a delete button right underneath the comment. I also made sure that only the user that has made the 
      comment is able to delete it so other users will not be able to see this button. Same counts for users that dont have an account.

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643175025/readme/comments_uac5eg.png" centre centre no repeat>

- ### Admin site
    - The site has a section where only the owner of the site is able to enter. This is so that the owner can make new posts,
      remove comments and likes, delete registerd users. This section of the site is made using Django administration.

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643175320/readme/adminsite_bxqhnx.png" centre centre no repeat>

- ### Extra feature (clock)
    - There is a digital clock between the footer and the posts on the home page and all the category pages. This clock shows the
      local time and date.
    <img src="" centre centre no repeat>

- ### Future features
    1. When a user registers a account the user will get their own personal profile page where they can view all the articles they
       liked.
    2. Improve the search bar to be more specific than it is now.
    3. Add a weather api for the region a user is in.
    4. More categories and extra subcategories.

## Technologies Used

- ### Languages Used


- ### Frameworks, Libraries & Programs Used


## Testing

### HTML Validation

### CSS Validation

### JS Validation

###  Python Validation

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals


-   #### Returning Visitor Goals


-   #### Frequent User Goals

### Further Testing


### know bugs


## Deployment

### Instructions Making a Local Clone


### Deploying this project to Heroku

## Credits

### Code


### Content 


### images

### titles and texts

### Acknowledgements
