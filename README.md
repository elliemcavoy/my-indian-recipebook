<h1>My Indian Recipebook</h1>
<h4><a href="" target="_blank">GitHub Link</a></h4>
<h4><a href="" target="_blank">Deployed Project</a></h4>
<img src="">
<p>My Indian Recipebook is a web based application that can be used to share recipes for Indian cuisine. Users are able to add their own recipes, edit & delete them, read other user's recipes and add recipes to their favourites.</p> 
<h2>Table of Contents</h2>
<ol>
<li><a href="#ux">UX</a></li>
<ul>
<li><a href="#wireframes">Wireframes</a></li>
<li><a href="#target-audience">Target Audience</a></li>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#design">Design</a></li>
<ul>
<li><a href="defensive-design">Defensive Design</a></li>
<li><a href="typography">Typography</a></li>
</ul>
</ul>
<li><a href="#database">Database</a></li>
<li><a href="#features">Features</a></li>
<ul>
<li><a href="#existing-features">Existing Features</a></li>
<li><a href="#new-features">Features left to implement</a></li>
</ul>
<li><a href="#technologies">Technologies Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#credits">Credits</a></li>
</ol>
<h1 id="ux"><u>UX</u></h1>
This web based application's primary purpose is to allow the sharing of recipes. The recipes will be available to browse by any visitor to the website. However, additional functionality will be made available for user's that register on the site. A search functionality will provide any visitors the ability to search for recipes by a keyword such as an ingredient or name. Registering on the site will allow users to, once logged in, edit and delete their own recipes. It will also allow them to add other user's recipes to their favourite's list which will then be stored in their profile and be readily available for them to view. A leaderboard on the main page will also allow visitors to see the current most voted for recipes.<br>

<h2 id="wireframes">Wireframes</h2>
Please see the wireframes for this project:<br>
<a href="https://share.balsamiq.com/c/nyqLcnpov9SR5JqB1idUpW.png" target="_blank">Desktop</a><br>
<a href="https://share.balsamiq.com/c/smk12dS2m54dXyfPrxxRvk.png" target="_blank">Mobile</a><br>

<h2 id="target-audience">Target Audience</h2>
<ul>
<li>The audience that this application will be aimed at will be avid home cooks who have a particular interest in Indian Cuisine. </li>
</ul><br>

<h2 id="user-stories">User Stories</h2>
As a user of the website, the following actions and results would need to be achieved:
<ol>
<li>As a user, I want to be able to view all of the recipes and to be able to search for recipes containing a specific word.</li>
<li>As a user, I want to be able to see the top three rated recipes at any given time.</li>
<li>As a user, I want to be able to see the type of dish, ingredients, method and time to make the recipe.</li>
<li>As a user, I want to ability to create a profile by entering a username and password.</li>
<li>As a registered user, I want the ability to log in and log out of my account.</li>
<li>As a registered user, I want to be able add recipes so that other user can view them. </li>
<li>As a registered user, I want to be able to see all of my recipes via my Profile and have the ability to edit & delete them if required.</li>
<li>As a registered user, I want to be able to add other user's recipes to 'My Favourites' and have easy access to them through my Profile.</li>
<li>As a registered user, I want to be able to vote (upvote or downvote) on other user's recipes.</li>
<li>As the admin user, I want to be able to remove and edit any recipe regardless of which user added it to the application.</li></ol><br>

<h2 id="design"><u>Design</u></h2>
I have kept the design of the webpages simple and easy to navigate.
<ul><li>All of the headings are the same size, colour & font and the colour scheme is the same throughout.</li>
<li>Also all of the buttons have the same colour schemes and sizes.</li>
<li>By using the card class from materialize, whenever the recipes are shown, the stlying and spacing is the same.</li>
<li>Again with the collapsible class, all of the recipes will be displayed in the same format.</li>
<li>To ensure that all of the recipes show an image, I have added a generic image to be displayed if an image is not provided by the user. This will allow the design to be the same for each recipe that is added.</li>
<li>The colours used for this project are: rgba(255, 136, 0), rgba(116, 115, 115, 0.911), grey </li></ul>

<h2 id="defensive-design">Defensive Design</h2>
<p>Defensive design for this application was built into a lot of the functions as well as the templates. This means that only registered user can access certain parts of the application and edits can only be made by the relevant people.</p>
<ul>
<li>An IF statement on the base template means that unless a user is logged in, they only have access to the following pages: Home, Recipes, Log In & Register. They are able to view recipes but cannot vote or add them to favourites.</li>
<li>The registration form requires a unique username & password to be provided to ensure users cannot duplicate log in details. The password will be hashed before being entered into the users collection for added security.</li>
<li>The Log In will only be successful if the username & password match those provided in the users collection.</li>
<li>To ensure only the author of each recipe can edit or delete them, the buttons to do so only appear on their recipes once they are logged in and once they are on their 'My Profile' page. </li>
<li>To ensure that an admin user has complete control over the content, if they are logged in, they are able to delete and edit any recipe from the 'Recipes' page.</li>
</ul>

<h2 id="typography">Typography</h2>
<p>2 Google Fonts were used in this project:</p>
<ol>
<li>Delius Unicase - Logo</li>
<li>Arima Madurai - Main Body text & headings </li>
</ol><br>

<h1 id="database"><u>Database</u></h1>
For this project, there will be 4 collections in the MongoDB database that I have created called 'recipebook'. The tables below show the items in each of the collections.<br>

<h3><u>Users</u></h3>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Object Id (automatically generated to be unique)| ID |
|username| Username decided by user| Varchar/Integer (20) |
|password| Password chosen by user that has been hashed| Varchar/Integer (15) |

<br>
<h3><u>Recipes</u></h3>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Object Id (automatically generated to be unique)| ID |
|name| Recipe Name| Text |
|ingredients| Recipe ingredients| Text |
|method| Method to create dish| Text |
|time| Time to create recipe| Time |
|meal_type_name| Starter, Main, Side or Dessert| Text | 
|image| URL for image of finished dish| Text (URL) |
|created_by|username of the user who added recipe| Varchar/Integer (20) |

<br>
<h3><u>Meal_type</u></h3>
This collection is limited to 4 entries which are: Starter, Meain Course, Side Dish and Dessert. The collection cannot be added to or changed apart from manually through MongoDB.

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Object Id (automatically generated to be unique)| ID |
|meal_type_name| Type of dish| Text |

<br>
<h3><u>Vote</u></h3>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Object Id (automatically generated to be unique)| ID |
|vote| An array which is either upvote or downvote| Text |
|recipe_name|Name of dish that has been voted| Text |
|added_by|Username of user who is voting| Varchar/Integer (20) |

<br>
<h3><u>Favourites</u></h3>
<p>This collection was originally used however after improvements were made to the code it was no longer required so is no longer referenced in the app.py.</p>

| Key                | Value          | Data Type       |
|--------------------|----------------| ----------------|
|_id | Object Id (automatically generated to be unique)| Id |
|meal_type_name| Type of dish| Text|
|name|Recipe Name| Text |
|ingredients| Ingredients for selected recipe| Text |
|method| Method for selected recipe| Text |
|image| URL for image of dish| Text (url) |
|added_by| Username of user who added to favourites| Varchar/Integer (20) |

<br>
<h3>Database Design</h3>
Below is the design of how the collections will work together during the project.<br>
<img src="static/images/conceptual.JPG">
<h1 id="#features"><u>Features</u></h1>

<br>
<h2 id="existing-features"><u>Existing Features</u></h2>
<ol>
<li>NAVIGATION</li>
<li>VIEW RECIPES</li>
<li>SEARCH RECIPES</li>
<li>REGISTRATION</li>
<li>LOGIN</li>
<li>LOGOUT</li>
<li>ADD RECIPE</li>
<li>EDIT RECIPE</li>
<li>FAVOURITES</li>
<li>LEADERBOARD</li>
</ol>

<br>
<h2 id="new-features"><u>Features Left to Implement</u></h2>
<ol>
<li>I would ideally like to connect to a supermarket API which is could then link to the ingredients from each recipe to display the prices of these items and give users the option to purchase them from the recipecard page.</li>
<li>I think that it would also be beneficial to incorporate a relational database so that a user's favourites & recipes could be stored against that users account. It would also be helpful to allocate each dish with the number of upvotes & downvotes rather than pulling all of the dish names from the votes collection in MongoDB. This is because as the collection grows in size it will take longer to pull all the data required to generate the leaderboard values.</li>
<li>I would like to add additional functionality to the add & edit recipes form. I would like the user to be able to add the method and ingredients as a separate entry for each item. But I would like them still to be entered as one value in the MongoDB database. This would then allow me to parse the ingredients & method onto separate lines for each entry made by the user.</li>
<li>I would like to add additional security when deleting recipes such as an extra check to ensure the user wants to delete the item.</li>
</ol>


<h1 id="technologies"><u>Technologies Used</u></h1>

<h3>Languages Used</h3>
<ul>
<li>HTML5</li>
<li>CSS3 </li>
<li>JavaScript</li>
<li>Python3</li>
</ul>
<h3>Libraries Used</h3>
<ul>
<li>JQuery</li>
<li><a href="https://materializecss.com/">Materialize</a> - Used to provide page structure, Navbar design and form components. Also used to provide generic styling. </li>
<li><a href="https://fontawesome.com/">Font Awesome</a>  - Icons for forms and styling.</li>
<li><a href="https://fonts.google.com/">Google Fonts</a> - Used to create a look in keeping with the website aim and to create uniform styling throughout.</li>
</ul>
<h3>Python Frameworks & Libraries</h3>
<ul>
<li>Flask Framework</li>
<ul><li>PyMongo</li>
<li>Split</li>
<li>Paginate</li>
</ul>
<li>werkzeug.security</li>
<li>bson</li>
<li>Counter</li>
<li>Random</li>
</ul>
<h3>Database & Deployment</h3>
<ul>
<li>MongoDB</li>
<li>Git</li>
<li>GitHub</li>
<li>Heroku</li>
</ul>

</ul>

<h1 id="testing"><u>Testing</u></h1>
<h4>Validators</h4>
<ul>
<li>W3C HTML Validator</li>
All pages of HTML content have been checked by the HTML validator and have passed.
<li>W3C CSS Validator</li>
<img src="static/images/css-validator.JPG">
</ul>

<h4>Manual Testing</h4>
I have carried out a lot of manual testing on different aspects of this project. Please see detailed manual testing logs <a href="testing.md"> here </a>.
Please see below a brief overview of the testing carried out. Any issues found and fixes put in place are documented in the testing log.

| Page                  | Bug Detected   | Bug fixed Y/N |
|---------------------- |----------------| --------------|
| Main Page (user)    | ISSUE FOUND| Y
| Main Page (user logged in)  | No issues found| 
| Register Page (user)  | No issues found| 
| Log In Page (user)  | No issues found| 
| Recipe Page (user)  | ISSUE FOUND| Y
| Recipe Page (user logged in) | ISSUE FOUND    | Y
| Recipe Page (admin logged in) | ISSUE FOUND     | Y
| Individual Recipecard (user) | No issues found     | 
| Individual Recipecard (user logged in) | No issues found     | 
| User Profile | No issues found     | 
| Add New Recipe | No issues found    | 
| Update Recipe (user's own recipe) | No issues found     | 
| Update Recipe (admin user)| No issues found     | 
| Delete Recipe (user's own recipe) | No issues found     |
| Delete Recipe (admin user) | No issues found     | 
| Add to favourites | ISSUE FOUND     | Y
| View favourites recipecard | ISSUE FOUND  | N



<h1 id="deployment"><u>Deployment</u></h1>
This project has been deployed via Heroku and can be accessed here - .<br>

If you would like to deploy this project for yourself please see below the steps I followed to deploy and you can do the same:
<ol>
<li>
Create your new repository (I used GitHub) and then download or clone the following link: 
</li>
<li>You will also need to create a cluster in MongoDB and a new collection. </li>
<li>
This site is currently deployed on Heroku using the master branch on GitHub. You can deploy this project remotely using the following steps:
<h3>Deploying with Heroku</h3>
<ol>
<li>Firstly you need to create a requirements.txt file. This is used by Heroku to install all the required dependancies that are needed to run the application. To create the requirements.txt file you will need to enter the following into the terminal:

pip3 freeze --local > requirements.txt
You can view the requirements.txt file for this project here to ensure all of the requirements are present in your own file.</li>
<li>Secondly, Heroku requires a Procfile which tells it what type of application is being deployed and how it should run it. To add the Procfile you will need to enter the below into the terminal:

echo web: python run.py > Procfile

(Please make note that the 'P' in Procfile should be capitalized)


You can view the Procfile for my project here: Procfile</li>

<li>You will then need to sign up for a free Heroku account or, if you already have one, you will need to sign in. The link to create your account is: https://signup.heroku.com/ </li>

<li>Once signed in to your Heroku account, you will need to create a new app ensuring you select the region closest to your location.</li>

<li>You then need to choose your deployment method in the Deploy section. If you have created your repository using GitHub, you can connect to the specific repository by searching for the repo-name. If you cannot connect via GitHub, you can connect using Heroku Git (follow the instructions provided on Heroku).</li>

<li>Once connected, you can 'Enable Automatice Deploys' so if you make any further changes and commits, it will automatically update and deploy a new version of the application.</li>

<li>In Heroku click on the 'Settings' tab. In the Config Vars section, click on 'Reveal Config Vars' which is used to configure the environmental variables. You will need to set up your env.py file in order to complete this section. Setting up your env.py file can be done as follows:
<ul>
<li>Create a new file outside the folder structure called env.py.</li>
<li>You will need to type 'import os' at the top of this file.</li>
<li>Then the environment variables need adding as below:<br>
os.environ.setdefault("IP", "0.0.0.0")<br>
os.environ.setdefault("PORT", "5000")<br>
os.environ.setdefault("SECRET_KEY", "insert your secret key here")<br>
os.environ.setdefault("MONGO_URI", "insert your connection string here")<br>
os.environ.setdefault("MONGO_DBNAME", "insert you database name here")<br>
The SECRET_KET can be anything you choose.<br>
The MONGO_URI connection string can be found by doing the following in MongoDB:
<ul>
<li>Click on the 'Overview' tab</li>
<li>Click on the 'Connect' option</li>
<li>Select the 'Connect your application' option</li>
<li>Select 'Python' as the driver</li>
<li>You will then be provided with a connection string</li>
<li>Paste the connection string into MONGO_URI variable</li>
<li>Ensure you update the sections in capital letters with your own information e.g your password, your cluster name and your collection name: mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority".</li></ul></li>
</ul>
</li>
<li>Once your env.py file is created, go back to the Config Vars in Heroku and add the IP, PORT, SECRET_KEY, MONGO_URI & MONGO_DBNAME with the correct values as per your env.py file.</li>
<li>Finally, go back to the 'Deploy' tab on Heroku and in the Manual Deploy section chose the 'main' branch and click 'Deploy Branch'. Once the application has been built, you will receive a message stating 'Your app was successfully deployed' with a link to view the app.</li>
</ol>
</li>

</ol>
<h1 id="#credits">Credits</h1>

<h3>Design</h3>
<ul>
<li>Navbar & side Navbar taken from Materialize version 1.0.0. This includes the Jquery used to operate the sidenav as well. </li>
<li>Card class taken from Materialize which inlcudes a floating button.</li>
<li>Form components HTML & CSS classes taken from Materialize including the Jquery to operate.</li>
<li>Collapsible component taken from Materialize including the Jquery.</li>
<li>Pagination implemented using code from <a href="https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo">https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo</a>.</li>
<li>Google Fonts utilized for all font styles within the project.</li></ul>

<h3>Code</h3>
<ul>
<li><a href="https://docs.mongodb.com/">MongoDB Documentation</a> used to help implement the search function and the pull method used in removing an item from favourites.</li>
<li><a href="https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo">Stack Overflow - Implementation of Pagination</a> which was used to implement the pagination on the 'recipes' page.</li>
<li>Tutor Support assisted with adding the recipe ObjectId into the 'favourites' array and then retrieving the recipe using the ObjectId.</li>
<li>Code Institute Turtorials were used for reference when creating functions.</li>
<li>Task Manager Mini Project. Login, Register & Log Out functions taken from this project and just modified to fit in with my milestone project. Other functionality was based around Task Manager function such as the 'add recipe' and 'edit recipe' functions. </li>
<li><a href="https://www.geeksforgeeks.org/python-counter-objects-elements/">Geeks for Geeks - Python Counter</a> used to help implement the Counter functionality in the voting function.</li>


</ul>

<h3>Media</h3>
<ul>
<li>Font Awesome used for all icons and symbols.
</li>
<li>Generic Image for recipe found at <a href="https://media.istockphoto.com/vectors/fork-knife-icon-vector-id468611140?k=20&m=468611140&s=170667a&w=0&h=vv4BkhlRA35rC-CkIvRBf-r4X9kcFSEQGnzNiJOFH5s=">https://media.istockphoto.com/vectors/fork-knife-icon-vector-id468611140?k=20&m=468611140&s=170667a&w=0&h=vv4BkhlRA35rC-CkIvRBf-r4X9kcFSEQGnzNiJOFH5s=</a></li>
<li>Image to show responsive design from <a href="http://ami.responsivedesign.is/#">http://ami.responsivedesign.is/#</a></li></ul>







