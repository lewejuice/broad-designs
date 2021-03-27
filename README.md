<img src="media/readme-files/bd-mockup.png" alt="Desktop Demo" title="Desktop Demo" style="max-width:100%;">
<h1>Broad Designs</h1>
<h3>Fourth Milestone Project: Full Stack Frameworks with Django - Code Institute</h3>
<h4>By Lewis Hamilton</h4>
<hr>
<p>Welcome to <a href="https://broad-designs.herokuapp.com/" rel="nofollow" target="_blank">Broad Designs</a>!</p>
<p><a href="https://broad-designs.herokuapp.com/" rel="nofollow" target="_blank">Broad Designs</a> Is a graphic design/software development business built using Django.</p>
<br>
<p><a href="https://broad-designs.herokuapp.com/" rel="nofollow" target="_blank">Broad Designs</a> allows users to explore the portfolios of previous work, look through all the services provided, contact them via different channels (email or instant messenger), create a profile and start an order on their own project with email confirmations, order history and online payments.</p>
<br>
<p>This exciting application creates a simple, fuss free route for users to obtain professional designs and applications, with direct lines of communication like the <a href="https://www.tawk.to/" rel="nofollow" target="_blank">Tawk.to</a> instant messenger API for quick and simple responses to questions.</p>
<br>
<p>If you have any issues with the app, please head over to the <a href="https://broad-designs.herokuapp.com/" rel="nofollow" target="_blank">Broad Designs page and fill out a contact form or simply open the chat app and someone will get back to you as soon as possible.</a></p>
<br>
<h3>Demo</h3>
<p>A live demo can be found here <a href="https://broad-designs.herokuapp.com/" rel="nofollow" target="_blank">here</a>.</p>
<br>
<h3>Database Schema</h3>
<p><a href="https://en.wikipedia.org/wiki/PostgreSQL" rel="nofollow">PostgreSQL</a> was used to create the database for this application.</p>
<p>The final database schema consists of four collections which include users, services, portfolio and orders.</p>
<img src="media/readme-files/database.png" alt="Desktop Demo" title="Desktop Demo" style="max-width:100%;">
<br>
<h2><a id="user-content-table-of-contents" class="anchor" aria-hidden="true" href="#table-of-contents"></a>Table of Contents</h2>
<ol>
<li>
<p><a href="#ux"><strong>UX</strong></a></p>
<ul>
<li><a href="#user-stories"><strong>User Stories</strong></a></li>
<li><a href="#design-choices"><strong>Design choices</strong></a></li>
<li><a href="#wireframes"><strong>Wireframes</strong></a>
<ul>
<li><a href="#variation-between-wireframes-and-final-product">Variation Between Wireframes and Final Product</a></li>
</ul>
</li>
</ul>
</li>
<li>
<p><a href="#technologies-used"><strong>Technologies Used</strong></a></p>
<ul>
<li><a href="#front-technologies-used"><strong>Front End Technologies</strong></a></p></li>
<li><a href="#back-technologies-used"><strong>Back End Technologies</strong></a></p></li>
</ul>
</li>
<li>
<p><a href="#features"><strong>Features</strong></a></p>
<ul>
<li><a href="#existing-features"><strong>Existing Features</strong></a></li>
<li><a href="#features-to-be-implemented"><strong>Features To Be Implemented</strong></a></li>
</ul>
</li>
<li>
<p><a href="#testing"><strong>Testing</strong></a></p>
</li>
<li>
<p><a href="#deployment"><strong>Deployment</strong></a></p>
<ul>
<li><a href="#local-deployment"><strong>Local Deployment</strong></a></li>
<li><a href="#remote-deployment"><strong>Remote Deployment</strong></a></li>
</ul>
</li>
<li>
<p><a href="#credits"><strong>Credits</strong></a></p>
<ul>
<li><a href="#api"><strong>Images and Data</strong></a></li>
<li><a href="#logo"><strong>Fonts</strong></a></li>
<li><a href="#code-credits"><strong>Code Credits</strong></a></li>
<li><a href="#learning-resources"><strong>Learning Resources</strong></a></li>
<li><a href="#acknowledgements"><strong>Acknowledgements</strong></a></li>
</ul>
</li>
<li>
<p><a href="#disclaimer"><strong>Disclaimer</strong></a></p>
</li>
</ol>
<h2><a id="user-content-ux" class="anchor" aria-hidden="true" href="#ux"></a><strong>UX</strong></h2>
<p>This project is part of my <a href="https://codeinstitute.net/" rel="nofollow" target="_blank">Code Institute</a> Full Stack Software Development studies, specifically the Full Stack Frameworks module. The objective for this milestone project is to "Create a web application that allows users to discuss and order a specific graphic design or software development works to be carried out, where payment can be processed via the website, and email confirmatons and order history is provided to them".</p>
<br>
<h3><a id="user-content-user-stories" class="anchor" aria-hidden="true" href="#user-stories"></a>User stories</h3>
<p>"<strong><em>As a user, I would like to</em></strong> _______________"</p>
<p><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>successfully implemented</em></p>
<p><g-emoji class="g-emoji" alias="x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/274c.png">❌</g-emoji> <em>not yet implemented</em></p>
<ul>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>view the site</em> from <strong>any device</strong> <em>(mobile, tablet, desktop)</em>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>see</em> information on what services the site provides.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>have exclusive services for <strong>account holders</strong>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>create</em> my own <strong>profile</strong>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>update</em> my <strong>profile</strong> information.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>view</em> a portfolio of work that has been done in a <em>clear and simple way</em>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>process</em> my <strong>orders</strong> with <em>ease</em>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>submit</em> my own <strong>questions</strong> in a fast and reliable way.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>find</em> the location of the buisness and have their address if need be.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>forgot password functionality</em> for <strong>security</strong> and to stop being locked out of my account.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> be able to <strong>log out</strong>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> be able to <strong>change my password</strong>.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>see</em> an <strong>updated total</strong> as I add <em>services</em> to my order.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>recieve</em> <strong>email confirmations</strong> of my orders.</li>
<li><g-emoji class="g-emoji" alias="white_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2705.png">✅</g-emoji> <em>upload</em> <strong>a useful image</strong> with my order like a logo or design inspiration.</li>
<li><g-emoji class="g-emoji" alias="x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/274c.png">❌</g-emoji> <em>see</em> information on what's included with each <em>service</em>.</li>
</ul>
<h2><a id="user-content-design-choices" class="anchor" aria-hidden="true" href="#design-choices"></a>Design Choices</h2>
<h3><a id="user-content-colours" class="anchor" aria-hidden="true" href="#colours"></a>Framework</h3>
<ul>
<li><a href="https://getbootstrap.com/" rel="nofollow">Bootstrap v5.0.0</a>
<ul>
<li>Although this framework is only in beta, I found it had some new smart features that older version did not have while also maintaining bootstraps modern and clean layout with its simple-to-understand documentation.</li>
</ul>
</li>
<li><a href="https://code.jquery.com/jquery/" rel="nofollow">jQuery 3.5.1</a>
<ul>
<li>In an effort to keep the JavaScript minimal, I have decided to use jQuery in my my scripts framework.</li>
</ul>
</li>
<li><a href="https://www.djangoproject.com/download/" rel="nofollow">Django 3.1.5</a>
<ul>
<li>Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap.</li>
</ul>
</li>
</ul>
<h3><a id="user-content-colours" class="anchor" aria-hidden="true" href="#colours"></a>Colours</h3>
<ul>
<li>
<p><strong>Navbar</strong> - I decided to use bootstraps <code>#f8f9fa</code>(Light grey) as I feel this colour is clean and simple with a professional look.</p>
</li>
<li>
<p><strong>Buttons and Icons</strong> - I decided to use bootstraps #198754(green), #dc3545(red) and #0d6efd(blue) which represents add, confirmation or cancel. Also it stands out against the coloured and white backgrounds.</p>
</li>
<li>
<p><strong>Font Colour</strong> - The main colours I decided to use <code>#555</code>(Dark grey) &amp; <code>#FFFFFF</code>(White) for the text as it keeps with the simplistic theme, but also stands out against the background colours.</p>
</li>
</ul>
<h3><a id="user-content-fonts" class="anchor" aria-hidden="true" href="#fonts"></a>Fonts</h3>
<ul>
<li>
<p><a href="https://fonts.google.com/specimen/Poppins?preview.text_type=custom" rel="nofollow"><strong>Poppins</strong></a> - I used this font throughout the site, as I feel it fit in with the clean design, while also bold enough to stand out for readability.</p>
</li>
</ul>
<h3><a id="user-content-icons" class="anchor" aria-hidden="true" href="#fonts"></a>Icons</h3>
<ul>
<li>
<p><a href="https://fontawesome.com/" rel="nofollow"><strong>Font Awesome</strong></a> - Although there are other sites that provide icons, I prefer the look of the Font Awesome icons, and they have significantly more icons to use. They aren't displayed using text, but rather classes, so use on mobile devices isn't affected.</p>
</li>
</ul>
<h3><a id="user-content-wireframes" class="anchor" aria-hidden="true" href="#wireframes"></a>Wireframes</h3>
<ul>
<li>
<p>The wireframes for the initial layout in the planning stage of the website were created using <a href="https://balsamiq.com/" rel="nofollow">Balsamiq</a>. I chose to use Balsamiq for their simplicity and ease of use in a quick and effective manner. You can view the wireframes for Broad Design <a href="https://github.com/lewejuice/broad-designs/tree/master/media/wireframes">here</a>.</p>
</li>
<li>
<p>The wireframes include a design layout for Desktop and Mobile.</p>
</li>
<li>
<p>The colour scheme I had in mind when designing the mockups was not available on the site.</p>
</li>
</ul>
<h4><a id="user-content-variation-between-wireframes-and-final-product" class="anchor" aria-hidden="true" href="#variation-between-wireframes-and-final-product"></a>Variation Between Wireframes and Final Product</h4>
<p>I only made a couple changes from the initial design plan, as certain things I feel didn't work while building the site:</p>
<h5><a id="user-content-landing-page" class="anchor" aria-hidden="true" href="#landing-page"></a>Landing Page</h5>
<ul>
<li>For the homescreen I changed to show multiple catergories with movie posters to engage users instantly, instead of having them navigate to a categorie.</li>
</ul>
<h4><a id="user-content-level-select-modal" class="anchor" aria-hidden="true" href="#level-select-modal"></a>Modal</h4>
<ul>
<li>I did not include the design for my modal as I thought, instead of loading a new page, a modal window pop up is more efficient.</li>
</ul>
<h2><a id="user-content-technologies-used" class="anchor" aria-hidden="true" href="#technologies-used"></a>Technologies Used</h2>
<ol>
<li>
<p><a href="https://balsamiq.com/" rel="nofollow">Balsamiq</a> - Used to bring my wireframe sketches to life.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Adobe_Illustrator" rel="nofollow">Adobe Illustrator</a> - Used for building the website logo.</p>
</li>
<li>
<p><a href="https://github.com/">GitHub</a> - I used to store my repository for the project and record all my commits.</p>
</li>
<li>
<p><a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a> - Used as my primary IDE for developing projects.</p>
</li>
</ol>
<h3>Front End Technologies</h3>
<ol>
<li>
<p><a href="https://en.wikipedia.org/wiki/HTML" rel="nofollow">HTML</a> - This was used for the overall structure of the website.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" rel="nofollow">CSS</a> - This was used for the styling of elements on the website.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/JavaScript" rel="nofollow">JavaScript</a> - This was mainly used to retrieve and display data from the API, but also a couple small animations i.e displaying the modals.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/JQuery" rel="nofollow">jQuery</a> - This was used in my javascript files to help achieve complex ideas in a simpler way.</p>
</li>
<li>
<p><a href="https://getbootstrap.com/" rel="nofollow">Bootstrap5</a> - Used as the front-end framework for layout and design.</p>
</li>
<li>
<p><a href="https://dashboard.stripe.com/login" rel="nofollow">Stripe API</a> - Used to make secured payments on Orders.</p>
</li>
<li>
<p><a href="https://aws.amazon.com/" rel="nofollow">Amazon AWS S3</a> - Used to store staticfiles and media folders and files.</p>
</li>
<li>
<p><a href="https://developers.google.com/maps" rel="nofollow">Google Maps API</a> - Used to display the location of the buisness on the contact page.</p>
</li>
<li>
<p><a href="https://www.tawk.to/" rel="nofollow">Tawk.to API</a> - Used as an instant messenger for users to be able to ask questions and get quick responses.</p>
</li>
<li>
<p><a href="https://fonts.google.com/" rel="nofollow">Google Fonts</a> - I used Google Fonts to source the fonts I used on the website.</p>
</li>
</ol>
<h3>Back End Technologies</h3>
<ol>
<li>
<p><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" rel="nofollow">Python3</a> - Used as the back-end programming language.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Django_(web_framework)" rel="nofollow">Django 3.1.5</a> - Used as my Python web framework.</p>
</li>
<li>
<p><a href="https://www.postgresql.org/" rel="nofollow">PostgreSQL</a> - Used to store all the data in an organised database.</p>
</li>
<li>
<p><a href="https://dashboard.heroku.com/apps" rel="nofollow">Heroku</a> - Used for "Platform as a Service" (PaaS) for app hosting.</p>
</li>
</ol>
<p>Further details on all Python packages used on this project can be found in the <a href="https://github.com/lewejuice/broad-designs/blob/master/requirements.txt" rel="nofollow">requirements.txt file</a>. Each of these is outlined below (click below to expand the dropdown), with the package version and a brief description.</p>
<details open="">
<summary>CLICK HERE to expand the full <b>requirements.txt</b> details.</summary>
<table>
<thead>
<tr>
<th align="left">Package</th>
<th align="left">Version</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">asgiref</td>
<td align="left">3.3.1</td>
<td align="left">Standard for Python asynchronous web apps and servers to communicate with each other</td>
</tr>
<tr>
<td align="left">boto3</td>
<td align="left">1.17.30</td>
<td align="left">The AWS SDK for Python</td>
</tr>
<tr>
<td align="left">botocore</td>
<td align="left">1.20.30</td>
<td align="left">Foundation for AWS-CLI command line utilities</td>
</tr>
<tr>
<td align="left">crispy-bootstrap5</td>
<td align="left">0.2</td>
<td align="left">To run crispy-forms with bootstrap5</td>
</tr>
<tr>
<td align="left">dj-database-url</td>
<td align="left">0.5.0</td>
<td align="left">A utility to help you load your database into your dictionary from the DATABASE_URL environment variable</td>
</tr>
<tr>
<td align="left">Django</td>
<td align="left">3.1.5</td>
<td align="left">the Django framework</td>
</tr>
<tr>
<td align="left">django-allauth</td>
<td align="left">0.44.0</td>
<td align="left">Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.</td>
</tr>
<tr>
<td align="left">django-countries</td>
<td align="left">7.0</td>
<td align="left">A Django application that provides country choices for use with forms</td>
</tr>
<tr>
<td align="left">django-crispy-forms</td>
<td align="left">1.11.0</td>
<td align="left">An application that helps to manage Django forms</td>
</tr>
<tr>
<td align="left">django-forms-bootstrap</td>
<td align="left">3.1.0</td>
<td align="left">An application that enables you to use bootstrap classes in Django forms</td>
</tr>
<tr>
<td align="left">django-storages</td>
<td align="left">1.11.1</td>
<td align="left">Connects Django to S3 Buckets</td>
</tr>
<tr>
<td align="left">gunicorn</td>
<td align="left">20.0.4</td>
<td align="left">A Python WSGI HTTP Server for UNIX</td>
</tr>
<tr>
<td align="left">jmespath</td>
<td align="left">0.10.0</td>
<td align="left">Allows you to declaratively specify how to extract elements from a JSON document</td>
</tr>
<tr>
<td align="left">oauthlib</td>
<td align="left">3.1.0</td>
<td align="left">A framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework</td>
</tr>
<tr>
<td align="left">Pillow</td>
<td align="left">8.1.0</td>
<td align="left">Adds support for opening, manipulating, and saving many different image file formats</td>
</tr>
<tr>
<td align="left">psycopg2-binary</td>
<td align="left">2.8.6</td>
<td align="left">Python-PostgreSQL Database Adapter</td>
</tr>
<tr>
<td align="left">PyJWT</td>
<td align="left">2.0.1</td>
<td align="left">Python library which allows you to encode and decode JSON Web Tokens</td>
</tr>
<tr>
<td align="left">python3-openid</td>
<td align="left">3.2.0</td>
<td align="left">The reference library for OpenID in Python</td>
</tr>
<tr>
<td align="left">pytz</td>
<td align="left">2020.5</td>
<td align="left">This library allows accurate and cross platform timezone calculations</td>
</tr>
<tr>
<td align="left">requests-oauthlib</td>
<td align="left">1.3.0</td>
<td align="left">Makes requests simpler and more human-friendly</td>
</tr>
<tr>
<td align="left">s3transfer</td>
<td align="left">0.3.4</td>
<td align="left">Python library for managing Amazon S3 transfers</td>
</tr>
<tr>
<td align="left">sqlparse</td>
<td align="left">0.4.1</td>
<td align="left">Non-validating SQL parser</td>
</tr>
<tr>
<td align="left">stripe</td>
<td align="left">2.55.2</td>
<td align="left">Python library for Stripe’s API</td>
</tr>
</tbody>
</table>
</details>
<h2><a id="user-content-features" class="anchor" aria-hidden="true" href="#features"></a>Features</h2>
<h3><a id="user-content-existing-features" class="anchor" aria-hidden="true" href="#existing-features"></a>Existing Features</h3>
<p>In accordance to the project brief, I have successfully implemented all of the required features, as well as a few additional features to improve user experience!</p>
<p><strong>Register Account</strong> <g-emoji class="g-emoji" alias="bust_in_silhouette" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f464.png">👤</g-emoji> <g-emoji class="g-emoji" alias="heavy_plus_sign" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2795.png">➕</g-emoji></p>
<ul>
<li>Anybody can register for free and create their own unique account. This is built using Allauth's authentication and authorization to validate profile data.</li>
</ul>
<p><strong>Change Password</strong> <g-emoji class="g-emoji" alias="closed_lock_with_key" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f510.png">🔐</g-emoji></p>
<ul>
<li>Users can update their passwords from their profile page. They will receive an email with instructions on how to reset the password.</li>
</ul>
<p><strong>Contact <g-emoji class="g-emoji" alias="speech_balloon" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ac.png">💬</g-emoji></strong></p>
<ul>
<li>Users can ask questions via a contact form, instant chat or details of address, contact number and email are provided.</li>
</ul>
<p><strong>View Portfolio</strong></p>
<ul>
<li>Users can see a portfolio of work organised in to catergories of design and code.</li>
</ul>
<p><strong>View Services</strong></p>
<ul>
<li>Users can see a list of services the company provides and an explaination.</li>
</ul>
<p><strong>Add and Remove Services to Order</strong></p>
<ul>
<li>Users can add and remove services from their order.</li>
</ul>
<p><strong>Updated Total</strong></p>
<ul>
<li>Users get an updated total as they add and remove services.</li>
</ul>
<p><strong>Upload Image</strong></p>
<ul>
<li>Users can upload an image with their order, like a logo or design inspiration.</li>
</ul>
<p><strong>Email Confirmations</strong></p>
<ul>
<li>Users recieve email confirmations including all the information of their order.</li>
</ul>
<p><strong>Order History</strong></p>
<ul>
<li>Users can look through their order history and click on certain orders to open that orders details page up.</li>
</ul>
<p><strong>Toasts</strong></p>
<ul>
<li>Users will get toast popups to show errors, successes etc. All toasts are displayed with the company logo and message along with it.</li>
</ul>
<p><strong>Admin Status</strong> <g-emoji class="g-emoji" alias="police_officer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f46e.png">👮</g-emoji></p>
<ul>
<li>As Admin (ie: superuser), there are quite a few additional features across the site that no other user has access to. The account tab on the navbar has additional management option so they can add, edit and delete services and projects. They can also see a table of all the orders made and click on each order to get their details.</li>
</ul>
<h3><a id="user-content-features-to-be-implemented" class="anchor" aria-hidden="true" href="#features-to-be-implemented"></a>Features To Be Implemented</h3>
<p><strong>Information buttons</strong></p>
<ul>
<li>On the forms, I would like to add information buttons where if a user clicks, it will give a helper as to what that field needs.</li>
</ul>
<p><strong>Delete Account</strong></p>
<ul>
<li>Users should be given the opportunity to delete their account entirely. Currently they can register and edit their data, but not remove it from the database.</li>
</ul>



<h2><a id="user-content-testing" class="anchor" aria-hidden="true" href="#testing"></a>Testing</h2>
<p>A thorough mix of automated and manual testing have gone into building this project. In addition to tests, I have validated all files against online validation sites, and checked compatibilities across various modern browsers and devices.</p>
<h3>Validators</h3>
<p><strong>HTML</strong></p>
<ul>
<li><a href="https://validator.w3.org" rel="nofollow">W3C HTML Validator</a>
<ul>
<li>All <strong>.html</strong> files checked.</li>
<li><strong>base.html</strong> file contained minor errors that have since been rectified (<em>Had a button element within an anchor element and type inside script tag for JS</em>). <a href="https://github.com/lewejuice/broad-designs/commit/master">Correction Commit: f1e7c6a301ede885654d9960234424e4716650ce</a></li>
<li><strong>Error</strong>: Had a button element within an anchor element.</li>
<li><strong>Error</strong>: Type inside script tag for JS.</li>
<li>The remaining validation issues are all attributed to comments made with hyphens to organise sections of code:
<ul>
<li><strong>Warning</strong>: The document is not mappable to XML 1.0 due to two consecutive hyphens in a comment.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>CSS</strong></p>
<ul>
<li><a href="https://validator.w3.org" rel="nofollow">W3C CSS Validator</a>
<ul>
<li>The W3C Jigsaw validator does not yet recognize some bootstrap5 styling, and therefore passes 6 Parse Errors, 5 Unknown pseudo-element or pseudo-class and 5 Property doesn't exist. The sixteen Errors I've received  consisted of:
<ul>
<li><code>abbr[data-bs-original-title], abbr[title]</code></li>
<li><code>.row</code></li>
<li><code>	.table > :not(caption) > * > *</code></li>
<li><code>.form-control::-webkit-file-upload-button</code></li>
<li><code>.accordion-button</code></li>
</ul>
</li>
<li>I also received 406 Warnings all from these bootstrap5 styling :
<ul>
<li><code>.custom-checkbox</code></li>
<li><code>.custom-control-input:checked</code></li>
<li><code>.custom-control-label::before</code></li>
<li><code>Same color for background-color and border-color</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>JavaScript</strong></p>
<li><a href="https://jshint.com/" rel="nofollow">JShint</a>
<ul>
<li><strong>stripe_elements.js</strong> <a href="https://github.com/lewejuice/broad-designs/blob/master/order/static/order/js/stripe_elements.js">file</a>:
<ul>
<li>METRICS:
<ul>
<li>There are <strong>5</strong> functions in this file. Function with the largest signature take <strong>1</strong> arguments, while the median is <strong>1</strong>. Largest function has <strong>14</strong> statements in it, while the median is <strong>5</strong>. The most complex function has a cyclomatic complexity value of <strong>3</strong> while the median is <strong>1</strong>..</li>
</ul>
</li>
<li>UNDEFINED VARIABLES:
<ul>
<li><code>Stripe</code> (used for Stripe API)</li>
<li><code>$</code> (used for jQuery)</li>
</ul>
</li>
</ul>
</li>
<li><strong>base.html scripts</strong> <a href="https://github.com/lewejuice/broad-designs/blob/master/templates/base.html">file</a>:
<ul>
<li>METRICS:
<ul>
<li>There are 6 functions in this file. Function with the largest signature take 1 arguments, while the median is 0. Largest function has 6 statements in it, while the median is 1.5. The most complex function has a cyclomatic complexity value of 1 while the median is 1.</li>
</ul>
</li>
<li>UNDEFINED VARIABLES:
<ul>
<li><code>$</code> (used for jQuery)</li>
<li><code>bootstrap</code> (used for bootstrap5)</li>
</ul>
</li>
</ul>
</li>
<li><strong>google_maps.js</strong> <a href="https://github.com/lewejuice/broad-designs/blob/master/contact/static/contact/js/google_maps.js">file</a>:
<ul>
<li>METRICS:
<ul>
<li>There is only one function in this file. It takes no arguments. This function contains 4 statements. Cyclomatic complexity number for this function is 1.</li>
</ul>
</li>
<li>UNDEFINED VARIABLES:
<ul>
<li><code>$</code> (used for jQuery)</li>
<li><code>google</code> (used for Google maps API)</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><a href="http://beautifytools.com/javascript-validator.php" rel="nofollow">Beautify Tools</a>
<ul>
<li><strong>stripe_elements.js</strong> <a href="/TravelTimN/ci-milestone05-fsfw/blob/main/project/static/js/stripe.js">file</a>:
<ul>
<li><em><code>Stripe</code> is not defined.</em></li>
</ul>
</li>
<li><strong>base.html scripts</strong> <a href="/TravelTimN/ci-milestone05-fsfw/blob/main/project/static/js/scripts.js">file</a>:
<ul>
<li><code>$</code> is not defined.</li>
<li><code>bootstrap</code> is not defined.</li>
<li><em><code>Tawk_LoadStart</code> is defined but never used..</em></li>
<li><em><code>toastList</code> is defined but never used..</em></li>
<li><em><code>hideToast</code> is defined but never used..</em></li>
</ul>
</li>
<li><strong>google_maps.js</strong> <a href="/TravelTimN/ci-milestone05-fsfw/blob/main/project/static/js/scripts.js">file</a>:
<ul>
<li><em><code>google</code> is not defined.</em></li>
<li><code>$</code> is not defined.</li>
<li><em><code>beachMarker</code> is defined but never used.</em></li>
<li><em><code>mapsApiKey</code> is defined but never used.</em></li>
<li><em><code>initMap</code> is defined but never used..</em></li>
</ul>
</li>
</ul>
</li>
<p><strong>Python</strong></p>
<ul>
<li><a href="http://pep8online.com/" rel="nofollow">PEP8 Online</a>
<ul>
<li>All <strong>71 .py</strong> files checked.</li>
<li>Entirely <strong>PEP8 compliant</strong> with one exception:
<ul>
<li><code>webhooks.py</code> <a href="https://github.com/lewejuice/broad-designs/blob/master/order/webhooks.py">file</a> (I have one line too long on line 43, as I cant find a way to indent it.)</li>
<li><em>line too long (&gt;79 characters)</em> -  <code>'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,</code> x4</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3>Compatibility</h3>
<p>To ensure a broad range of users can successfully use the site, I tested it across the 6 major browsers in both desktop and mobile configuration.</p>
<ul>
<li><strong>Chrome</strong> (<em>v.89.0.4389.90</em>)</li>
<li><strong>Edge</strong> (<em>v.89.0.774.63</em>)</li>
<li><strong>Firefox</strong> (<em>v.87.0</em>)</li>
<li><strong>Safari</strong> (<em>v.14.0.3</em>)</li>
<li><strong>Opera</strong> (<em>v.74.0.3911.232</em>)</li>
<li><strong>Internet Explorer</strong> (<em>v.11.0.11</em>)</li>
</ul>
<h3>Testing Matrix</h3>
<img src="media/readme-files/broad-design-testing-matrix.png" alt="Testing Matrix" title="Testing Matrix" style="max-width:100%;">
<h3>Chrome's DevTools Audit Report</h3>
<img src="media/readme-files/devtools-audit.png" alt="Audit Report" title="Audit Report" style="max-width:100%;">
<h3>Automated Testing</h3>
<p>With Django's built-in <code>unittest</code> library module and <code>TestCase</code> subclass, I built <strong>27</strong> different tests to encompass most of my python <em>views</em>, <em>forms</em>, and <em>models</em>. Using the <a href="https://coverage.readthedocs.io/en/v4.5.x/" rel="nofollow">coverage.py</a> test package, those 27 tests have provided an overall result of <strong>75% test coverage</strong>, which is within the approved minimum requirement for testing. All tests pass as '<em>OK</em>'! Most of the remaining Python that I didn't manually build tests for, are built-in Django boilerplates and core functionality. Below is a full table with the entire breakdown of the <strong>Coverage Report</strong> - click to expand the dropdown menu.</p>






<h2><a id="user-content-deployment" class="anchor" aria-hidden="true" href="#deployment"></a>Deployment</h2>
<p>I developed this project using <a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a>. Version control was done using git and hosting the repository was done through <a href="https://github.com/lewejuice/broad-designs">repository in GitHub</a>.</p>
<p>The live site was deployed via <a href="https://www.heroku.com/" rel="nofollow">Heroku</a>. The deployed site will update when pushed from to heroku via gitpod terminal. The Heroku app location can be found <a href="https://broad-designs.herokuapp.com/">here.</a></p>
<p><strong>PLEASE NOTE</strong>: during development, none of my <em>staticfiles</em> were pushed to GitHub, as taught in the Code Institute LMS videos. These were added to my <em><a href="https://github.com/lewejuice/broad-designs/blob/master/.gitignore">.gitignore</a></em> file, as Heroku cannot host these files. They are hosted on Amazon AWS in an S3-Bucket. These files were pushed to GitHub purely for project assessment purposes only at the end of development! My <em>static</em> files contains the following folders and files:</p>
<ul>
<li><strong>css/</strong>
<ul>
<li><em><a href="https://github.com/lewejuice/broad-designs/blob/master/static/css/base.css">base.css</a></em></li>
</ul>
</li>
<li><strong>media/</strong>
<ul>
<li>all images used for the project</li>
</ul>
</li>
<li><strong>js/</strong>
<ul>
<li><em><a href="https://github.com/lewejuice/broad-designs/blob/master/order/static/order/js/stripe_elements.js">stripe_elements.js</a></em></li>
<li><em><a href="https://github.com/lewejuice/broad-designs/blob/master/contact/static/contact/js/google_maps.js">google_maps.js</a></em></li>
</ul>
</li>
</ul>
<h3 id="user-content-local-deployment" class="anchor" aria-hidden="true" href="#local-deployment">Local Deployment</h3>
<p>It's highly recommended to work in a virtual environment, but not absolutely required.</p>
<p>In order to run this project locally on your own system, you will need the following installed (as a bare minimum):</p>
<ul>
<li><a href="https://www.python.org/downloads" rel="nofollow">Python3</a> to run the application.</li>
<li><a href="https://pip.pypa.io/en/stable/installing" rel="nofollow">PIP</a> to install all app requirements.</li>
<li><a href="https://www.atlassian.com/git/tutorials/install-git" rel="nofollow">GIT</a> for cloning and version control.</li>
<li><a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a> (or any suitable IDE) to develop your project.</li>
</ul>
<p>Next, there's a series of steps to take in order to proceed with local deployment:</p>
<ul>
<li>Clone this GitHub repository by either clicking the green "<em>Clone or download</em>" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
<ul>
<li><code>git clone https://github.com/lewejuice/broad-designs.git</code></li>
</ul>
</li>
<li>Navigate to the correct file location after unpacking the files.
<ul>
<li><code>cd &lt;path to folder&gt;</code></li>
</ul>
</li>
<li>In gitpod homescreen, click the settings icon and add enviroment variables to the list or use a .env file.
<ul>
<li><em>Note: the example .env file contains environmental variables for both local and remote deployment. (see below for remote deployment details)</em></li>
</ul>
</li>
<li>Install all requirements from the <a href="https://github.com/lewejuice/broad-designs/blob/master/requirements.txt">requirements.txt</a> file using this command:
<ul>
<li><code>pip3 -r requirements.txt</code></li>
</ul>
</li>
<li>In the IDE terminal, use the following command to launch the Django project:
<ul>
<li><code>python3 manage.py runserver</code></li>
</ul>
</li>
<li>The Django server should be running locally now on <strong><a href="http://127.0.0.1:8000" rel="nofollow">http://127.0.0.1:8000</a></strong> (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.</li>
<li>When you run the Django server for the first time, it should create a new <em>SQLite3</em> database file: <strong>db.sqlite3</strong></li>
<li>Next, you'll need to make migrations to create the database schema:
<ul>
<li><code>python3 manage.py makemigrations</code></li>
<li><code>python3 manage.py migrate</code></li>
</ul>
</li>
<li>In order to access the Django <em>Admin Panel</em>, you must generate a superuser:
<ul>
<li><code>python3 manage.py createsuperuser</code></li>
<li>(assign an admin username, email, and secure password)</li>
</ul>
</li>
</ul>
<p>Once the database migrations and superuser have been successfully completed, Django should migrate the existing migrations.py files from each app to configure the following relational schema:</p>
<img src="media/readme-files/database.png" alt="Desktop Demo" title="Desktop Demo" style="max-width:100%;">
<h3 id="user-content-remote-deployment" class="anchor" aria-hidden="true" href="#remote-deployment">Remote Deployment</h3>
<p>This site is currently deployed on Heroku using the main branch on GitHub. Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:</p>

<ul>
<li>Create a <strong>requirements.txt</strong> file so Heroku can install the required dependencies to run the app:
<ul>
<li><code>pip3 freeze --local &gt; requirements.txt</code></li>
<li>The <em>requirements.txt</em> file for this project can be found here: <a href="https://github.com/lewejuice/broad-designs/blob/master/requirements.txt">requirements.txt</a></li>
</ul>
</li>
<li>Create a <strong>Procfile</strong> to tell Heroku what type of application is being deployed using <em>gunicorn</em>, and how to run it:
<ul>
<li><code>echo web: gunicorn main.wsgi:application &gt; Procfile</code></li>
<li>The <em>Procfile</em> for this project can be found here: <a href="https://github.com/lewejuice/broad-designs/blob/master/Procfile">Procfile</a></li>
</ul>
</li>
<li>Sign up for a free Heroku account, create your project app, and click the <strong>Deploy</strong> tab, at which point you can <em>Connect GitHub</em> as the Deployment Method, and select <em>Enable Automatic Deployment</em>.</li>
<li>In the Heroku <strong>Resources</strong> tab, navigate to the <em>Add-Ons</em> section and search for <strong>Heroku Postgres</strong>. Make sure to select the free <em>Hobby</em> level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your <em>.env</em> file with your new <em>database-url</em> details.</li>
<li>In the Heroku <strong>Settings</strong> tab, click on the <em>Reveal Config Vars</em> button to configure environmental variables. You will need to copy all of the enviroment variables key value pairs from your gitpod settings, into the config variables, but please omit the <em>development=True</em> variable; this is only for local deployment.</li>
<li>Still within the <strong>Settings</strong> tab, find the <em>Buildpacks</em> section and add the following two buildpacks below. This is because the main project lives in a subdirectory. Note: the order these are added is important:
<ul>
<li><code>https://github.com/timanovsky/subdir-heroku-buildpack.git</code></li>
<li><code>heroku/python</code></li>
</ul>
</li>
<li>Your app should be successfully deployed to Heroku at this point, but you're not quite finished yet!</li>
<li>Update the <em>settings.py</em> file to connect the remote database using this Python package: <code>dj_database_url</code></li>
<li>Re-build the migrations and create a superuser to your new remote database using the instructions in the <em>local deployment</em> section above.</li>
<li>Sign up for a free <a href="https://aws.amazon.com/" rel="nofollow">Amazon AWS</a> account in order to host your <em>staticfiles</em> and <em>media</em> files. From the <strong>S3 buckets</strong> section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:</li>
</ul>
<p><strong>Permissions</strong> &gt; <strong>CORS configuration</strong>:</p>
<pre>
<code>
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
</code>
</pre>
<p><strong>Permissions</strong> &gt; <strong>Bucket Policy</strong>:</p>
<pre><code>
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
</code></pre>
<p><em>! IMPORTANT ! - on the <strong>Resource</strong> line above, be sure to replace <code>&lt;x&gt;</code> with your <strong>AWS bucket arn</strong> details, but retain the <code>/*</code> at the end.</em> It should look similar to this:
- <code>"Resource": "arn:aws:s3:::my-bucket-name/*"</code></p>
<ul>
<li>From here, you'll need to navigate to the <strong>IAM</strong> section of AWS.
<ul>
<li>Create a <em>New Group</em> and be sure to select your existing S3 Bucket details to attach.</li>
<li>Create a <em>New Policy</em> and a <em>New User</em> in the IAM section as well, then attach these to the Group you just built.</li>
</ul>
</li>
<li>In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
<ul>
<li><code>python manage.py collectstatic</code></li>
</ul>
</li>
<li>Sign up for a free <a href="https://stripe.com" rel="nofollow">Stripe</a> account. Navigate to the <strong>Developers</strong> section, and click on <strong>API Keys</strong>. You should have two confidential keys which need to be added to your gitpod settings variables, as well as your Heroku config vars. These keys are:
<ul>
<li><code>Publishable Key</code>: <strong>pk_test_key</strong></li>
<li><code>Secret Key</code>: <strong>sk_test_key</strong></li>
</ul>
</li>
</ul>
<p>Congratulations! Your project should be completely setup and ready for remote deployment! <g-emoji class="g-emoji" alias="tada" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f389.png">🎉</g-emoji></p>
<h2><a id="user-content-credits" class="anchor" aria-hidden="true" href="#credits"></a>Credits</h2>
<h3><a id="api" class="anchor" aria-hidden="true" href="#api"></a>Images & Data</h3>
<ol>
<li>
<p>The service images on the what we do page and homepage were taken from <a href="https://www.google.com/" rel="nofollow">Google Images</a>.</p>
</li>
</ol>
<h3><a id="logo" class="anchor" aria-hidden="true" href="#logo"></a>Fonts</h3>
<ol>
<li>
<p>The typeface used throughout was from <a href="https://fonts.google.com/" rel="nofollow">Google Fonts</a>, called Poppins.</p>
</li>
</ol>
<h3><a id="user-content-code-credits" class="anchor" aria-hidden="true" href="#code-credits"></a>Code Credits</h3>
<ol>
<li>
<p><a href="https://developers.google.com/maps" rel="nofollow">Google Maps API</a> provided some useful documentation to style the map.</p>
</li>
<li>
<p>An extremely useful tool I used was <a href="https://stackoverflow.com/" rel="nofollow">Stack Overflow</a>, for help with many syntax and functions.</p>
<ul>
<li>Help with <a href="https://stackoverflow.com/questions/65034754/what-are-the-configuration-in-settings-py-to-send-e-mail-using-django-from-busin" rel="nofollow">setting up email confirmations with Outlook.</a></li>
<li>Help with uploading <a href="https://stackoverflow.com/questions/22831576/django-raises-multivaluedictkeyerror-in-file-upload/22832271" rel="nofollow">images</a> in a form.</li>
<li>Help with <a href="https://stackoverflow.com/questions/18999660/background-image-not-showing-on-ipad-and-iphone" rel="nofollow">background images</a> on the home-page being visible on mobile screens.</li>
</ul>
</li>
<li>
<p>I used <a href="https://www.youtube.com/" rel="nofollow">Youtube</a>, here a useful youtube tutorial I followed for extra information.</p>
<ul>
<li>Help with <a href="https://www.youtube.com/results?search_query=bootstrap+5+toasts+with+django" rel="nofollow">Bootstrap5 toasts.</a></li>
</ul>
</li>
</ol>
<h3><a id="user-content-acknowledgements" class="anchor" aria-hidden="true" href="#acknowledgements"></a>Acknowledgements</h3>
<p>A special thanks to:</p>
<ul>
<li>My Code Institute Mentor, <a href="https://github.com/precious-ijege">Precious Ijege</a> for his guidance and critical analysis.</li>
</ul>
<h3><a id="user-content-learning-resources" class="anchor" aria-hidden="true" href="#learning-resources"></a>Learning Resources</h3>
<ul>
<li>
<p>I have learnt so much from this project from start to finish, honing my skills in the communication between the front and backend. I can really understand now why Django is such an important tool to use and how it can create complex applications in a fraction of the time. Here are some resources that helped me along the way:</p>
</li>
<li>
<p><a href="https://codeinstitute.net/" rel="nofollow">Code Institute</a>.</p>
</li>
<li>
<p><a href="https://stackoverflow.com/" rel="nofollow">Stack Overflow</a>.</p>
</li>
<li>
<p><a href="https://www.youtube.com/" rel="nofollow">Youtube</a>.</p>
</li>
</ul>
<h2><a id="user-content-disclaimer" class="anchor" aria-hidden="true" href="#disclaimer"></a>Disclaimer</h2>
<p>This site has been created entirely for <strong>educational purposes</strong> only and has not been intended for anything else.</p>
</article>