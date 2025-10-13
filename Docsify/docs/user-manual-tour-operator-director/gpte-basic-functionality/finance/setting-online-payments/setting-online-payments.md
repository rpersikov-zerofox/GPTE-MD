# Setting online payments

When you set direct sales for your website, your clients can pay for the booked service with one of the e-commerce payment systems. To view the systems please, follow the link [E-commerce payment systems](https://www.software.travel/platform/gp-travel-enterprise/gateways/), scroll down to **Ready-Made Integrations** and find **Payment Services.**

## Payment Settings Configuration in **ABC Bank**

1.  On the **Finance** menu, click **Online payments** and then click the **ABC Bank** tab.
2.  Fill in the following parameters:

(in percent of the total price of the reservation): the withheld by the e-commerce payment system over the price amount. The mark up is included in the invoice price and payed by a customer.

the sum a customer should pay - a total price or a sum equivalent to maximal or minimal cancellation fee.

the default currency for conversion of the price of the booked service. The currency used to display rates on the B2C website may not correspond to the operational currencies of the payment system. In this case you need to select a currency from the list of currencies supported by the payment system. The invoice price for the service will be shown in this currency.

notifications on the web-site that are be displayed to the tourists and inform them about the terms and conditions of payments.

parameters required for online payments processing. Every payment system specifies its own list of parameters independently.

The **ABC Bank** system has the following requirements:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**            **Description**                             **Required value**
  ------------------------ ------------------------------------------- ---------------------------------------------------------------------------------------------------------
  URL                      The general URL to send system queries

  ACCEPT_PAYMENT_URL       The general URL to send system queries

  QUERY_reservationS_URL   URL to check payment status in the system

  MERCHANT NUMBER          Customer identification number              Merchant ID which is sent to you after your user account in the bank payment system has been activated.

  MERCHANT PASSWORD        User password                               Should be entered independently and is specified during the registration in the payment system.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Payment Settings Configuration in PayPal

The PayPal payment settings are configured in the same way as for the **ABC Bank** system described earlier. The configuration parameters in this case look as follows:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                            **Required value**
  --------------- ------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  URL             The main URL for sending requests to the system

  CHECKOUT_URL    URL of the services supplier. Used for redirection when the payment is being carried out

  PAYMENTACTION   Identification number                                                                      You can select the following options: \* The Authorization mode indicates the prior consent of the customer to the payment. In this case the required amount is reserved on its card, but the payment itself is not carried out. Confirmation will be required to make the payment. \* The Sale mode indicates the final payment and the request to make the transaction. \'Authorization\' mode is set by default.

  USER            Username                                                                                   Specified by the user. The Username is assigned when you create an account in the payment system.

  PWD             Password                                                                                   Specified by the user. The Password is assigned when you create an account in the payment system.

  SIGNATURE       Card signature (digital signature)                                                         Specified by the user. The Signature is assigned when you create an account in the payment system.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note. You can use the following currencies for paying in the PayPal system: USD, EUR, GBP, AUD, BRL, CAD, CHF, CZK,DKK, HUF, JPY, NOK, PLN, SEK, SGD.
