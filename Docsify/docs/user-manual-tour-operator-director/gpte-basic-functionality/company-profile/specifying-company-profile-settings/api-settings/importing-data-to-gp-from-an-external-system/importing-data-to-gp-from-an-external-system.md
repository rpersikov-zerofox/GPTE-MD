# Importing Data to GP from an External System

In order to configure the loading data to GP from an external system, you need to use the export API. To configure export API:

1.  Go to\*\* "My Company" - "Settings". \*\*
2.  Click\*\* "Edit" **and choose checkbox** "Export data to external applications".  \*\*Configuration form appears.

![2024-10-28_22-34-41.jpg](/assets/2024-10-28_22-34-41.jpg)

![2024-10-28_22-36-40.jpg](/assets/2024-10-28_22-36-40.jpg)

3.  The following information must be specified in the configuration form:
4.  **Name -**name of the system where you want to export data on orders from the GP system;
5.  **URL** - system URL where you want to export data on orders from the GP system;
6.  **Methods** - information to be imported. You can choose one or several options (e.g. \"Invoices\");
7.  **Format** (JSON is set by default in the system);
8.  **Protocol** - a method of transferring information (HTTP  is set by default in the system);
9.  Click **"Save"**.

**NOTE**

Using icon

you can delete from the GP system all the specified information about an external system.

Using icon

you can add several external systems for integration and create  its own configuration form for each external system.

![2024-10-28_22-41-07.png](/assets/2024-10-28_22-41-07.png)

5.  Next, let\'s look at the example of loading invoices:

After receiving a request **POST /issueInvoice**from our system you need to use our method **PUT/invoices**to send an URL of pdf file (invoice), invoice status (paid / unpaid) and the amount.

Example data model:

\"supplierId\": 0,

\"clientId\": 0,

\"invoiceId\": 0,

\"paymentStatus\": \"\",

\"externalInvoiceId\": \"\",

\"invoicePrice\": 0,

\"invoiceURL\": \"\"

}

**!** **Required fields**are \"supplierId\", \"invoiceId\", \"paymentStatus\", \"externalInvoiceId\", \"invoiceURL\".

6.  After receiving the data, the invoice status in the GP system will be \"Invoiced\" in the \"Invoices and payments\" section. When you click on the \"View invoices\" link, a list of invoices will open.

**"Invoices" functionality is currently available via administration panel.**

![2024-10-28_22-41-16.png](/assets/2024-10-28_22-41-16.png)

**NOTE:**

When booking a service , after invoicing and until information is received from the external system of the invoice status in the GP system, there will be \"Waiting\".

Example of exporting an invoice:

[\*\*POST/issueInvoice \*\*](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by GP system )**

{\"invoice\":{\"orderId\":7531,\"invoiceId\":1693,\"serviceTableShort\":{\"lines\":{\"serviceId\":1004769,\"serviceName\":\"AnNur(Testing)\",\"currency\":\"GBP\",\"invoicePrice\":349.59,\"commission\":\"0.00\",\"paymentType\":\"FULL\"}},\"paymentStatus\":\"INVOICE_WAITING\",\"supplierId\":1708077,\"clientId\":3903227,\"dueDate\":\"2019-08-31T11:23:40.672+03:00\",\"clientType\":\"DirectSales\"}}

[\*\*PUT_invoices \*\*](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by the external system)**

{

\"invoiceId\": 1693,

\"paymentStatus\": \"BILL\",

\"externalInvoiceId\": \"qwerty\",

\"supplierId\": 1708077,

\"invoiceURL\": \"gmail.com\"

}
