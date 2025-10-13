# PopularHotels

To add a new PopuparHotels click on "Add New PopuparHotels" and fill in the fields

![2024-11-20_09-52-16.jpg](/assets/2024-11-20_09-52-16.jpg)

![image-20210805-192844.jpg](/assets/image-20210805-192844.jpg)

- **CityId = GP cityId - mandatory - (can be obtained from hotel search URL or API)**

*A. The easiest way is to get it from the search line when search is made (see example below)*

![image-20210805-193207.png](/assets/image-20210805-193207.png)

*B. To get a city id via API you need to follow next steps:*

1.  Open Swagger in a new tab
2.  Enter API key, companyCodeOrAlias, login, password. Then press "Try it out" button.
3.

![image-20210805-193403.png](/assets/image-20210805-193403.png)

![image-20210805-193658.png](/assets/image-20210805-193658.png)

4.  Paste the token into the following field and click on "Explore":

![image-20210805-194151.png](/assets/image-20210805-194151.png)

5.  Go to **Locations - Choose Get/Locations** method

![image-20210806-061652.png](/assets/image-20210806-061652.png)

6.  Into the "pattern" field enter city name. Into the "limitCountries" field enter "-1"

![image-20210806-063405.png](/assets/image-20210806-063405.png)

![image-20220329-153918.png](/assets/image-20220329-153918.png)

7.  Press "Try it out" button. In the response body you can find city id:

![image-20220329-154338.jpg](/assets/image-20220329-154338.jpg)

------------------------------------------------------------------------

- **HotelId = GP hotelId - mandatory (can be obtained from hotel search URL or API)**

*A. from hotel search URL: look for a HotelId (hotelCode) in search URL.*

*B. from API via Swagger:*

After getting **cityId**go to **Accommodations - GET /hotels** method. Into the "cityId" field enter cityId and press the "Try it out" button. In the response body you can find **hotelId:**

![image-20220329-162038.jpg](/assets/image-20220329-162038.jpg)

------------------------------------------------------------------------

- **Img - optional**- to add image for hotel to be displayed for a certain hotel. In case if image haven't been added in CMS, Image will be added from GP database.
- **Title - optional** - In case if Title haven't been added in CMS, the name of hotel will be added from GP database.
- **Order**- **mandatory** - For sorting please use this option

------------------------------------------------------------------------

When all the steps are done please SAVE and PUBLISH current popular hotel. You can create as many entries as you want. Now the Popular Hotels will be displayed on your website:

![image-20220329-162618.png](/assets/image-20220329-162618.png)

When any hotel is chosen on the booking engine you will redirected to the hotel description page with available rooms:

![image-20220329-162624.png](/assets/image-20220329-162624.png)
