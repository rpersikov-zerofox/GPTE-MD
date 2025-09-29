# Importing Data to GP from an External System

In order to configure the loading data to GP from an external system, you need to use the export API.\
To configure export API:

1. Go to **“My Company” - “Settings”.**&#x20;

2\. Click **“Edit”** and choose checkbox **“Export data to external applications”.**  Configuration form appears.

3\. The following information must be specified in the configuration form:    &#x20;

1. **Name -** name of the system where you want to export data on orders from the GP system;
2. &#x20;**URL** - system URL where you want to export data on orders from the GP system;&#x20;
3. **Methods** - information to be imported. You can choose one or several options (e.g. "Invoices");
4. **Format** (JSON is set by default in the system);
5. **Protocol** - a method of transferring information (HTTP  is set by default in the system);

4\. Click **“Save”**.

**NOTE**

Using icon

![2024-10-28\_22-41-07.png](blob:https://gp-team.atlassian.net/729f738a-57df-446b-bdc5-892249ff6ea9) you can delete from the GP system all the specified information about an external system.\
\


Using icon&#x20;

![2024-10-28\_22-41-16.png](blob:https://gp-team.atlassian.net/c54af063-564b-478d-879e-0afe50451bbc) you can add several external systems for integration and create  its own configuration form for each external system.

5\. Next, let's look at the example of loading invoices:

After receiving a request **POST /issueInvoice** from our system you need to use our method **PUT/invoices** to send an URL of pdf file (invoice), invoice status (paid / unpaid) and the amount.

Example data model:

&#x20; "supplierId": 0,

&#x20; "clientId": 0,

&#x20; "invoiceId": 0,

&#x20; "paymentStatus": "",

&#x20; "externalInvoiceId": "",

&#x20; "invoicePrice": 0,

&#x20; "invoiceURL": ""

}

**!** **Required fields** are "supplierId", "invoiceId", "paymentStatus", "externalInvoiceId", "invoiceURL".

6\. After receiving the data, the invoice status in the GP system will be "Invoiced" in the "Invoices and payments" section. When you click on the "View invoices" link, a list of invoices will open.

**”Invoices” functionality is currently available via administration panel.**

**NOTE:**

When booking a service , after invoicing and until information is received from the external system of the invoice status in the GP system, there will be "Waiting".

Example of exporting an invoice:

[**POST/issueInvoice** ](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by GP system )**

{"invoice":{"orderId":7531,"invoiceId":1693,"serviceTableShort":{"lines":{"serviceId":1004769,"serviceName":"AnNur(Testing)","currency":"GBP","invoicePrice":349.59,"commission":"0.00","paymentType":"FULL"\}},"paymentStatus":"INVOICE\_WAITING","supplierId":1708077,"clientId":3903227,"dueDate":"2019-08-31T11:23:40.672+03:00","clientType":"DirectSales"\}}

[**PUT\_invoices** ](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by the external system)**

{

&#x20; "invoiceId": 1693,

&#x20; "paymentStatus": "BILL",

&#x20; "externalInvoiceId": "qwerty",

&#x20; "supplierId": 1708077,

&#x20; "invoiceURL": "gmail.com"

}

