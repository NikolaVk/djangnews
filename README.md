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
- ## User Experience (UX)

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

    - ## Design
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


- ## Features

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

- ### Searchbar 
    - Like mentioned earlier the site contains a search bar which is made to be more specific in what the user wants to read.
      A search will bring the user to a page with the articles the user was looking for or the page will display an error message.


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
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643193688/readme/clock_x2klqb.png" centre centre no repeat>

- ### Future features
    1. When a user registers a account the user will get their own personal profile page where they can view all the articles they
       liked.
    2. Improve the search bar to be more specific than it is now.
    3. Add a weather api for the region a user is in.
    4. More categories and extra subcategories.

## Technologies Used

- ### Languages Used

    - HTML5[link](https://en.wikipedia.org/wiki/HTML5)
    - CSS3[link](https://en.wikipedia.org/wiki/CSS)
    - JavaScript[link](https://en.wikipedia.org/wiki/JavaScript)
    - Python[link](https://en.wikipedia.org/wiki/Python_(programming_language))


- ### Frameworks, Libraries & Programs Used

    - Heroku[link](https://id.heroku.com/login) was used to hoes the website
    - Django[link](https://www.djangoproject.com/) was used as the framework
    - Crispy forms[link](https://django-crispy-forms.readthedocs.io/en/latest/) was used for the django forms
    - Summernote[link](https://summernote.org/) was used to add the text editor for the content being posted
    - Bootstrap[link](https://getbootstrap.com/) was used to make the website responcive
    - Font-Awesome[link](https://fontawesome.com/) was used for the icons and favicon
    - Cloudinary[link](https://cloudinary.com/) was used as the database storage on the cloud
    - Fonticon[link](https://gauger.io/fonticon/) was used to create the favicon
    - Photoshop[link](https://www.adobe.com/products/photoshop.html?promoid=RBS7NL7F&mv=other) was used to create the watchface


## Testing

- ### HTML Validation

    - I ran the site through W3C Markup Validator[link](W3C Markup Validator) however as seen below it was not able to pass
      certain tests. I did add a lang attribute to the html tag, however the duplicate id's i cant replace. Technacly it is still ]
      one id, but because its related to bootstrap. For the image I could add a alt tag however because the image changes with 
      every new upload and I didn't know what else was possible

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643178110/readme/htmlvalidator_k0plpl.png" centre centre no repeat>

- ### CSS Validation

    - Here I ran the site through the W3C CSS Validator[link]https://jigsaw.w3.org/css-validator/. No errors returned here

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643178771/readme/cssvalidator_upp1i2.png" centre centre no repeat>


- ### JS Validation
    - For the JavaScript I ised jshint javascript validaror[link](https://jshint.com/) This returned no mistakes only one unused variable.

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643179227/readme/javascriptvalidator_fm2nc7.png" centre centre no repeat>


- ###  Python Validation

    Python was tested with PEP8 online[link](http://pep8online.com/) this returned no issues

    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643179419/readme/pythonvalidator_zy75d2.png" centre centre no repeat>

- ### Testing User Stories from User Experience (UX) Section

    -   #### First Time Visitor Goals
        1. As a first time visitor I want to know what type of site is this. Expected users would be people 
           who we're looking through the web searching for an article or found themselfs scrolling through Google
           when they stumbled onto this site

           - When you enter the site you are presented with various news articles and clear bold letters
             with a header full of categories for the user to go through.

        2. As a first time user I want to be able to find the right article or category I was searching for with ease.

            - In the navbar there is already a clear breaking news category and right besids it there is another button
              named categories. If you mis it and starts to scroll down firstly the nav bar will scroll with you to get 
              your attention and if you reach the bottom you will find in the footer an even clearer category list.

        3. As a first time user I want to be able to easely navigate through the site

            -  All the letters on the site are bold and everything is clearly visiable due to the black on white
               theme of the site

    -   #### Returning Visitor Goals
        1. As a returning visitor I want to see the site being updated on the latest news. 

            - On the home page and the category pages a constant wave of new articles will apear as time
              goes on

    -   #### Frequent User Goals
        1. As a frequent user I want to be able to make an account so I can comment my opinion on
            a certain article and/or join a conversation.

            - When you are logged in you are able to like the posts and comment/join a conversation on any
              article you want

- ### Further Testing

    - The site was tested in mozila firefox and google chrome on a laptop with a 17.1 inch screen and a 24inch monitor

    - On the left side is Mozilla Firefox on the 17.1 inch screen and right will be the Google Chrome on the 24 inch monitor
    <img src="https://res.cloudinary.com/nikv5296/image/upload/v1643180770/readme/testingscreens_ryanrz.png" centre centre no repeat>

    - I also tested the site on a 6.9 inch android phone and a 6.06 inch ios device

    - The same has been done on the dev tool with chrome

- ### Function testing

    - #### While making this site I made a several accounts to test out farious functions:

        - I tested out the creation of the account throught the register page. I tried this with leaving blank
          spaces for the password and same with the user name I got an error message after I left the username blank.
          I didn't get one with the password, but it did automatically send me to the password textarea. Also if I 
          fill in a short or simple password I did get an error message. The same with trying to log in with a wrong
          password and/or username I got an error message

        - The comment section was also put under a test to make sure if another user comented that I cant see the delete
          button and also same for the other side. Also deleting functions goes widouth any issue. Same as liing a post and
          seeing the count of likes go up with every new user liking the post

        - The search bar works nicely when searching for words, but it also works if I enter one single letter. I did not manage
          to fix this on time. However if I do enter something that isnt on the site I did get an error message. The same when I
          left the search bar blank and clicked on the search button, here I recieved a different error message



- ### Known bugs

    - The navbar has a sticky bootstrap class which should mean it will always remain on screen, however for some unknown reason
      it does not work properly. I tried looking it up, but did not get much brighter. Also this issue had a lower priority 
      comparing to other issues

    - On the mobile view my dropdown menu when clicked on does appear, but when it's clicked again on the same spot it does not
      respond. Also on the galaxy fold once clicked on the dropdown menu for some reason my hamburger menu icon moves to the right
      a couple of pixels, luckely it does not fall outside the screen So here is the same story like the bug above I had more urgent 
      issues that needed fixing first which took a long time.


- ## Deployment

This project was made using Gitpod and Github. This project has some secure information which is why an env.py file was used

- ### Instructions Making a Local Clone

    1. Make an account or login to Github and go to the main page of the repository[link](https://github.com/NikolaVk/djangnews)
    2. Above all the files besides the large green Gitpod button click on code.
    3. Now copy the link unter the HTTPS tab
    4. Open whatever code editor you use
    5. Open a new work directory or opan an existing one
    6. In the terminal type in git clone and then paste the url you copied behind it
    7. Now create a database using postgres on heroku
    8. In the terminal type: pip3 install -r requirements.txt
    9. Create an env.py file and add this:

    <pre>
    import os

    os.environ[
    "DATABASE_URL"
    ] = "postgres://zvzjfrqyqdswfc:8da2f5f3d54704d5707134b798556833fbbc60f3b4461f7cf99b924347e4af2b@ec2-54-229-47-120.eu-west-1.compute.amazonaws.com:5432/d8tum44ep5c08i"
    os.environ["SECRET_KEY"] = "your own key"
    os.environ[
    "CLOUDINARY_URL"
    ] = "cloudinary://582856596832186:JdZh8SuZ7eagE__mg9EPiRY4cco@nikv5296"

    </pre>

    10. Add the env.py file to gitignore so no one can see your personal information 
    11. And your ready to go just type in python3 manage.py runserver


- ## Deploying this project to Heroku

    1. Create an account on Herouk or login
    2. Create a new app within Heroku
    3. Set the region you are in or otherwiae the closest one to you
    4. After doing all that go to the settings bar and click on "Reveal Config Vars" and type in:

    <pre>
    Config Vars
    CLOUDINARY_URL  cloudinary://582856596832186:JdZh8SuZ7eagE__mg9EPiRY4cco@nikv5296

    DATABASE_URL    postgres://zvzjfrqyqdswfc:8da2f5f3d54704d5707134b798556833fbbc60f3b4461f7cf99b924347e4af2b@ec2-54-229-47-120.eu-west-1.compute.amazonaws.com:5432/        d8tum44ep5c08i
    SECRET_KEY      your own key!!
    </pre>

    5. Go back to Gitpod and type in:  pip3 freeze --local > requirements.txt
    6. After that create a procfile echo web: python manage.py > Procfile 
    7. Now add, commit and push to Github
    8. After doing that return to heroku and click on the deploy tab and chose Github as deployment method
    9. Now connect your repository name after that is ready
    10. Scroll down and click "enable automatic deployment"
    11. Click deploy and your ready to go

- ## Credits

- ### Code

    - This project is based on the Django Blog project made by Code Institute

- ### Images
    
    - #### Default post image
        - This image comes from Pexels and it was made by Anna Shvets[link](https://www.pexels.com/nl-nl/@shvetsa) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/aarde-model-vervagen-schade-5217882/)

    - #### Heading images 
        - This image comes from Pexels and it was made by ThisIsEngineering[link](https://www.pexels.com/nl-nl/@thisisengineering) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/code-geprojecteerd-op-vrouw-3861969/)
        - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/zwart-textiel-41949/)
        - This image comes from Pexels and it was made by Victor Freitas[link](https://www.pexels.com/nl-nl/@victorfreitas) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/persoon-met-barbell-841130/)
        - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/gele-harde-hoed-op-bruin-en-geel-brandweerkostuum-162540/)
        - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/twee-rode-papieren-organisatoren-265024/)
        - This image comes from Pexels and it was made by Eren Li[link](https://www.pexels.com/nl-nl/@eren-li) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/hand-lens-vervagen-zoomen-7188801/)

    - #### Posts Images

        - ##### Breaking News

            - This image comes from Pexels and it was made by Дмитрий Трепольский[link](https://www.pexels.com/nl-nl/@67117688) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/architectuur-kerk-historisch-rusland-8285167/)
            - This image comes from Pexels and it was made by Nataliya Vaitkevich[link](https://www.pexels.com/nl-nl/@n-voitkevich) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/gezondheid-laboratorium-medisch-geneeskunde-5863389/)
            - This image comes from Pexels and it was made by Eren Li[link](https://www.pexels.com/nl-nl/@eren-li) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/air-craft-overdag-40907/)

        - ##### Business 

            - This image comes from Pexels and it was made by Karolina Grabowska[link](https://www.pexels.com/nl-nl/@karolina-grabowska) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/verkoudheid-rood-cafeine-welving-4389667/)
            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/close-up-van-verlichte-tekst-tegen-zwarte-achtergrond-258083/)
            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/beursraad-210607/)

        - ##### Tech 
             
            - This image comes from Pexels and it was made by Z z[link](https://www.pexels.com/nl-nl/@z-z-2157359) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/lichten-bouw-service-bewegwijzering-6200343/)
            - This image comes from Pexels and it was made by Garrett Morrow[link](https://www.pexels.com/nl-nl/@garrettmorrow) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/foto-van-rode-en-zwarte-sony-ps4-dualshock4-2323435/)
            - This image comes from Pexels and it was made by Kindel Media[link](https://www.pexels.com/nl-nl/@kindelmedia) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/innovatie-robot-futuristisch-elektronica-8566472/)

        - ##### Media and Entertainment 
            
            - This image comes from Pexels and it was made by Craig Adderley[link](https://www.pexels.com/nl-nl/@thatguycraig000) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/foto-van-kasteel-overdag-3411132/)
            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/persoon-met-bruine-en-zwarte-gitaar-33597/)
            - This image comes from Pexels and it was made by Josh Hild[link](https://www.pexels.com/nl-nl/@josh-hild-1270765) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/spider-man-bovenop-gebouw-2854693/)

        - ##### Sport

            - This image comes from Pexels and it was made by Chris Peeters[link](https://www.pexels.com/nl-nl/@krizz59) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/man-rijden-op-racewagen-12795/)
            - This image comes from Pexels and it was made by Kindel Media[link](https://www.pexels.com/nl-nl/@kindelmedia) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/gras-golfbal-golfclub-golfvereniging-6572962/)
            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/olympisch-symbool-orientatiepunt-236937/)

        - ##### World 

            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/lichaam-van-water-34101/)
            - This image comes from Pexels and it was made by Artem Beliaikin[link](https://www.pexels.com/nl-nl/@belart84) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/foto-van-zwarte-kleding-op-hangers-1036856/)
            - This image comes from Pexels and it was made by Shoval Zonnis[link](https://www.pexels.com/nl-nl/@shoval-zonnis-1882145) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/wit-passagiersvliegtuig-vliegt-over-de-stad-tijdens-zonsondergang-3769532/)

        - ##### Travel
            - This image comes from Pexels and it was made by Tomáš Malík[link](https://www.pexels.com/nl-nl/@tomas-malik-793526) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/rode-en-grijze-pagodetempel-3408354/)
            - This image comes from Pexels and it was made by Pixabay[link](https://www.pexels.com/nl-nl/@pixabay) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/bos-in-de-buurt-van-waterlichaam-533881/)
            - This image comes from Pexels and it was made by Samson Bush[link](https://www.pexels.com/nl-nl/@samson-bush-1387215) Here's a link to the image[link](https://www.pexels.com/nl-nl/foto/twee-cruiseschepen-2678418/)

### Titles and texts

 - All news articles used in this project come from the news site CNN[link](https://edition.cnn.com/) 

### Acknowledgements

    - Thanks to my friends and family that we're eble to help me where possible
    - And aspecially thanks to the tutor support from Igor Basuga and Scott...