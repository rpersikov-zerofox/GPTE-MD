# User Roles

Each user account requires an assigned role that determines system access and permissions. User roles control what actions users can perform and what information they can access.

## Available Roles

The following roles are available in GP Travel Enterprise. Click each role to view details.

<details>
<summary><strong>Accountant</strong></summary>

**Primary Function:** Financial management and invoice processing

**Permissions:**
- View all reservations within the company network
- Issue customer invoices for reservations
- Manage auto-cancellation settings on reservations
- Configure invoice terms and conditions
- Access financial ledgers and accounting records

**Typical Use:** Accounting department staff managing finances and billing
</details>

<details>
<summary><strong>Agent</strong></summary>

**Primary Function:** Create and manage personal reservations

**Permissions:**
- Create and process reservations for travel products and services
- Access only their own reservations (no visibility of other agents' work)

**Typical Use:** Front-line booking agents with limited access
</details>

<details>
<summary><strong>Avia Sales Manager</strong></summary>

**Primary Function:** Flight reservation specialist

**Permissions:**
- Create flight reservation requests
- View all company reservations
- Modify flight reservations (issue e-tickets, cancel, synchronize with suppliers)

**Typical Use:** Specialized aviation department staff
</details>

<details>
<summary><strong>Content Manager</strong></summary>

**Primary Function:** Product content and descriptions

**Permissions:**
- Create, view, and edit hotel descriptions
- Manage direct contracted supplier information
- Edit self-operated product descriptions

**Typical Use:** Marketing or product management staff
</details>

<details>
<summary><strong>Director</strong></summary>

**Primary Function:** Full system administration and management

**Permissions:**
- **User Management:** Create users, assign passwords, modify user data for company and client companies
- **Network Management:** Register partners and client companies, create user accounts for partners, configure contracts
- **Reservation Management:** Create, view, modify, and cancel all reservations across the entire network
- **Approval Authority:** Manually change and cancel reservations requiring approval
- **Product Management:** Create tour products and packages
- **System Configuration:** Access all general system settings
- **Reporting:** Generate all available reports

**Typical Use:** Company owners, executives, system administrators
</details>

<details>
<summary><strong>Dispatcher</strong></summary>

**Primary Function:** Schedule and transport coordination

**Permissions:**
- Access scheduler functionality
- View group lists and configured transport
- Resolve schedule-related issues

**Typical Use:** Operations staff managing group departures and transportation
</details>

<details>
<summary><strong>Driver</strong></summary>

**Primary Function:** Limited access for transportation providers

**Permissions:**
- Search for services (cannot book)
- Generate reports

**Typical Use:** External drivers needing visibility into schedules
</details>

<details>
<summary><strong>Guest</strong></summary>

**Primary Function:** Demo and prospective client access

**Permissions:**
- Search offers and view pricing
- No booking rights

**Typical Use:** Potential agents or distributors evaluating your products and services

**Note:** Recommended for demonstration purposes only
</details>

<details>
<summary><strong>Guide</strong></summary>

**Primary Function:** Tour guide with read-only access

**Permissions:**
- Search for services (cannot book)
- Generate reports

**Typical Use:** Tour guides needing itinerary information
</details>

<details>
<summary><strong>Manager</strong></summary>

**Primary Function:** Team and client reservation management

**Permissions:**
- Create and process reservations for travel products and services
- Manage reservations created by company agents
- Manage reservations from assigned client companies
- View user information for own company and assigned client companies

**Typical Use:** Team leads managing agent activities
</details>

<details>
<summary><strong>Supervisor</strong></summary>

**Primary Function:** Senior administrator (almost full access)

**Permissions:**
- All Director permissions
- **Exception:** Cannot deactivate Director-role users

**Typical Use:** Senior management needing full access without ability to remove top administrators
</details>

<details>
<summary><strong>Sales Staff</strong></summary>

**Primary Function:** Sales team member with booking access

**Permissions:**
- Create and process bookings for travel products and services
- Access all company bookings
- Process bookings from company users and client companies
- Read-only access to direct sales settings
- Read-only access to client lists (legal and private)
- Generate reports

**Typical Use:** Sales team members needing visibility across all bookings
</details>

<details>
<summary><strong>Sales Manager</strong></summary>

**Primary Function:** Sales team leader with client management

**Permissions:**
- Create and process bookings for travel products and services
- Access all company bookings
- Process bookings from company users and client companies
- Read-only access to company users list
- Read-only access to direct sales settings
- Full access to manage legal and private client information
- Limited access to Finance tab
- Generate reports

**Typical Use:** Sales managers responsible for client relationships
</details>

## Role Selection Guidelines

Choose roles based on these criteria:

1. **Job Function** - Match the role to the user's primary responsibilities
2. **Access Level** - Grant minimum necessary permissions
3. **Data Visibility** - Consider what reservation data the user needs to see
4. **Approval Authority** - Determine if the user needs to approve or override bookings

## Related Topics

- [Creating New User Profile](../creating-new-user-profile.md) - Step-by-step user creation process
- [Modifying Users](../../modifying-users/modifying-users.md) - Change user roles and permissions
