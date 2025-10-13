# Import data

**This functionality is currently available via administration panel.**

You can update your corporate clients\' data and import information about the employees into the system from XLS-files. To import the data from an XLS-file,

1.  On the Navigation menu point to **Clients**and click **Corporate clients**.
2.  Click the name of the client whose data you want to import.
3.  Go to the **Import data** tab.
4.  By default the list of documents is empty. To add a document, click **Upload**. The New Department window appears.

![image-20200922-174607.jpg](/assets/image-20200922-174607.jpg)

You can upload XSL-files that contain tabs with the name of the legal client or a group of companies.

Contact the technical support service for the template of the XSL-document.

5.  From the **Document type** drop-down, select the type of data you want to import:

- CustomFields_reservation - custom fields for the reservations;
- CustomFields_Person - custom fields for the users;
- PersonalData - personal information on the users.

6.  If you select the **Deactivate not found values** check box, the system verifies the user data that is not updated during the import. If such an employee is found in the system, the record about this user is marked as inactive, while the **Dismissed \[Date\]** text is added into the log-file.
7.  In the **Upload** file form, click **Add**, browse to the document you want to upload and click **Upload**.
8.  Click **Save**. The data from the file is imported to the system. The XSL-file appears in the list of documents.

After importing you can download the log-file that contains a list of the updated fields or rejected records with reasons of the rejection.

Only tour operators\' users with the Director role and the corporate users with the Travel manager role can import the data.
