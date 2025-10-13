# TopTours

To add a new Popular destination click on "Add New TopTour" and fill in the fields:

![2024-11-19_16-29-28.png](/assets/2024-11-19_16-29-28.png)

![2024-11-19_16-30-17.png](/assets/2024-11-19_16-30-17.png)

## PackageTourID

To get package tour id you need to follow next steps:

1.  Open Swagger in a new tab :
2.  Enter API key, companyCodeOrAlias, login, password. Then press the "Try it out" button.
3.

![image-20201026-162407.jpg](/assets/image-20201026-162407.jpg)

![image-20210805-191721.png](/assets/image-20210805-191721.png)

Paste the token into the field and click on "Explore":

![image-20210805-192844.jpg](/assets/image-20210805-192844.jpg)

1.  Select **PackageTours\>Get to receive the list of added Package Tours** (in this case, all active package tours that have been created in the Back office will be displayed). In the Response Body field, find the desired tour by name and copy value "id".

![image-20210805-193207.png](/assets/image-20210805-193207.png)

2.  Paste the value in the PackageTourId field in the CMS and click Save.

Now Package Tour is displayed in the Top Tour section on your website.

![image-20210805-193403.png](/assets/image-20210805-193403.png)
