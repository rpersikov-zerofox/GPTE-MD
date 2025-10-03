# Setting Currency Exchange Rates

* [Viewing Currency Exchange Rates](https://gp-team.atlassian.net/wiki/spaces/GPTEUG/pages/1922255697/GPTE+Setting+Currency+Exchange+Rates#Viewing-Currency-Exchange-Rates)
* [Manual managing of exchange rates](https://gp-team.atlassian.net/wiki/spaces/GPTEUG/pages/1922255697/GPTE+Setting+Currency+Exchange+Rates#Manual-managing-of-exchange-rates)
* [Exchange Rate Settings](https://gp-team.atlassian.net/wiki/spaces/GPTEUG/pages/1922255697/GPTE+Setting+Currency+Exchange+Rates#Exchange-Rate-Settings)

The system provides two modes of working with currency rates:

* Automatic update of the rates set by **European Central Bank**.
* Manual input of the required rates.

The required mode is set during the installation of the system.

#### Viewing Currency Exchange Rates <a href="#viewing-currency-exchange-rates" id="viewing-currency-exchange-rates"></a>

To view currency rates,

1. On the General Settings menu click Exchange rates.

![2024-11-09\_23-06-11.png](blob:https://gp-team.atlassian.net/95c00922-749c-4273-a215-65cfee53732b#media-blob-url=true\&id=8944d0ee-13f8-47a9-9c26-d74aa54e19c9\&collection=contentId-1922255697\&contextId=1922255697\&width=150\&height=257\&alt=2024-11-09_23-06-11.png)

In the Settings area, select the base currency to view currency rates against it:

![2024-11-09\_23-07-54.png](blob:https://gp-team.atlassian.net/083bf299-43ac-48b7-a904-aed789006df4#media-blob-url=true\&id=2a46452b-0cdc-4a3c-b628-d5fc818a2cd7\&collection=contentId-1922255697\&contextId=1922255697\&mimeType=image%2Fpng\&name=2024-11-09_23-07-54.png\&size=93644\&width=789\&height=480\&alt=2024-11-09_23-07-54.png)

Note: If the Bank that is connected to the system is not providing actual currency exchange rates as of the current date, you can either wait for the moment when the bank gives the actual information, or work with the old rates. If the information is outdated the special message will be displayed after you enter the system.

#### Manual managing of exchange rates <a href="#manual-managing-of-exchange-rates" id="manual-managing-of-exchange-rates"></a>

In case a certain currency is absent in the needed currency exchange rates source for automatic setting, there is also a possibility of manual rates configuration:

![2024-12-23\_13-39-26.png](blob:https://gp-team.atlassian.net/a131d29c-3653-4c5f-a5e2-6c24a0a8c477#media-blob-url=true\&id=6067978f-592f-45b7-89d2-16bb50b1609a\&collection=contentId-1922255697\&contextId=1922255697\&mimeType=image%2Fpng\&name=2024-12-23_13-39-26.png\&size=78495\&width=995\&height=402\&alt=2024-12-23_13-39-26.png)

#### Exchange Rate Settings <a href="#exchange-rate-settings" id="exchange-rate-settings"></a>

**This functionality is currently available via administration panel.**

With GP Travel Enterprise you can set the currency exchange rates to use for settlements with suppliers and clients. It is of particular importance if between the date a document (an invoice, a credit note, etc.) was issued and payed for the exchange rate changes.

For example, an invoice for a client is issued on August, 1. It is due to pay August, 31. The system currency is EUR while the invoice is issued in USD. In the invoice, the exchange rate is indicated and is set 0,8485. During the period of 30 days, the EUR-USD exchange rate changes to 0,9190. The question arises which exchange rate is to be used.

To configure the exchange rate,

1. On the General settings menu, click **Exchange rates settings**:
2.  The Exchange rates settings page appears:

    ![](blob:https://gp-team.atlassian.net/62f40394-c4d2-4453-b4c0-0b91bd6a4066#media-blob-url=true\&id=8a6dd96f-8c8f-43fa-b830-10a11a842036\&collection=contentId-844923384\&contextId=1922255697\&mimeType=image%2Fpng\&name=image-20200921-104105.png\&size=69059\&width=757\&height=454\&alt=)
3. On the Exchange rates settings page, click the required button for every operation, specifically:
   1. issuing invoices for cancellation fees;
   2. calculating payment for invoices;
   3. issuing credit notes;
   4. canceling the service.
4. Repeat the procedure both for settlements with suppliers and settlements with clients.
5. Click Save.

Thus if we take the configurations displayed in the figure above (calculate payment for the invoice using current exchange rate), in the previously mentioned example, the invoice will be issued using current exchange rate of 0,9190 EUR for 1 USD.
