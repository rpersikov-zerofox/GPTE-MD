# Tags

**This functionality is currently available via administration panel.**

By using tags you can manage access of certain clients to products and rates. For example, by labeling certain products with the \"private\" tag you can show them only to some clients and hide from others.

You can create, edit and delete all tags, except for the default \"public\" tag.

![image-20201005-195418.png](/assets/image-20201005-195418.png)

To set tags,

1.  Go to the contract, tab tags.
2.  Click Edit to switch to editing mode.
3.  Specify tags within "Included" and "Excluded" blocks to define what products should be available or not available for this sales channel. You can either use pre-defined tags to switch off some suppliers or your own tags that you define in self-operated products (see ). Based on matching tags system will show or not show corresponding product.
4.  Click Save.

There are certain restrictions to the tag names: ·A tag name should consist of one or several words written in Latin characters. ·A tag name can include maximum 500 characters. ·If you use several tags, they should be separated with a comma.

Every product and contract has "public" tag by default. This means that this product is available for all clients. If you don't want to make any limitations, please, don't erase this tag from settings. It should be kept as it is.

**Pre-defined Tags**

You can use tags to determine the suppliers whose offers are available to a particular customer or for a particular sales channel. All possible options are listed in the table below.

  -----------------------------------------------------------------------------------------------------------------------
  **Offers from the suppliers that need to be displayed**   **Tag that needs to be specified in the contract settings**
  --------------------------------------------------------- -------------------------------------------------------------
  From all suppliers                                        public

  From one of the external suppliers                        supplier:SupplierСode

  From all direct contracted suppliers                      \*:public

  From one of the direct contracted suppliers               SupplierTag:public
  -----------------------------------------------------------------------------------------------------------------------

Table comments:

- The supplier code for external suppliers and GDSs cannot be ascribed manually in the profile of a supplier. To determine the external supplier whose products are available for a particular customer or sales channel, in the contract settings of the customer, use the respective code that corresponds to the particular external supplier (see the table below).

  -----------------------------------------
  Supplier            Code (SupplierCode)
  ------------------- ---------------------
  Abreu               abreu

  Academservice       academ

  Aeroexpress         aeroexpres

  Alphastrakhovanie   alpha

  Amadeus             amadeus

  A&A                 aeroclub

  Alean               alean

  AmandaTour          amanda

  CarDelMar           cardelmar

  CarTrawler          cartrawler

  Diethelm            diethelm

  Dolphin             dolphin

  DOTW                dotw

  Eurotours           eurotours

  Expedia             expedia

  Galileo             galileo

  GoGlobal            goglobal

  GTA                 gta

  HBSi                hbsi

  Hotelbeds           hotelbeds

  HotelsPro           hotelspro

  Hotusa              hotusa

  iWay                iway

  JacTravel           jacob

  Jumeirah            jumeirah

  Kandagar            kandagar

  Kuoni               kuoni

  Miki                miki

  Multitur            multitur

  Novasol             novasol

  ATS Pacific         pacific

  RoomsXML            rooms

  RCR                 rcr

  Roza Vetrov         roza

  Sirena travel       sirena

  Terramar            terramar

  Tourico             tourico

  TOWERS              towers

  Travco              travco

  Viator              viator
  -----------------------------------------

For your own contracted suppliers, you can specify the Supplier code manually by entering the tag prefix in the profile of a direct contracted supplier.

1.  On the Navigation bar, point to **Suppliers** and click **Suppliers**.
2.  In the Name column, click the supplier of your choice.
3.  On the\*\* Supplier\*\* page, click **Edit** to switch to editing mode.
4.  Locate mouse pointer into the Tag prefix box and type the supplier code.
5.  Click **Save**.

![image-20201005-201234.jpg](/assets/image-20201005-201234.jpg)

Let us consider an example of tag application for external and direct contracted suppliers.

- To ensure the availability of offers from the external Hotelbeds supplier only, in the client contract settings (Navigation bar - Clients - Contract - Tags), add the following tag: **supplier:hotelbeds**

![image-20201005-201336.jpg](/assets/image-20201005-201336.jpg)

- To ensure the availability of offers from the direct contracted Travel Guard supplier only, in the client contract settings, add the following tag: **supplier:travelguard**or\*\* travelguard:public\*\*

![image-20201005-201425.jpg](/assets/image-20201005-201425.jpg)
