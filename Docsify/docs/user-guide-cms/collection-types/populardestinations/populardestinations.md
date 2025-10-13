# PopularDestinations

To add a new Popular destination click on "Add New PopularDestination" and fill in the fields.

![2024-11-20_09-55-41.jpg](/assets/2024-11-20_09-55-41.jpg)

![image-20210805-191721.png](/assets/image-20210805-191721.png)

## LocationID and Country Code

To get location id (city id) and Country Code you need to follow nexts steps:

1.  Open Swagger in a new tab :
2.  Enter API key, companyCodeOrAlias, login, password. Then press "Try it out" button:
3.

![image-20210805-192844.jpg](/assets/image-20210805-192844.jpg)

![image-20210805-193207.png](/assets/image-20210805-193207.png)

Paste the token into the following field and click on "Explore":

![image-20210805-193403.png](/assets/image-20210805-193403.png)

4.  Choose Get/Locations method:

![image-20210805-193658.png](/assets/image-20210805-193658.png)

5.  Into the "limitCountries" field enter "-1" → press "Try it out" button:

![image-20210805-194151.png](/assets/image-20210805-194151.png)

6.  In the response body choose the country and copy "id". Also you can find here **Country Code**(iso2Code value):

![image-20210805-194530.png](/assets/image-20210805-194530.png)

7.  To proceed paste "id" into "paretntId" field" → Into the "limitCities" field enter "-1" → press "Try it out" button. Choose a city to be displayed as a Popular Destination and copy city "id".

## Country Code

See step 6. If it needed to display country flag near city name it is necessary to enter Country Code in non-capital letters:

![image-20210806-061652.png](/assets/image-20210806-061652.png)

![image-20210806-062803.jpg](/assets/image-20210806-062803.jpg)

## Image

To upload an image click "Add" → "Add more assets":

![image-20210806-062947.jpg](/assets/image-20210806-062947.jpg)

![image-20210806-063026.jpg](/assets/image-20210806-063026.jpg)

There is 2 ways to upload your image: from computer or from url:

![image-20210806-063219.png](/assets/image-20210806-063219.png)

When all the steps are done make sure that field"OnHomePage is switched ON:

![image-20210806-063405.png](/assets/image-20210806-063405.png)

You can create as many entries as you want.

Now the Popular destination will be displayed on your website:

![image-20210806-063558.jpg](/assets/image-20210806-063558.jpg)
