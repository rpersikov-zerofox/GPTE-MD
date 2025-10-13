# Resorts

**Instruction on adding new Resort:**

Open CMS → go to tab Resorts → Click "Add New Resort" and fill in the fields as follows:

![2024-11-20_09-33-04.jpg](/assets/2024-11-20_09-33-04.jpg)

![image-20210805-191721.png](/assets/image-20210805-191721.png)

**Link**- add resort name.

**DescriptionTitle** - add resort name which should be displayed on the Booking Engine.

**CityId**- How to get cityId? There two ways to get cityId:

*A. The easiest way is to get it from the search line when search is made (see example below)*

![image-20210805-192844.jpg](/assets/image-20210805-192844.jpg)

*B. To get a city id via API you need to follow next steps:*

1.  Open Swagger in a new tab :
2.  Enter API key, companyCodeOrAlias, login, password. Then press "Try it out" button.
3.

![image-20210805-193207.png](/assets/image-20210805-193207.png)

![image-20210805-193403.png](/assets/image-20210805-193403.png)

4.  Paste the token into the following field and click on "Explore":

![image-20210805-193658.png](/assets/image-20210805-193658.png)

5.  Go to **Locations - Choose Get/Locations** method:

![image-20210805-194151.png](/assets/image-20210805-194151.png)

6.  Into the "pattern" field enter city name. Into the "limitCountries" field enter "-1":

![image-20210806-061652.png](/assets/image-20210806-061652.png)

![image-20210806-062803.jpg](/assets/image-20210806-062803.jpg)

7.  Press "Try it out" button. In the response body you can find city id:

![image-20210806-062947.jpg](/assets/image-20210806-062947.jpg)

## Image

To upload an image click "Add" → "Add more assets":

![image-20210806-063026.jpg](/assets/image-20210806-063026.jpg)

There are 2 ways to upload your image: from a computer or from URL.

![image-20210806-063219.png](/assets/image-20210806-063219.png)

Add resort description:

![image-20210806-063405.png](/assets/image-20210806-063405.png)

Add SPA and Leisure description if you need:

![image-20210806-063558.jpg](/assets/image-20210806-063558.jpg)

![image-20210806-063945.png](/assets/image-20210806-063945.png)

To provide your clients with a more detailed description you can add more resort images and videos to the gallery.

![image-20210806-063956.png](/assets/image-20210806-063956.png)

**Video**

![image-20210806-064115.jpg](/assets/image-20210806-064115.jpg)

**Src** - it is necessary to add a link. For example if you need to add any video from Youtube it is necessary to follow next steps: Click share below chosen video → Choose "Embed" → Copy link as indicated in the screenshot:

![image-20210806-064512.jpg](/assets/image-20210806-064512.jpg)

![image-20210806-064608.jpg](/assets/image-20210806-064608.jpg)

**Thumb** - link to any photo that would be displayed as a preview

**Caption** - Video title, you can add as per your needs.

Click "**Save**" -\> "**Publish**".

When all the steps are done make sure that fields "DescriptionActive", "SpeciatizationActive", "SpaActive", "LeisureActive", "GalleryActive" are switched ON to be displayed on the website. If some of the fields are not needed switch them off.
