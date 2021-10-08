### Project 4 Backend



SWAPxSHOP

Overview

SWAPxSHOP is a site for users to shop for second-hand football kits. With a fully RESTful Django backend that explores relationships between the users and the kits. We also wanted to try to build an e-commerce site with a working shopping cart. We also decided to use Bootstrap for styling.

Deployment

This web app has been deployed with Netlify and Heroku and is available [here](https://swapxshop.netlify.app/).

Brief

Build a full-stack web application using ReactJS for the frontend and a postgreSQL backend with a Django REST framework and Python. I had one week to complete this project and worked with [Nnanna Uwakwe](https://github.com/Uwaks).

Technologies Used

-   HTML5

-   Sass

-   React-Bootstrap

-   ReactJS

-   JSX

-   Cloudinary

-   Python

-   Django

-   postgreSQL

-   Insomnia

-   TablePlus

-   Trello

-   GitHub

Process

My partner and I spent one day planning our project through the use of a wireframe and database diagram. We used a Trello board to stay organized and on track through the build.

![](https://lh3.googleusercontent.com/bFCH0rwoLwRvYIKBhInlKX4FHsDoqVRJjOIrQcvykcu9UoRlpwjZtPZSuYhEPuYrsB8-BTn99HG9ZGFbAypm3VlGcsjoFhbOvbGlwwc_fHQeKUHnt1-Y5KJc5dLf8eVzR9-6vDWH=s0)

![](https://lh4.googleusercontent.com/f4TNT_fpgMMNXOkZ87xccJLRonZLO_vpgzeF4F2zScXWcJ7b4fMPcobj6DjgdzEVkiX72xPT5Dd2g82by-KfSVCiCgLGIdD_5lKKylIhNaVSEWsQksxAmrwEhedD5QLjo0KkSS1S=s0)

When we were ready to begin coding, we decided to begin and work as a team on the backend. We added models, views, and serializers for the items and users. As we tested functionality we added serializers and updated views. Once the backend was complete we added seed data and moved to the frontend.

As a team, we hooked up the backend to the front end. Then we divided up the tasks to complete the frontend. My partner worked on the Navbar, shopping cart, and checkout  functionality.

I began by creating the itemIndex page and the itemCards to populate the page. As I built the page I used very basic styling to get each piece in the right place. I had not used React-Bootstrap much before, so I learned as I was coding. This meant that I made use of the Card, Container, and Buttons in the early stages.

I built the itemShow page and added functionality to display similar items.

![](https://lh3.googleusercontent.com/_3WgM2GgNCDeXPeCPfOPoZWDzAAmu_9Z0sS8pqtNRmWbMocw_KU77RFk5XJTH2gfxT3YzYgRSxEA1HHKzkXtipbD3YmoiL3cEp4fYIoqaK7uH9363a9vt7dVfRBc4IFjBD8T9tW_=s0)

I built the registration form and page, the login form and page, and the itemCreate form and page. I linked the photo upload to a Cloudinary account.

I added a hero image and functionality to display recently added kits to the home page.

I created a user profile page that displays their purchases, sales, and favorites. Then I added the frontend functionality to "like" a kit. I added comments to the itemShow page.

I updated the createItem form to have a select option for the team name. Forcing users to post items with a uniform team name allowed me to create a dropdown filter to search by team on the index page.

As a team, we began styling together so that we agreed on what to do and then we each styled the pages we built. I styled the register, login, createItem, home, index, show, createComment, and profile pages.

On the last day of work, I tried to execute smaller pieces of work that cropped up as we walked through the user journey. This included adding error handling to the fields on the forms, correcting some buttons and labels, and removing extraneous console.logs,

Known Bugs

-   Can't update the boughtBy status on the items or the inverse field.

-   The shopping cart process doesn't lead anywhere.

Challenges

We struggled to get the boughtBy and itemBought fields working correctly in the backend. In the end, we needed some help to see that we were creating a new user when we used the NestedUserSerializer. We needed a distinct serializer to get the userID of the buyer and populate it. Using Insomnia we were able to give items a boughtBy field and users an itemBought field, but we were not able to realize this on the frontend. That will be a future improvement that will allow us to show purchase history in a user's profile and remove purchased kids from the shop index page.

I also would have liked to have had more time to work with the forms. I think there's a large opportunity here for refactoring. For example, I think I could work on combining the list of teams on the index page used for filtering and the list used for creating a new kit for sale. I tried to make this list its own component and import it in both instances, however it only worked for the kit creation. I think with more time I could have simplified this and made it work for both.

![](https://lh6.googleusercontent.com/zBd7c2coBjrNxNcmRCF_1GmzLiR3UmMWzH7A37_T0tmNHRpoMXnHGMQxnnIc2TtDgjBiISQaUopvNRMjd-Jv5DwYysO4Ljr4iVodkkGK2KuW2thWdmO363j8fzz0VCTrgxbHoJDl=s0)

Wins

This project was helpful for me to build my own PostgresQL database with Django REST Framework. I benefited from creating the views and serializers. We initially used the rest_framework.generics for our Item views. This caused a problem when we needed to add a sellerID to newly created items. I realized the generic was bundling the create and index views together and preventing us from attaching the information we needed. So, I split them into two unique views and was able to populate the sellerID.

![](https://lh5.googleusercontent.com/UMVO6vP1gx5lBNr2Tun2oSyAVmmyQ5MDLOjC7sj3DFWCzLBOYcAoYAYM2UMud2tHf5Zx42uNv5cTXwe55bk10jYEclhhy6gLk3NAQLVRHgFEM0UDYX0YSHM_RdcLwrPbNKNPDcrU=s0)

I also enjoyed getting the practice of making the frontend. I was able to solidify several pieces of coding that were used in my group project 3, [MuggleMore](https://muggle-more.netlify.app/). For example, the code to display the most recently added kits.

![](https://lh5.googleusercontent.com/GSwro807Ri8n2PIWKfZboiM4A0cv7W5rmNPZhj9DvC8wms6_W4_4Po-Mu4UW8rPeiXFjwve-95SZE8kh1ksFIvf8MKrS7fZijTi95-zgeHWrITl8vjDGFUgNo4eU1tpza8SkjVif=s0)

![](https://lh5.googleusercontent.com/zW4D2Qk24wvsDk194vKGPWoveSjevuk8A6KX-yZ5Bq7gnYC_wriUvJ4ZqTmARPYbd0yg2Ub5sd9J09_owJxv8WYmvkXum7mG9vplL3ZGnEV8pFSKg-GFJhSbmu3cSDwH0IfTTlGz=s0)

Future Improvements

-   Get the boughtyBy fields to update correctly.

-   Use Faker to add user seed data.

-   Update the shopping cart.

-   Create a custom hook for the forms.

-   Add ability for a user to delete kits they've listed for sale.

-   Refactor.

Key Learnings

Learning how the serializers work in the backend was very useful. I had not done much styling in the last project, so this was an opportunity for me to stretch. I learned how to work with React Bootstrap and used many of those components like the Cards, Containers and Rows, and Buttons. Learning as I went did make coding take a bit longer, but I'm glad to have spent the time learning the framework.