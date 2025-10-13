# Invoices

Manage all customer and supplier invoices from a centralized location. View, search, download, and track payment status for both issued and received invoices.

## Overview

The Invoices module tracks:

- **Customer Invoices** - Bills issued to your clients for travel services
- **Supplier Invoices** - Bills received from travel service providers
- Invoice payment status and history
- Outstanding balances and overdue payments

## Access Invoices

Navigate to **Finance** > **Invoices**

## Invoice Categories

### Tour Operator Invoices

Invoices related to reservations created by travel agencies in your distribution network:

- **Invoices to Customers** - Bills you issue to your travel agency partners
- **Invoices from Suppliers** - Bills you receive from consolidators and contracted suppliers

### Agency Invoices

Invoices related to reservations created by your internal travel agency:

- **Invoices to Customers** - Bills issued to individual travelers buying through your agency
- **Invoices from Suppliers** - (Tab remains blank as your tour operator acts as the supplier)

![Invoice categories](/assets/Screen-Shot-2020-09-17-at-1.41.37-PM.jpg)

## View Invoices

Access invoices through two methods:

### From Reservation Page

1. Open a reservation
2. Look for **Invoice Issued** status
3. Click **Show Invoices** link

![Invoice from reservation](/assets/Screen-Shot-2020-09-17-at-1.42.49-PM.jpg)

The Invoice List displays all invoices for that reservation.

### From Finance Menu

1. Navigate to **Finance** > **Invoices**
2. Select the appropriate tab:
   - **Tour Operator Invoices** - For agency partner billing
   - **Travel Agency Invoices** - For direct customer billing

![Invoice list](/assets/Screen-Shot-2020-09-17-at-1.45.04-PM.jpg)

Invoices sort by transaction date. Click an invoice name to open the PDF document.

## Search for Invoices

Use the search form to find specific invoices:

![Invoice search](/assets/Screen-Shot-2020-09-17-at-2.42.08-PM.png)

**Search Criteria:**

- **Date** - Invoice issue date or date range
- **Pay Date** - Payment due date
- **Booking Number** - Associated reservation number
- **Customer** - Client name
- **Original Currency** - Invoice currency
- **Invoice Name** - Invoice identifier
- **Supplier** - Service provider name
- **Status** - Payment status (paid, invoiced, overdue, etc.)

Click **Search** to filter results.

## Invoice Status

**Status Indicators:**

- **Paid** - Payment confirmed and processed
- **Invoice Issued** - Invoice created but payment pending (full or partial)
- **No Invoice** - No invoice issued yet or changes require new invoice
- **Invoice Incomplete** - Missing invoices for some services in multi-service orders
- **Payment is Overdue** - Payment deadline passed, amount unpaid

**Tip:** Hover over the status icon to view detailed status information.

## Reconciliation Statements (Revise Acts)

Generate consolidated payment summaries for multiple unpaid invoices.

### When to Use

- Multiple invoices for one customer requiring single payment
- Currency conversion needed for foreign invoices
- Consolidated statement for accounting purposes

### Generate Reconciliation Statement

1. Navigate to **Finance** > **Invoices**
2. Select **Tour Operator Invoices** or **Agency Invoices** tab
3. Check the boxes for invoices to include

   ![Select invoices](/assets/Screen-Shot-2020-09-17-at-2.46.04-PM.jpg)

4. Click **Download the Revise Act**

5. In the Calculator window:

   ![Revise act calculator](/assets/Screen-Shot-2020-09-17-at-2.57.34-PM.png)

   - **Date** - Effective date for currency conversion
   - **Currency** - Target currency for statement
   - **Exchange Rate** - Currency conversion rate (auto-filled based on date)
   - **Format** - PDF or Excel

6. Click **Continue**

The reconciliation statement opens (PDF) or downloads (Excel).

![Revise act example](/assets/Screen-Shot-2020-09-17-at-3.21.22-PM.png)

**Note:** Reconciliation statements are generated on-demand and not saved in the system. Download for your records if needed.

## Best Practices

### Invoice Management

- **Review regularly** - Check invoice status weekly
- **Track overdue payments** - Follow up on unpaid invoices promptly
- **Verify accuracy** - Confirm invoice details match reservations
- **Maintain records** - Download important invoices for archival

### Payment Processing

- **Record payments promptly** - Update status when payments received
- **Use reconciliation statements** - Simplify multi-invoice payments
- **Monitor currency rates** - Review conversions for foreign currency invoices

## Related Topics

- [Invoice Payment](invoice-payment/invoice-payment.md) - Process and record payments
- [Ledgers](../ledgers/ledgers.md) - View accounting records
- [Statement of Account](../statement-of-account/statement-of-account.md) - Client and supplier financial summaries
- [Payment Settings](../payment-settings/payment-settings.md) - Configure invoice and payment options
