# Markups and commissions settings

**This functionality is currently available via administration panel.**

If it needed to apply difficult and more flexible conditions of markups and commissions for different hotels and flights it is possible to use module **Markups and commissions settings**(switch on in ASP options)

## Markups and commissions settings for hotels

Sometimes markups and commissions can vary depending on hotel location, dates of stay at the hotel, check in hours, etc. Therefore a tour operator might need to implement flexible configuration of service fee and aget interest rate.

**To accomplish this you need to upload the following data into the system:**

1.  Fill all the necessary data info at Excel file (*the file template is provided by the support team at the stage of system implementation*) by setting up following categories: 1. Supplier code; 2. Hotel code; 3. Hotel name; 4. Starting date of the rule; 5. Rule expiration date; 6. Hotel location; 7. Date of stay; 8. Supplier commission; 9. Direct sales mark-up; 10. Agency commission; 11. Currencies; 12. and other categories that you can find in the Excel file template.

![2024-12-24_12-43-39.jpg](/assets/2024-12-24_12-43-39.jpg)

1.  On **Clients** tab click **Sales settings** and find **Markups and commission settings.**

![image-20201007-141836.png](/assets/image-20201007-141836.png)

2.  Click **Upload**.

![image-20201007-142032.jpg](/assets/image-20201007-142032.jpg)

3.  Click **Add** in the dialog box.
4.  Specify the path to Excel file with the data entered.The file should have the .xls or .xlsx extension.
5.  Click **Save**.

Now the data is uploaded into the system. To update data - repeat steps 1-7 with the new data added to the Excel file. After the new file is uploaded into the system the previous Excel file is saved to archive, so all the settings will be taken from the updated file.

Markups and commissions set in Markups and commissions settings for hotel file are applied only when using daily rates. To see more information about daily rates module, see [Daily rates](https://gp-team.atlassian.net/wiki/spaces/GPTE/pages/844890503/+Accommodation#Daily-rates-%2F-Price-list-for-surcharges).

## Markups and commissions settings for flights

For Markups and commissions settings for flights the way is the same as for the hotels. It is necessary to fill in excel file and download it into the module

**Instructions how to fill in the markups and commissions file for flights:**

1.  This file contains different rules for markup and commission calculation. Only if all conditions match to the current offer, the corresponding rule will apply.
2.  Empty or \"-\" cell value means that this condition is not checked. In this case this condition has lower weight as compared with the cell with concrete value.
3.  Commission is always calculated from basic fare (without taxes).
4.  Its possible to use slash (/) for OR logic and expression NOT () to exclude some values (for example, \"Everything except LON\" can be written as NOT (LON)\"
5.  In order to apply several conditions at once, use \"&\" (for example, \"all CIS countires except Russia can be written as \"CIS & NOT (Russia)\")
6.  It\'s also possible to specify ranges, like \"4001:4999\"
7.  For correct calculation it\'s important to keep current structure of file and order of columns. The lines can be added.

![image-20201007-142103.png](/assets/image-20201007-142103.png)

The sample you can find in the Excel file template.

## Apply commision on cancelled services

There can be different scenarios on applying Agent commission on cancelled services:

- current logic - when a service is cancelled, the Agent commission is totally removed;
- new logic - when a service is cancelled, the commission is recalculated from cancellation fees.

With a new version the configuration on this functionality has been added to the settings of groups of contracts and individual contracts with Agencies / Distributors.

![image-20220215-130556.png](/assets/image-20220215-130556.png)
