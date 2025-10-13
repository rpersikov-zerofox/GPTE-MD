# Ledgers

## General information

Finance information about transactions between your company customers and suppliers is stored in the finance module of the system. By using general ledgers you can view the trade liabilities, the debts of the customers as well as income and expenses, and thus keep track of the company financial flow.

To access ledgers, on the Finance menu, click Ledgers. In the system, there are four major types of ledgers:

- **Company general ledger:** reflects all financial information from the point of view of a tour operator and its internal tour agency, which are considered as one whole. The ledgers reflect all payments between a tour operator and its suppliers, internal tour agencies, and individuals buying the agency's services.
- **Travel agent's general ledger:** reflects all financial information from the point of view of a travel agency. The ledgers reflect all payments between a travel agency and its clients (tourists) on the one hand, and also between travel agencies and tour operators on the other hand.
- **Tour operator's general ledger:** reflects all financial information from the point of view of a tour operator. The ledgers reflect all payments between a tour operator and its suppliers, internal and external travel agencies.
- **Supplier's general ledger:** reflects all financial information from the point of view of a supplier. The ledgers reflect all payments between a supplier and a tour operator.

Note: The general ledgers contain information about system transactions only. Other external information such as salary, stationery expenses, etc. is not displayed here.

## Displaying general ledgers

Inside the general ledger, the information is displayed in the form of a tree. There are four main nodes on the top level:

![Screen Shot 2020-09-16 at 5.36.57 PM.png](/assets/Screen-Shot-2020-09-16-at-5.36.57-PM.png)

- **Income:** estimated amount of earnings (including amounts already paid for the reservations as well as prospective payments for unpaid reservations).
- **Expense:** your expenses on travel products from the internal suppliers and commission that you owe to the travel agencies.
- **Liability:** the amount that your company owes to the creditor at the moment.
- **Assets:** the amount due to your company (debts of your travel agencies, direct sales reservations unpaid by your tourists), including the current bank assets (earnings of the paid reservations).

Click (Expand icon) to see the detailed information in every section:

![Screen Shot 2020-09-16 at 5.42.27 PM.png](/assets/Screen-Shot-2020-09-16-at-5.42.27-PM.png)

Altogether, income and expenses determine the theoretical balance of your company. Liabilities and assets determine the real range of your financial assets.

Note 1: All sums reflected in financial ledgers are accumulated on a cumulative total from the very beginning of system use.

Note 2: If a reservation is canceled, the price of the canceled service is deducted from financial ledgers and it is not taken into account in further accounts.

## **Example**

Assume that according to the contract conditions, a tour operator adds a mark-up of 20% to a net-price, and the travel agency's commission is set to 10%. Let\'s see how the information change is reflected in the general ledger at different steps of selling services.

**Step 1** A tourist books a room in a hotel for 42,00 EUR via a travel agency. The information is registered in all four parts of the general ledger.

- **Income:** reflects the supplier's net-price and the mark-up added by you (42,00 EUR).
- **Expense:** the amount of 39,20 EUR reflected in this line includes the supplier\'s services price (the net-price of 35,00 EUR) and the agency commission (10% of 42,00 = 4,20 EUR).
- **Liabilities:** your liabilities consist of the amount that you have to pay to a supplier. That is why this line shows the hotel supplier\'s net-price, which is 35,00 EUR.
- **Assets:** in our example, the sum of 37,80 EUR represents the gross-price of the service after deduction of tour agency commission (42,00 - 4,20), that is the sum that a tour agency has to transfer you after selling the service.

**Income** The detailed information about earnings is shown below:

- **Sales:** the supplier's net-price and the mark-up added by you, that is the service price which is an offer to a final customer (42,00 EUR).
- **Client name:** the name of an agency to which the service is sold.
- **Service name:** the name of the sold service (accommodation).
- **Currency:** the net-price in the supplier's currency with the mark-up taken into account (if the system fixed currency differs from the currency of the supplier\'s prices).
- **FX Gains:** your foreign exchange gain in case of currency rate difference. For detailed information about the foreign exchange gain, see the Reflecting rate difference.

**Expense** Detailed information about expenses is shown below:

- **Purchases:** the total sum that you have to pay to a service supplier (the supplier's net-price is 35,00 EUR) and to an agency that sells the service (the tour agency\'s commission is 4,20 EUR).
- **Supplier Name:** the name of a supplier to which you have to transfer the payment and the amount you have to pay.
- **Service Name:** the name of the service to pay for (hotels)and the amount to be paid.
- **Currency:** the service net-price shown in the supplier's currency.
- **Travel Agency Name:** the name of a tour agency to which the current service is sold and the amount of the commission fee that you owe to the agency (4,20 EUR).
- **Service Name:** the name of the sold service and the amount of the agency commission fee.
- **Currency:** the tour agency commission fee shown in the supplier's currency.
- **FX Losses:** your exchange losses if they appear due to currency rate difference. For more information about currency rate difference, see the Reflecting rate difference.

**Liabilities** Detailed information about your liabilities is shown below:

- **Account Payable:** your effective debt to a service supplier (at net-price values) - 35,0 EUR.
- **Supplier Name:** the name of a supplier that receives payment for the booked service and the amount of payment (35,00 EUR).
- **Booked:** the total price of services (with the Booked status), purchased from the supplier (35,00 EUR).
- **Service Name:** The name of the booked service and the amount of your debt on it.
- **Currency:** the amount of debt in the supplier's currency.
- **Prepayments:** the amount of advance payment made by your tour agencies (if there are any).

**Assets** Detailed information about assets is shown below:

- **Prepaid Expenses:** the amount of advance payments made by your company.
- **Accounts Receivable:** effective debt of your tour agency calculated on the basis of the difference between gross-price and the agency commission. In this case the debt of the agency is 42,00 EUR -- 4,20 EUR = 37,80 EUR.
- **Travel Agency Name:** the name of a tour agency that should pay you for the booked service and the amount of the payment.
- **Booked:** accounts due from a tour agency for all services with the Booked status (In this case the Booked status means that the service is booked but the invoice is not yet issued to a client).
- **Service Name:** the name of the service paid for by the agency and the amount of the payment.
- **Currency:** accounts due to a tour agency that is shown in the service supplier's currency.
- **Current Assets:** your current assets, that is the amount on your bank account.

**Step 2** An agency receives the tour operator's invoice for the booked service and in turn, issues an invoice to a tourist. These operations are reflected in the tour operator\'s Assets sections. The amount of the tour agency\'s advance expenses for this service is moved from the Booked line to the Invoiced line.

**Step 3** The tourist pays the agency\'s invoice, and the agency in turn transfers money to the tour operator. Once the operation is performed, the agency\'s advance expenses decrease respectively. Additionally, the rest decreases respectively in the Invoiced line and the total price reflected in the Bank -\> Current Account the line is replenished.

**Step 4** The tour operator pays the supplier\'s invoice. As a result, the amount in Liabilities line decreases respectively to the amount paid (in this case, the amount decreases to zero, because only one service was booked earlier which is now fully paid: 35,00 EUR - 35,00 EUR = 0) and your net profit for the service remains in the Assets section (37,80 EUR -- 35,00 EUR = 2,80 EUR).

## **Reflecting rate difference**

The rate difference can occur when the currency of a tour product, which is sold to a tourist, differs from the system currency and when the dates of service booking and invoicing are different. In such a case, tour operators can have both exchange gains and exchange losses because of the cross-rate for these days.

Assume that an agent books an offer for 1 000 EUR on Monday, with the dollar's rate to the euro 0,95. Than 950 USD are transferred to the tour operator\'s bank account.

But as of the date of invoicing (on Tuesday) the rate changes and climb to 0,98 USD for 1 euro. That is why the amount of 30 USD should be additionally transferred to the tour operator\'s account (980 USD-950 USD).

In case the dollar\'s rate to euro changes decreases by the time of Invoicing and drops to 0,95 for 1 euro, then the loss of 30 USD is reflected on the tour operator\'s account (the Edit Rate section).

## **Flow of funds during invoicing and payments**

Information in the finance book is not static. During invoicing and payments the funds move to the respective subsections. After the final settlement, the accounts payable and the accounts receivable are set to zero. in such a case, the accumulated income can be viewed on the bank account.

## **Exporting general ledgers to Excel**

You can not only study the financial data but also export it to the Excel format. To export general ledgers to the Excel file:

1.  On the Finance menu, click Ledgers.
2.  Select a ledger. The Ledger window appears.
3.  Click the . All the ledger information is exported to Excel.
