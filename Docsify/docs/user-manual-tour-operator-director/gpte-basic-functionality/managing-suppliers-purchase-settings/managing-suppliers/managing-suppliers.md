# Managing Suppliers

Configure supplier connections to access travel inventory and create self-operated products. Proper supplier setup is essential for searching and booking products through GP Travel Enterprise.

## Overview

Suppliers provide the travel products and services you sell to customers. GP Travel Enterprise supports two types of supplier connections:

1. **External Suppliers** - Third-party providers connected via XML API
2. **Direct Contract Suppliers** - Suppliers you manage directly for self-operated products

**Important:** You must configure at least one supplier before you can search for or book travel products.

## Supplier Types

### External Suppliers (API Connections)

Connect to travel suppliers through XML API integrations:

**Supported Supplier Categories:**
- Hotels and accommodation providers
- Airlines and flight consolidators
- Ground transportation companies
- Tour operators
- Activity and excursion providers
- Car rental companies
- Travel insurance providers

**Features:**
- Real-time availability and pricing
- Instant booking confirmation
- Automated inventory updates
- Direct supplier communication

**Setup Requirements:**
- Supplier API credentials
- Technical integration configuration
- Contract terms and pricing agreements

### Direct Contract Suppliers

Manually managed suppliers for self-operated products or direct contracts:

**Use Cases:**
- Products you own and operate
- Suppliers without online connectivity
- Direct hotel contracts
- Local service providers
- Custom or specialized products

**Features:**
- Manual product creation and management
- Custom pricing control
- Inventory management
- Flexible contract terms

## Supplier Configuration Workflow

### Adding External Suppliers

1. **Obtain API Credentials** - Get access credentials from the supplier
2. **Configure Connection** - Enter API settings in the system
3. **Test Connection** - Verify the integration works correctly
4. **Set Commercial Terms** - Configure markup, commission, and pricing rules
5. **Activate Supplier** - Enable the supplier for searches and bookings

### Adding Direct Contract Suppliers

1. **Create Supplier Profile** - Enter supplier business details
2. **Define Contract Terms** - Set payment terms and conditions
3. **Configure Pricing** - Establish markup and commission structures
4. **Create Products** - Build product catalog (see [Creating Self-Operated Products](../../creating-self-operated-products/creating-self-operated-products.md))
5. **Set Availability** - Configure product inventory and allotments

## Supplier Management

### Key Supplier Information

For each supplier, manage:

- **Business Details** - Name, address, contact information
- **Financial Information** - Payment terms, currency, banking details
- **Commercial Terms** - Markups, commissions, discounts
- **Technical Settings** - API configuration, connection parameters
- **Product Catalog** - Available products and services
- **Contract Documents** - Agreements, rate sheets, terms and conditions

### Supplier Operations

Common supplier management tasks:

- Update supplier contact and business information
- Modify commercial terms and pricing
- Add or remove products
- Review booking performance
- Process supplier invoices
- Generate supplier reports
- Deactivate or suspend suppliers

## Purchase Settings

Configure how you purchase from suppliers:

### Pricing Control

- Default markup percentages
- Product-specific markups
- Seasonal pricing adjustments
- Commission structures

### Payment Terms

- Credit terms and payment schedules
- Currency preferences
- Banking and payment methods
- Deposit requirements

### Booking Rules

- Booking confirmation workflows
- Cancellation policies
- Modification terms
- Penalty structures

## Supplier Relationships

### Performance Monitoring

Track supplier effectiveness:

- Booking volume and revenue
- Confirmation speed and reliability
- Product availability rates
- Customer satisfaction scores
- Error rates and issues

### Communication

Manage supplier interactions:

- Booking confirmations
- Modification requests
- Issue resolution
- Contract negotiations
- Performance reviews

## Integration Requirements

### For External Suppliers

Technical requirements for API integrations:

- Supported API protocols (XML, REST, SOAP)
- Authentication methods
- Data mapping and field requirements
- Testing and certification process

Contact technical support for assistance with API integrations.

### For Direct Contract Suppliers

No technical integration required. You manually create and manage products through the platform interface.

## Best Practices

### Supplier Selection

Choose reliable suppliers based on:

1. **Product Quality** - Services meet your standards
2. **Pricing Competitiveness** - Rates support your margins
3. **Technology Capability** - API reliability for external suppliers
4. **Service Level** - Responsiveness and support quality
5. **Financial Stability** - Payment reliability and credit terms

### Ongoing Management

Maintain healthy supplier relationships:

- Review performance regularly
- Update contracts and terms as needed
- Maintain accurate product information
- Process payments promptly
- Communicate issues quickly
- Negotiate favorable terms periodically

## Troubleshooting

### Common Supplier Issues

**Products Not Appearing in Search:**
- Verify supplier is activated
- Check product availability settings
- Confirm pricing is configured
- Review API connection status (external suppliers)

**Booking Failures:**
- Test API connectivity
- Verify supplier credentials are current
- Check product availability
- Review error logs

**Pricing Discrepancies:**
- Verify markup configuration
- Check currency settings
- Review discount and commission rules
- Confirm rate updates are current

For technical issues with supplier integrations, contact your system administrator or technical support.

## Related Topics

- [Creating Self-Operated Products](../../creating-self-operated-products/creating-self-operated-products.md) - Build product catalog for direct suppliers
- [Search & Book](../../search-book/search-book.md) - How supplier products appear in searches
- [Finance](../../finance/finance.md) - Supplier invoicing and payments
- [Analytics](../../analytics/analytics.md) - Supplier performance reporting
