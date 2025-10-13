# Transfer Scheduler

**General information**

**Module Scheduler**

The GP Travel Enterprise system has the **Scheduler** module that allows the 1st level tour operator (Director, Supervisor roles) working with their own products (Transfer or Excursion) to have the following capabilities:

- To plan the seating of tourists regarding the transport;
- To set up a guide service for the tourist group;
- To set up a driver service for the tourist group;
- To move applications from one group to another group with the same service type, the program type \"Shared\" and with the same program name;
- To separate one group of tourists into several groups;
- To search by filters (program type, program name, service, date, status, driver, guide);
- To edit groups through the drop-down lists within each group (making changes to the fields \"Guide\", \"Driver\", \"Status\";
- To mass edit;
- To show the lists of tourists;
- To show the service information, the reservation number and the reservation status in the "Tourists\" section;
- To export the document to Excel and download it with xlsx extension;
- To track changes in groups. The main \"Scheduler\" window consists of following parts: Search and Calendar.

![2024-11-11_14-09-40.jpg](/assets/2024-11-11_14-09-40.jpg)

**Search**

To search for the route fill in basic search options, which include:

- **Dates:**specify the dates.
- **Service status:** choose from the drop-down one go the 4 status, or this field can be empty
- **Service types**: Choose from the drop-down Transfer or Excursion, or this field can be empty;
- **Shared or individual:**Choose from the drop-down Individual or Shared, or this field can be empty;
- **Service name:**fill in the service name if it is known or this field can be empty;
- **Guide**: specify the guide's name;
- **Driver**: specify the driver's name;
- **Vehicle**: specify vehicle information.

To initiate search process,

- Select information from filters or fill in fields you need to search,
- Click **Filter**. Search results are arranged in the table:

![2024-11-11_14-16-20.jpg](/assets/2024-11-11_14-16-20.jpg)

**Calendar**

The Calendar tool helps to understand what dates there are reservations for transfer or excursions and what are their status. The reservation date is marked with a color indicator.

![2024-11-11_14-17-01.png](/assets/2024-11-11_14-17-01.png)

You can see the list of routes clicking on the date in the Calendar. Routes are ranked by the date parameter in descending order (starting from the nearest and further group).

**Viewing route details**

Each route consists of 2 sections: Information and Tourists.

The **information** tab shows:

- Editable **Guide** and **Driver** filters;
- Editable **Comments** field;
- Editable **Status** field;
- Editable **Vehicle Type** and **Vehicle** fields.

![2024-11-11_14-19-38.jpg](/assets/2024-11-11_14-19-38.jpg)

The **Tourists** tab shows the number of tourists that are included in the reservation. While the reservation is cancelled or rejected, the number of tourists changes. in the tourists tab there following parameters:

- First name and Last name, tourist type (age for children);
- Seat number;
- Reservation number (consists of the link to the reservation);
- From: Specify the departure address; it is mandatory got transfers to fill in the flight information;
- To: Specify the arrival address; it is mandatory got transfers to fill in the flight information;
- Contacts;
- Reservation status.

**Status**

Each route in the Scheduler has the status. There are 4 statuses:

- **New**: this group is automatically made and is not seen by the manager (the manager did not plan the driver or the guide, did not check tourists in the group list);
- **In progress**: the manager started managing this group;
- **Done**: the manager completed the group and planed the driver and the guide.
- **Cancelled**: all group reservations are cancelled, this group is cancelled.

![2024-11-11_14-23-46.jpg](/assets/2024-11-11_14-23-46.jpg)

## The main modifications in the group

Main modifications:

1.  Normal editing of parameters via drop-down lists;
2.  Mass editing of parameters.

### Editing parameters via drop-down lists

To edit parameters,

1.  Select the desired route and click **Details**;
2.  From the drop-down list of 3 sections (Status, Guide or Driver), select the desired parameter:

![2024-11-11_14-30-56.png](/assets/2024-11-11_14-30-56.png)

4.  Click icon.

**Mass editing of parameters**

**This functionality is currently available via administration panel.** Mass editing of groups is necessary to be able to quickly assign a guide or driver, or change the status of several groups at once.

For this:

In the table with the lists of groups, you need to select one or more groups using checkboxes:

![2024-11-11_14-33-28.png](/assets/2024-11-11_14-33-28.png)

2.  Click on Edit:

![2024-11-11_14-33-35.png](/assets/2024-11-11_14-33-35.png)

3.  After clicking, a pop-up window appears \"Changing the selected group\" (if one group is selected) or \"Changing the selected groups\" (if several groups are selected) with parameters that can be edited: Status, Guide, Driver:

![2024-11-11_14-42-49.png](/assets/2024-11-11_14-42-49.png)

4.  Select the desired parameter from the drop-down list;
5.  To save the entered data, click \"Save\". :info: When you click \"Close\", the changes are not saved.

**Transfer to another group** **Status New**

A group with the New status is formed automatically and the manager has not yet dealt with it (he did not plan a driver or guide, did not specify which of the tourists would be in this group).

**Status In progress**

This status is assigned manually by the manager when he starts the group planning process.

**Status Completed**

This status is assigned manually by the manager to groups with the status \"In progress\" if work with this group is completed.

**Status Canceled**

This status is assigned manually by the manager for groups with the status \"In progress\" or \"Completed\" if all applications that are in this group are rejected or canceled.

**Manual exclusion of an application with the status \"Rejected\", \"Canceled\" from the group**

**This functionality is currently available via administration panel.**

An employee of the company has the opportunity to manually exclude an application with the status \"Rejected\", \"Canceled\" from the group. At the same time, they are not transferred to any other group, but are simply excluded from the scheduler (because for canceled applications, in fact, it is not needed).

If you try to exclude an application with a status (one or more) other than \"Rejected\" or \"Canceled\", a pop-up window appears with a warning: \"Attention! Only applications with the status \"Rejected\" or \"Canceled\" can be excluded from the group.

To use this function:

- Select one or more applications using the check boxes in the list and then click \"Exclude from the group\" on the left under the list of applications;
- When you click on \"Exclude from group\", a pop-up window appears \"Exclusion of the selected application from the group\" (if one application is selected) or \"Exclusion of selected applications from the group\" (if several applications are selected).
- A message appears in this pop-up window: \"Do you really want to exclude the selected application from the group?\" (if one application is selected) or \"Do you really want to exclude the selected applications from the group?\" (if several applications are selected), and the employee needs to confirm the exclusion of the application/applications:

![2024-11-11_14-45-42.png](/assets/2024-11-11_14-45-42.png)

- If the answer is \"YES\", the application is excluded from the list and a window appears: \"Application successfully excluded from the group\" (if one application is selected) or \"Applications successfully excluded from the group\" (if several applications are selected);

![image-20200929-061342.png](/assets/image-20200929-061342.png)

- The application/applications are excluded from the list in the \"Scheduler\" group, but remain in the system in the list of applications in the \"Applications\" tab;
- If the answer is \"No\", the application/applications are not excluded from the group, no changes occur, the pop-up window closes.

**Merging groups**

**This functionality is currently available via administration panel.** This function is used to combine several groups with the same type of service, the type of program \"Group\", the same program and date into one group. To use this function, you need to select several groups with the same type of service, the type of program \"Group\", the same program and the date of the service using the check boxes in the table-list of groups and then click \"Merge\".

1.  A pop-up window \"Combining selected groups\" appears with options for selection;
2.  In the pop-up window, the selected groups and inactive fields are displayed in columns in the form of a drop-down list \"Driver\", \"Guide\", with already saved values for each of the groups;
3.  The maximum number of groups in the pop-up window is 5, then a horizontal scroll appears at the bottom of the window to view offers;
4.  It is possible to make changes for the selected group in the \"Driver\" and \"Guide\" fields through the drop-down list;
5.  To save the entered data, click \"Save\". At the same time, all applications from all merged groups are moved to the selected main group, and the remaining groups go to the \"Canceled\" status.

![image-20200929-061518.jpg](/assets/image-20200929-061518.jpg)

When you click \"Close\", the changes are not saved;

When you try to combine groups that do not match the parameters specified above, a pop-up window appears with a warning: \"Attention! You can combine groups with the same type of service, the type of program \"Group\", the same program and the date of the service\"

![image-20200929-061608.jpg](/assets/image-20200929-061608.jpg)

**Exporting a schedule to Excel** For the convenience of using information by groups, the schedule is exported to an Excel document with the xlsx extension.;

To use this function, you must,

1.  Click on the upload icon ;
2.  When you click \"Export\" icon, a document with the xlsx extension is downloaded.

The file contains:

- Group Id
- Date
- Time
- Status
- Service name
- Guests
- Type
- Guide
- Driver
- Vehicle

![image-20200929-061636.jpg](/assets/image-20200929-061636.jpg)

**Archive**

Inactive and already worked-out lists of groups with past dates, regardless of their status, are archived. They are ranked by the \"Date\" parameter according to the descending principle (starting from the nearest date and further). For example, the group with the date 06.08.2020 comes first, followed by the group with the date 01.07.2020, then 28.06.2020, and so on.
