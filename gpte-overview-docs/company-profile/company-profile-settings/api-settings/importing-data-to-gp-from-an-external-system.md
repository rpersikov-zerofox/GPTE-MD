---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Importing Data to GP from an External System

In order to configure the loading data to GP from an external system, you need to use the export API.\
To configure export API:

1. Go to **My Company - Settings.**&#x20;
2. Click **Edit** and choose checkbox **Export data to external applications.**  Configuration form appears.
3. The following information must be specified in the configuration form:    &#x20;

* **Name -** name of the system where you want to export data on orders from the GP system
* &#x20;**URL** - system URL where you want to export data on orders from the GP system
* **Methods** - information to be imported. You can choose one or several options (e.g. "Invoices")
* **Format** (JSON is set by default in the system)
* **Protocol** - a method of transferring information (HTTP  is set by default in the system)

4. Click **“Save”**.

**NOTE**

Delete from the GP system all the specified information about an external system.

<div align="left"><figure><img src="../../../.gitbook/assets/ex1.png" alt="" width="27"><figcaption></figcaption></figure></div>

Add several external systems for integration and create  its own configuration form for each external system.

<div align="left"><figure><img src="../../../.gitbook/assets/add1.png" alt="" width="24"><figcaption></figcaption></figure></div>

Next, let's look at the example of loading invoices:

After receiving a request **POST /issueInvoice** from our system you need to use our method **PUT/invoices** to send an URL of pdf file (invoice), invoice status (paid / unpaid) and the amount.

Example data model:

```
{
  "supplierId": 0,
  "clientId": 0,
  "invoiceId": 0,
  "paymentStatus": "",
  "externalInvoiceId": "",
  "invoicePrice": 0,
  "invoiceURL": ""
}
```

{% hint style="warning" %}
**!** **Required fields** are "supplierId", "invoiceId", "paymentStatus", "externalInvoiceId", "invoiceURL".
{% endhint %}

6\. After receiving the data, the invoice status in the GP system will be "Invoiced" in the "Invoices and payments" section. When you click on the "View invoices" link, a list of invoices will open.

{% hint style="danger" %}
**Invoices functionality is currently available via administration panel.**
{% endhint %}

When booking a service , after invoicing and until information is received from the external system of the invoice status in the GP system, there will be "Waiting".

Example of exporting an invoice:

[**POST/issueInvoice** ](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by GP system )**

```
{"invoice":{"orderId":7531,"invoiceId":1693,"serviceTableShort":{"lines":{"serviceId":1004769,"serviceName":"AnNur(Testing)","currency":"GBP","invoicePrice":349.59,"commission":"0.00","paymentType":"FULL"}},"paymentStatus":"INVOICE_WAITING","supplierId":1708077,"clientId":3903227,"dueDate":"2019-08-31T11:23:40.672+03:00","clientType":"DirectSales"}}
```



[**PUT\_invoices** ](http://preliveapp.gp:8188/gptour-main/stat/swagger/index.html#!/Invoices/POST/issueInvoice)**(sent by the external system)**

```
{
  "invoiceId": 1693,
  "paymentStatus": "BILL",
  "externalInvoiceId": "qwerty",
  "supplierId": 1708077,
  "invoiceURL": "gmail.com"
}
```

