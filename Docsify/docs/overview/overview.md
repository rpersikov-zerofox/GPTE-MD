# OVERVIEW

GP Travel Enterprise is a state-of-the-art web-based solution that provides immense opportunities for travel companies to fully automate business processes, including back-office management and interaction with partners, as well as online sales of travel services. The purpose of the system is to simplify and accelerate searching and booking of travel services, rendered by various suppliers. Moreover, using the configuration and control tools you can create a single workspace to cooperate with a vast network of clients (including travel agencies and distributors) granting access to respective information for them.

<table>
  <colgroup>
    <col style="width:55%" />
    <col style="width:45%" />
  </colgroup>
  <thead>
    <tr>
      <th>GP Travel Enterprise features</th>
      <th>Our Clients</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Access to world leading suppliers and GDSs</li>
          <li>Inventory management with detailed description of travel products, prices and availability</li>
          <li>B2B and B2C online booking</li>
          <li>Comprehensive reservation and finance management</li>
          <li>API for integration with 3rd party applications</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Destination Management Companies</li>
          <li>Online booking portals and OTAs</li>
          <li>Airline companies</li>
          <li>Outbound and inbound tour operators</li>
          <li>Travel services consolidators</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

<table>
  <colgroup>
    <col style="width:45%" />
    <col style="width:55%" />
  </colgroup>
  <thead>
    <tr>
      <th>Highlights</th>
      <th>Advantages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Data repository: MySQL (with optional porting to Oracle).</li>
          <li>Access: multi-user via the Internet.</li>
          <li>Architecture: "client-server" (all business logic is managed on a centralized server).</li>
          <li>Accessibility: 24/7, upwards of 99,9% (including time for scheduled updates).</li>
          <li>Programming languages and frameworks of the system: Java, XSLT, JS.</li>
          <li>External components: Jasper Reporting, AmCharts, Google/Yandex maps.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Allows permanent access 365/24/7.</li>
          <li>Works online via the Internet.</li>
          <li>Provides instant booking of travel services directly from suppliers.</li>
          <li>Supports multi-user access for suppliers, agencies, tour operators and their staff, and individual travelers with different user permissions.</li>
          <li>Provides access to change history logging.</li>
          <li>Designed for international markets (with multilanguage descriptions and multi-currency support).</li>
          <li>Allows manual input of currency rates and integration with various financial information sources (banks, currency exchange rates APIs, etc.).</li>
          <li>May be utilized in various configurations.</li>
          <li>Enables complex automation of business processes and flexible adaptation to numerous business models.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Business Model

GP Travel Enterprise is a multifunctional modular platform that includes more than 100 modules. The architecture can be easily customized on demand to suit the requirements of various business models and it covers such aspects as BUYING travel products from suppliers, SELLING them via B2B/B2C sales channels and MANAGING processes and reservations.

![Business Model.jpg](/assets/Business-Model.jpg)

The modules of the system are combined into six independent components to solve the specific range of business tasks. All components and modules of the platform can be combined in many ways and also include scalability mechanisms for adaptation to business processes and unique needs.

| Component | Business tasks |
|---|---|
| HUB | Provides a unified interface for integration with multiple travel suppliers. |
| INVENTORY | Allows to manage own and directly-contracted inventory (prices, availability, descriptions, policies). |
| B2B | Builds up B2B distribution network. |
| B2C | Handles sales to end consumers. |
| ENTERPRISE MANAGER | Provides a fully functional back-office solution for configuring markups & commissions & other sales rules, managing reservations, creating invoices, controlling payments and obtaining analytics. |
| GATEWAYS | Enhances business automation via integration with external systems (e.g. CRM, Accounting, online payment gateways, etc.). |

## Platform Delivery and Administration

### Installation Options

GP Travel Enterprise can either be hosted on GP Solutions dedicated servers or on clients\' servers.

**Dedicated Server**

Individual software installation on a dedicated server of a client is the most common implementation option. The platform installation and configuration is performed by GP Solutions specialists. In case of plans for on-going customisation of the solution, we recommend having an additional test server for internal use.

**Multi-Server Installation**

If the system is supposed to process a large amount of booking transactions (approximately more than 5 000 bookings per month) or if high search load is expected, it is recommended to use the multi-server installation to assure a high performance level.

:::: note
::: title
Note
:::

Each multi-server installation is configured on a case-by-case basis according to every client's exact requirements.
::::

::: dropdown
**Parameters to consider:**

1.  Which and how many external suppliers are to be connected.
2.  How many company\'s self-operated travel products will be stored in the company\'s database (e.g. hotels, tours).
3.  Expected number of B2B users and concurrent sessions.
4.  Expected number of B2C guests and concurrent search queries.
5.  Number of offices/branches (for the Holding configuration).
6.  Number of websites (for tour operators and agencies).
7.  Expected number of search queries per day.
8.  Rates of search queries in peak hours.
9.  Expected number of bookings per month.
:::

### System Settings and Adjustment

With the system customization features, you can easily configure the platform to meet specific requirements of clients:

- Functional modules adjustments (e.g. setting up the rules for payment methods and penalty charges).
- UI adjustments (e.g. unique company logo, color schemes, utilized images).
- Document and report customization (e.g. control over vouchers, invoices, product descriptions).

### 3rd Party Integrations

GP Travel Enterprise implementation flexibility enables integrations with third-party software. It allows:

- Getting connected to new product suppliers;
- Getting connected to various online payment systems;
- Getting integrated with accounting software (e.g. 1C);
- Enabling user authorization via external system (e.g. LDAP);
- Getting integrated with the company's and partners' self-developed or 3rd party software.

## Technical Requirements

To provide efficient operation of GP Travel Enterprise the server and Internet browsers should meet the following requirements.

### Server Requirements

Live Server:

- CPU: 16 cores with HT, starting from 2.5 GHz.
- RAM: 128 GB.
- STORAGE: 1+ TB NVME in RAID 1 in ZFS filesystem.
- OS: Ubuntu Server 24.04 x64 in min setup (only ssh server installed).
- External FTP backup 500Gb+.
- CREDS: root access to the server.
- Internet connection: 1GB/sec.

Test Server:

- CPU: 8 cores with HT, starting from 2.5 GHz.
- RAM: 32+ gb (more - better).
- STORAGE: 1+ TB NVME in RAID 1 in ZFS filesystem.
- OS: Ubuntu Server 24.04 x64 in min setup (only ssh server installed).
- External FTP backup 500Gb+.
- CREDS: root access to the server.
- Internet connection: 100 Mb/sec at least. 1GB/sec is preferred.

These are the minimum requirements. The requirements are applicable in case of the Full Platform installation (all components) on one server. Server requirements may vary in case separate components are installed (e.g. HUB only).

The requirements for partial platform installation (separate components) are to be defined during implementation. Likewise, multi-server configuration may lay down different requirements to various types of servers (database server, application server). As a result, the final server configuration is defined case-by-case.

### Browser and Client PC Requirements

The system is web-base and therefore does not require PC installation. Before you start working with the system, make sure that your PC is connected to the Internet and has a browser installed. If you want to use the system in the form of application, you can download the Mozilla Prism application. You will be able to launch the system with this application, without using a browser.

:::: note
::: title
Note
:::

To ensure the system work correctly, it is recommended to set the minimal screen resolution to 1366x768.
::::

## Operational Requirements

### Logging in

After you company is registered in the system, you receive log in data. Using it you can log in to the system and start working with GP Travel Enterprise.

### Introduction to the Home Page

The GPTE home page is a starting point for users to get to know the system and configure products, reservations, clients, analytics, tour operator-supplier relations, etc. At the same time, here travelers are able to access a customizable service search form and create a new reservation request (no login-in is required).

![Home Page New.jpg](/assets/Home-Page-New.png)

The old interface of GPTE has different view of its home page. The layout of the home hage depends on the role of a logged-in user and on the platform section currently opened, therefore it may differ from that depicted in the screenshot below.

The areas shown in the figure are:

1.  **Navigation bar** - to move across the platform sections.
2.  **Search form** - to search for travel products and services.
3.  **Workspace** - The contents of the workspace depend on the selected system section. The workspace can display dialog boxes, each with a number of tabs that enable a user to browse the subsections.
    - On the Home page, the central part of the workspace displays news, links and tips. The contents of the workspace are generated and regulated by system users.
    - On the right side of the screen, on the home page, there is a list of 10 most popular destinations. The list features the cities/regions that are searched for and booked most frequently in the system.
    - Below the list of popular destinations, there is the Currency rates form.

![Home Page Old.jpg](/assets/Home-Page-Old.jpg)

### Exporting Data to Excel

By using GP Travel Enterprise you can export system data to a Microsoft Excel file. In some cases, the browser you use may not allow downloading files from external web-sources. In such cases, configure file export. The configuration procedure varies depending on the browser you use. Please, refer to the browser web help for detailed information on exporting data.

### Online Help

The system has reference pages for all the general sections and subsections. Online help is intended to highlight the necessary information and give prompt responses regarding system functionality. To get a reference on a particular section, click the Query icon.

![Online Help.jpg](/assets/Online-Help.png)

### Frequently Asked Questions

To make the process of using GP Travel Enterprise easier for system users, you can create a list of frequently asked questions.

### Multilingual Description

In the system, the pages containing textual data are localized. It means that you can enter textual information in different languages. It may be particularly useful if you offer services on a international level and have a network of clients across the globe. In this case using multilingual description will help you to successfully distribute your products and operate on the markets of different countries.

## BASIC FUNCTIONALITY

Before you can start sales via the system first of all you need to configure your company profile, your suppliers & products you want to sell, your clients & sales rules, as well as financial conditions. After you configure these basic options you will be able to accept bookings, manage reservations and payments, as well as receive analytics on the workflow.

### Company Profile

Your company is the central element of GP Travel Enterprise. Before getting to work with the platform, you should configure your company profile. Configuring your company profile is implemented through 3 steps:

- **Configuring general information**about the company and **uploading documents** needed for proper business communication.
- **Creating profiles for the users.** Every employee who will work with the system must be registered as a unique user. User profiles are created to ensure proper system functioning and to differentiate access rights to the information stored in the system.
- **Specifying company settings** - personalize the look of the system so that it complies with your brand and identity as well as configure the localization preferences, links with external applications, and notifications.

### Managing Suppliers & Purchases

In GP Travel Enterprise there are two ways to develop a travel product:

- Sell existing offers from external suppliers or GDSs (real-time connection via API).
- Develop self-operated travel products.

The first step of developing a product is establishing connections with suppliers - either external or direct. There are 2 ways to configure the suppliers:

- Connect to external suppliers via XML API.
- Create direct suppliers for self-operated products.

After the suppliers are connected to the system, you can either start selling services of external suppliers or create your own self-operated products, provided by direct suppliers.

GP Travel Enterprise features all functions and tools required to develop self-operated products: hotels, transfers, tours and many others. The management of self-operated travel products is implemented via Inventory module. Inventory allows travel companies to create their own travel products (for example, sell the company's own transfers or excursions) and also add direct contracts with suppliers, which don't have the possibility to be connected online. The process of self-operated product development includes entering the description of a product and specifying rates and availability.

The Inventory module is represented by common solutions for the following purposes:

- Input of descriptions of travel products (short and detailed descriptions, photo gallery, services)
- Configuration of pricing (various kinds of price lists: for different season; specific setup for discounts, cancellation conditions, etc.)
- Management of availability (allotments for room availability for hotels and tours, timetable and seats availability for transfers, charters, etc.)

With the help of these solutions, it is possible to create various types of travel services and place them for sale reasonably quickly. It's important to mention that the Inventory core itself is a technological structure, and its value for the end users is defined by its individual modules specially adapted for specific products:

- Accommodation (Hotels, Villas, Apartments, etc.),
- Charters,
- Transfers,
- Car Hire,
- Excursions,
- Events,
- Tours,
- Visas,
- Insurance,
- Extra services,
- Cruises,
- Package tours,
- Complex Tours and Packages.

In general the process of developing self-operated products includes the following steps:

1.  **General product description**. The first step implies entering basic information on the product or service. The information to be specified varies depending on the product. There are however certain common fields: 1. Adding general information on the product, including name, supplier, transaction currency, and the description of the product itself. 2. Adding particular categories to a service catalogue (for example, categories for accommodation, service classes for charters, type for excursions and tours, etc.) 3. Creating traveler categories. The Adult category is created by default. In case you want to provide special rates for children or elderly travelers, you can add corresponding categories and later adjust price calculation. 4. Scheduling services. Includes setting service schedule (usually service start time.) 5. For some products configuration of relevant additional services is also available.
2.  **Price configuration.** Price configuration includes several steps, and generally consists of: 1. Creating tariffs according to which the prices are calculated and sales terms are formed; 2. Creating price-lists for a product and all services it includes; 3. Adding a price list for additional services; 4. Selecting types of discounts and specifying terms of their application; 5. Setting penalties.
3.  **Availability.** Specifying allotments of seats or rooms available for booking (if you have corresponding agreement with suppliers) or configuring sales "on request".

As a result, a travel product is created in the system and becomes available for search and booking. If needed, all new products can be modified.

### Managing Clients

Using management and control tools, you can create and manage your own vast network of partners and clients. You can add sub-agencies via which you re-sell your travel products, as well as create profiles for corporate and private clients.

Each type of clients has its own specifics:

**Agencies** -- companies that re-sell your travel products to end consumers. The main concept is that they can only sell using sales terms that you configure for them in advance, and usually they get commission that is being configured within the contact with them. You can either accept requests from your agencies via phone and then create reservations on behalf of them. Or, alternatively (and more often), you can give access to the system for agencies themselves so that they can search&book and communicate with you via the system.

The full procedure of registering a new Agency includes the following steps:

- Creating a new agency company profile.
- Uploading company documents.
- Adding users of the company.
- Configuring contract terms.
- Adjusting the look and feel of the system (if necessary).

**Multi-Level Distribution Chains** - gives the ability to re-sell your travel products via some intermediary companies (usually either some wholesalers or agency chains or other Tour Operator), who have their own sub-agencies. The main concept is that they can get from you Net rates (that are usually composed as your Net rate from supplier + your Markup) and can configure their own clients and own markups for them. This allows to involve multiple companies into the distribution and automate search&book processes for all of them on the same platform. At the same time, please, note that only Tour Operator Level 1 (licensee owner) will be able to configure travel products and connections to suppliers. While other distributors in chain will be able to sell them, but not create&manage own products.

This is depicted in the following diagram:

![Multi-Level Distribution Chains](/assets/Multi-Level-Distribution-Chains.jpg)

The main capabilities of this module are:

- Register Tour Operator accounts as clients (so called Tour Operators Level 2)
- Ability to log in as Tour Operator Level 2 and configure own Travel Agencies with own sales conditions for them (markups&commissions)
- Search&book travel products both within Tour Operator Level 2 account and their sub-agencies
- Get analytics on turnovers and actual amount due with regards to suppliers and clients on any level of the distribution chain.

How it works:

1.  Tour Operator Level 1 (supervisor of your company) logs into the system, goes to My company -\> Clients legal and creates new company with type "Tour Operator" and configures sales rules for him (e.g. markup +10%).
2.  Tour Operator Level 2 logs into the system and goes to My company -\> Clients legal and creates his own sub-agencies and configures sales rules for them (e.g. markup + 20% and commission 15%).
3.  Travel Agency beneath Tour Operator Level 2 logs into the system and makes a booking. After that every company in the chain sees this booking with corresponding net and gross prices in their accounts.

**Corporate Clients**-- organisations that require travel services for their own employees or partners.

By using GP Travel Enterprise, you can manage business trips and incentive travel for corporate clients, sell travel products and services to them, keep a record of such clients and set specific sales terms for each of them. Moreover you can give access to the system for corporate clients themselves so that they can search&book and communicate with you via the system.

In the following section the basic functionality on configuring corporate clients is presented. If you are interested in extended corporate sales with ability to configure and use corporate policy, approval schemas, extended profiles, etc. -- please visit the respective section of the current document.

### Managing Sales

The Sales settings section lays the foundation for the configuration of sales conditions of tour operator and managing contracts for B2C and B2B sales.

Relationships between companies are regulated by contracts - a union of sales conditions that include:

- What products should be available
- What markup and commission should be applied
- Whether VAT should be applied or not
- Etc.

In compliance with the type of client and cooperation, rates and marketing terms can be configured in the following ways:

- Direct sales: these are the sales conditions that are applied if Tour Operator staff sells services directly to travelers.
- Web sales: these are the sales conditions that are applied for search&book via Tour Operator web site (when travelers make bookings by themselves).
- Groups of contracts: B2B clients can be arranged into groups with the same contract terms set for all of them. It's possible to create as many of such groups, as you need.
- Individual contracts: in this case you configure individual terms with a particular client.

### Search & book

By using GP Travel Enterprise you can book all the different travel products offered by suppliers. The booking procedure includes several steps:

1.  Search for the products you are interested in. At this stage the platform provides information about the availability of rooms (tickets, seats) that can be booked immediately. Depending on the availability of allocated places the platform supports two types of booking: 1. free booking - the services can be booked immediately; 2. booking upon confirmation - at the time of booking, information about the reservation is saved, but the manager must contact the supplier to confirm the booking.
2.  View search results. If you are not satisfied with the search results you can go back and repeat the search.
3.  Choose and book the product you are interested in.
4.  Get booking confirmation from the supplier. The final step includes creating a reservation and saving it in the system. If needed, you can modify reservations and add new products to them.

You can search for travel products and services using 3 different methods. Specifically,

- Using the Search form;
- Creating a new reservation request;
- Creating a new reservation for a particular client.

### Reservations

In GP Travel Enterprise all the reservations are stored in one directory. On the Reservations page, you can fully manage company's reservations, specifically:

- Search for reservations
- View and edit existing reservations
- Create new reservations
- Assign and re-assign reservation managers
- Receive/issue invoices for reservations

### Finance

The Finance module helps you track financial operations and acquire complete information about the company's financial flow. Finance module include the following funcctionality:

**Ledgers** - information about financial transactions between your company, customers and suppliers is stored in the finance module of the system. By using general ledgers you can view trade liabilities, debts of the customers as well as income and expenses and thus keep track of your company's financial flow.

**Deposit** - Using deposits your agencies can prepay the services that they book. If an agency uses an e-commerce online payment system for transferring a certain amount from a credit card to you, it reflects immediately in the system. However, if the agency uses a bank transfer to pay you, you should register this in the system by placing a respective amount to its deposit. Only tour operators can withdraw funds from the deposit.

**Invoices** - GP Travel Enterprise gives you extended possibilities to manage invoices. After invoicing, you can view all the invoices, both issued to your clients and requested from suppliers, and pay, download, or cancel them.

**Statement of Account** - With GP Travel Enterprise you can track all financial transactions between a tour operator and suppliers as well as all transactions made by any customer.

**Payment Settings** - the following points covered here:

- **Configuring invoice print-out settings** - With GP Travel Enterprise you can customize the parameters that are used to generate invoices. General parameters are set by default in the system; however, you can configure them individually
- **Configuring VAT** - In order to make correct financial payments between a Tour operator and Travel agencies, you can calculate prices of services, including the value added tax, and view information about VAT in the invoices that are issued to a customer.
- **Configuring Payment Plans** **and Payment Methods** - It is necessary to configure payment plans and methods for customers, specify either one method of payment or some mutually exclusive methods of payment (e.g. in the case when your first specified method have effect only till occurrence of penalty period, and the second - after its occurrence).

**Online Payments**- contains every transaction made by customers via online-payment systems.

### Analytics

With the Analytics module you get full control over sales and operational efficiency. It helps you obtain the latest data over any period including the amount of reservations generated by agencies, supplier inventory statistics, improve your workflow, rate partners' results and profitability and decide on your future priorities.

All system reports fall into 5 major groups:

1.  **Analytic** reports - allow to review your business activity including sales reports with breakdown by agencies, suppliers, regions, and other criteria, dynamics of sales, look-to-book ratio.
2.  **Corporate** service reports - allow you to obtain the list of cases of corporate policy violation.
3.  **Financial** reports - include detailed information on flows of funds.
4.  **Inventory** reports - allow you get a summary of prices in printable form and to see general statistic on availability of your selfoperated products.
5.  **Rooming** list reports - allow you to obtain lists of travelers who are going to check in or get a charter or transfer within certain period of time.

You can generate reports both in PDF and Excel format.

### General Settings

This section covers a wide range of points related to the configuration of the system. You can see the lists of companies and users, create news to display on the Home page, configure visa services and currency rates and view frequently asked questions.

## Extended Functionality

### Extended Company Structure

*Holdings*

In GP Travel Enterprise, for organizations of complex structure a specific Holdings module was developed. This module will help you to manage bookings if your company consists of several relatively independent divisions (e.g. a head office and a number of departments) situated in different cities or countries. With the Holdings module, all branches of the company will be able to book services from each other. Every one of them will be able to independently control its finances, issue invoices on its own behalf and have its own agencies network. With Holdings, you will be able

- Set types of relationships and financial conditions between your company's branches
- Search&book travel products throughout different units of the organization
- Manage bookings independently within each division.

*Multi-level distribution*

Multi-level distribution enables a tour operator to configure complex distribution chains and sell products not only directly to end-customers or travel agencies, but also to other tour operators or agency chains. Tour operators and travel agencies in their turn will be granted possibility to create their own subagencies and configure sales rules for them.

The multi-level distribution allows to involve multiple companies into the distribution and automate search&book processes for all of them on the same platform.

At the same time, please, note that only tour operator of the 1st level (licensee owner) will be able to configure travel products and connections to suppliers. Other tour operators and agencies in the chain will be able to sell them, but not create and manage self-operated products. With the multilevel distribution, you will be able to:

- Register tour operator accounts as clients (tour operators level 2)
- Log in as tour operator level 2 and configure own travel agencies with own sales conditions for them (markups and commissions)
- Search&book travel products both within tour operator level 2 account and their sub-agencies
- Get analytics on turnovers and actual amount due with regards to suppliers and clients on any level of distribution chain.

### **Extended Search & Book capabilities**

*HotelMapping*\* \*

Hotel Mapping module is a plug-in to Hotel Content Management module that allows grouping the same hotels from different suppliers. This might be useful if you would like to combine them altogether and show the best price for a hotel among multiple suppliers. With mappings of hotels you can:

- Use predefined automatic mappings (when hotel name and address are the same)
- Manually review and set grouping for the same hotels
- Automatically recognize duplicating hotels during search&book and return identifier that this is the same hotel.

Note that you can either use Hotel Mapping Tool (if you want to map by yourself) to order the mapping services from GP Solutions.

*Extended flights search & book*

- **\*Flight search by schedule**\* Flights Search by Schedule module allows you to search flights not only by price but by departure date and time as well. This feature can be useful for cases when clients know the exact dates or time of departure and arrival and the price of a ticket is not considered as the main search criteria. The key features are: \* Displaying flights search results according to their departure time and dates; \* Checking availability and prices of the selected options.
- **\*Voiding tickets**\* Flights Void allows you to void issued e-tickets directly from the system. Thus you can void a ticket within 24 hours from the booking time.

### **Packaging**

With GP Travel Enterprise you can not only sell separate travel products (e.g. accommodation, flights, transfers, etc.) but combine them and distribute as travel packages. Depending on the nature of packaged products, in GP Travel Enterprise we single out Dynamic Packages and Complex Tours.

Dynamic Package stands for the combination of travel services distributed as one product entity. The constituent services are not fixed - you can choose and combine them to meet your specific needs (e.g. replace one component with another).

Complex Tour stands for a package a package usually consisting of several components with a fixed itinerary. The constituent services cannot be changed and replaced since the program of a complex tour is predefined.

### **Extended management of reservations**

*Service teams*

Each service team is comprised of the tour operator\'s employees and is responsible for processing one or several types of services (for example, one group may be responsible for hotels, while the other processes flights and train reservations). A manager of the service group is appointed, while other employees process the reservations if the manager is absent or unavailable.

*Arbitrary offline bookings*

With the Offline Bookings module you can fill in details of any booking that was made by your staff in any system. Just fill in booking details, traveler details, net and gross rates and the system will keep information easily accessible within the database. With Offline Bookings, you can

- Create offline reservations;
- Fill in booking details and traveler details;
- Specify prices and fees.

### **Extended Corporate sales**

*Extended profiles of employees*

Sometimes when working with corporate clients you have to specify additional data about employees, such as position, department, priority, direct supervisor, etc. Since the fields of this type are specific, the need in them may vary from company to company. Thus these fields can be created and configured individually in the profile of a separate corporate client. You can specify this information in the profile of an employee and copy it to the reservations for further management accounting. Besides, you can use it for setting the rules and terms of corporate policies and authorization procedures.

*Corporate policy*

For corporate clients, you can set conditions for corporate bookings and restrict certain elements to the value that is accepted in your company. For example, allow to book accommodation only if the price per night is no more than \$100. The restrictions can be applied to the following types of services:

- Hotels.
- Flights.
- Transfers.
- Trains.

Then if a corporate user books a service, the system will check if the service falls under the corporate policy conditions

*Approvals*

For corporate reservations, you can set the conditions for approval. In this case, once a reservation is made for a corporate client, its status will not be set to completed unless the reservation is approved by a user with respective approval rights.

Upon creating a reservation, a request for approval is sent to a user with approval rights

As soon as the reservation is approved, its status will be set to complete.

*3rd party contracts*

3rd party contracts module allows to configure and use specific agreements between Tour Operator, their Corporate Client and Supplier. For example, if a client has their own specific code for GDSs to get better prices and agreed rates -- it can be configured and thus system will check both client prices and public prices to find the cheapest offers for the client. With 3rd party agreements it is possible to

- Configure tripartite agreements with Corporate Clients
- Use tripartite agreements for search&book to find client-specific rates.

*Budget control*

Budget Control module saves minimal offer prices and flight variants and compares them with the cost of the booked offers. This data is saved to the reservations and can be viewed in the form of financial reports. With such reports you will have all the necessary information including number of booked flight offers in the period under review, total price and price difference. With budget control you can

- Save minimal price of flights in the reservations
- Get notified about loss of profit
- Get information about final price when the e-tickets are issued
- Create the loss of profit reports

### **Channel Manager**

A channel manager is a service provider that links the property management system (PMS) you use to manage your rooms and prices with online platforms like Booking.com, Expedia, GDS, etc. It lets you automatically update your rates, availability and reservations across several platforms all at once. If you don't have a PMS, certain channel managers can provide you with one. If you're selling rooms on more than one online platform, a channel manager will save you time and effort. It gives you a fast, easy way to update your prices across all online channels. You\'re also far less likely to get overbooked because as soon as a room is sold, it will automatically be removed from all other online channels. If you\'re offering availability across various platforms with a channel manager, you\'re more likely to sell your rooms for a good price during low season.

There are 2 ways of working with Channel manager:

1.  IN - prices and availability are loaded from hotels to inventory through channel manager. There is no need for the hotel's personnel to log in to every single channel in order to update availability. Channel managers receive information about bookings made through the online booking platform and transfer it to hotels

![Channel Manager IN](/assets/Channel-Manager-IN.jpg)

2.  OUT - prices and allotments are transferred to a Channel Manager through TO system (Inventory). When a booking is made, its information is sent to TO system back to pass it to hotels. The Channel Manager will automatically reduce availability when a room is booked on any one of your sales channels.

![Channel Manager OUT](/assets/Channel-Manager-OUT.jpg)

### **Extended CRM**

Extended CRM --- gives the ability to combine the online booking engine and management of relationships with your clients within single platform. Starting from Release 7.1 GP Travel Enterprise allows to do both! With Extended CRM set of modules you can:

- Classify your clients
- Track opportunities with potential clients
- Manage marketing campaigns
- Keep history of communications with clients
- View overall analytics on clients

*Loyalty*

A loyalty program is a special marketing tool that helps a company to establish long-term relationships with its customers and to turn them into frequent buyers. For instance, by using this tool you can stimulate direct sales and offer cumulative loyalty programs to your customers. The essence of such programs is that for each booking made through your company customers earn a certain number of points.

*Classifications*

Extended CRM Classifications --- allow you to: Mark your clients as VIP / high / low / normal priority Classify your clients depending on their industry and company size Differentiate potential and actual clients

*Opportunities*

Extended CRM Opportunities --- allow you to handle "big deals" with potential clients. Thus you can participate in tenders for corporate travel management or hold negotiations with large Agency chains and within the system reflect the current status of each such opportunity and assign who is responsible for it.

*Campaigns*

Extended CRM Campaigns --- allow you to manage marketing campaigns. Thus you can plan what steps towards gaining new clients you're going to undertake, what is the allocated budget and who is responsible for each campaign.

*History of Communications*

Extended CRM History of Communications --- is the way to have full knowledge on your clients and relationships with them. With this module you can:

- Record all calls and meetings held with your clients
- Plan and send arbitrary e-mails to your clients directly from the system
- Have reminders on home page about upcoming events
- Get quick and easy access to history of all previous communications with regards to a certain client, opportunity or reservation

*Analytics*

Extended CRM Analytics --- gives you full overview of your clients including average trip budget, preferred locations, categories and more. With these analytics you can have better understanding what can be proposed to each company.

*Subscription for marketing e-mails*

There's a possibility to specify which of your clients should receive marketing emails. You can use this option to organize mass mails.

### **GDS Terminal**

GDS Terminal - is an emulator that gives you the possibility to run commands directly to GDS for processing of complex reservations, for refunds, exchanges and more.

Please, note that this is not the standard way to communicate with GDS via API, so if you're interested in this module, first of all you will need to request access from GDS to such functionality.

Ability to switch to GDS Terminal and send commands/look through reports in terminal mode is provided to tour operator users with user roles Manager and higher. In order to make it easier to work in GDS Terminal special characters converter was developed.

GDS Terminal allows you to:

- Obtain air schedule and availability;
- Get flight information;
- Make booking requests, modify them;
- Retrieve PNRs;
- Receive Fare Rules;
- Process complex reservations;
- etc.
