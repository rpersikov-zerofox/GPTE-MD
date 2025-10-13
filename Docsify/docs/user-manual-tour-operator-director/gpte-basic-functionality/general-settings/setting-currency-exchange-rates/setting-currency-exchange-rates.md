# Setting Currency Exchange Rates

The system provides two modes of working with currency rates:

- Automatic update of the rates set by **European Central Bank**.
- Manual input of the required rates.

The required mode is set during the installation of the system.

## Viewing Currency Exchange Rates

To view currency rates,

1.  On the General Settings menu click Exchange rates.

![2024-11-09_23-06-11.png](/assets/2024-11-09_23-06-11.png)

In the Settings area, select the base currency to view currency rates against it:

![2024-11-09_23-07-54.jpg](/assets/2024-11-09_23-07-54.jpg)

Note: If the Bank that is connected to the system is not providing actual currency exchange rates as of the current date, you can either wait for the moment when the bank gives the actual information, or work with the old rates. If the information is outdated the special message will be displayed after you enter the system.

## Manual managing of exchange rates

In case a certain currency is absent in the needed currency exchange rates source for automatic setting, there is also a possibility of manual rates configuration:

![2024-12-23_13-39-26.jpg](/assets/2024-12-23_13-39-26.jpg)

## Exchange Rate Settings

**This functionality is currently available via administration panel.**

With GP Travel Enterprise you can set the currency exchange rates to use for settlements with suppliers and clients. It is of particular importance if between the date a document (an invoice, a credit note, etc.) was issued and payed for the exchange rate changes.

For example, an invoice for a client is issued on August, 1. It is due to pay August, 31. The system currency is EUR while the invoice is issued in USD. In the invoice, the exchange rate is indicated and is set 0,8485. During the period of 30 days, the EUR-USD exchange rate changes to 0,9190. The question arises which exchange rate is to be used.

To configure the exchange rate,

1.  On the General settings menu, click **Exchange rates settings**:
2.  The Exchange rates settings page appears:

![image-20200921-103913.png](/assets/image-20200921-103913.png)

3.  On the Exchange rates settings page, click the required button for every operation, specifically: 1. issuing invoices for cancellation fees; 2. calculating payment for invoices; 3. issuing credit notes; 4. canceling the service.
4.  Repeat the procedure both for settlements with suppliers and settlements with clients.
5.  Click Save.

Thus if we take the configurations displayed in the figure above (calculate payment for the invoice using current exchange rate), in the previously mentioned example, the invoice will be issued using current exchange rate of 0,9190 EUR for 1 USD.
