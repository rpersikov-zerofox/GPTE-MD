# Exporting Data to External Applications

**Swagger**

The information stored within the system\'s database can be exported to external web sites, applications, accounting or CRM-systems, and external software. To configure the export of information via API:

1.  On the Settings tab, check the **Export data to external applications** check box.
2.  After you select the check box, the symbol appears. Click it to expand the **Export configurations** form.

![2024-10-28_22-41-16.png](/assets/2024-10-28_22-41-16.png)

3.  In the **Export configurations** form, fill in the required data:

- **Name**: the name of the external system.
- **URL**: the address of the web-service of external system in the web thatcan accept information in the format being supported by the system.
- **Methods**: the information to be sent to an external system. You can select several or all variants.
- **Format**: the format to send the information in.
- **Protocol**: ways of sending the information.

4.  Click **Save**.

If needed, you can specify several external applications. Click and repeat the procedure.

------------------------------------------------------------------------

**\*Example of Reservation Export:**\*

The system sends request **POST /order**(booking) or **PUT /order** (modify)\*\* \*\*to the external system in 2 formats:

- XML

<!-- -->

    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <SOAP-ENV:Header/>
      <SOAP-ENV:Body>
        <ns2:order xmlns:ns2="http://www.software.travel/gptours/export" xmlns:ns3="http://www.generation-p.com/GPTOURS/booking">
          <ns2:orderId>9416</ns2:orderId>
          <ns2:title/>
          <ns2:created>2022-11-15T23:17:50+02:00</ns2:created>
          <ns2:modified>2022-11-15T23:18:15.672+02:00</ns2:modified>
          <ns2:status>IN_PROGRESS</ns2:status>
          <ns2:agent>
            <ns2:id>1721205</ns2:id>
            <ns2:prefix>Mr</ns2:prefix>
            <ns2:firstName>Support</ns2:firstName>
            <ns2:lastName>Support</ns2:lastName>
          </ns2:agent>
          <ns2:manager>
            <ns2:id>1721205</ns2:id>
            <ns2:prefix>Mr</ns2:prefix>
            <ns2:firstName>Support</ns2:firstName>
            <ns2:lastName>Support</ns2:lastName>
          </ns2:manager>
          <ns2:agentCompanyId>1711626</ns2:agentCompanyId>
          <ns2:clientId>5923530</ns2:clientId>
          <ns2:clientType>DirectSales</ns2:clientType>
          <ns2:clientCompanyName/>
          <ns2:clientPerson>
            <ns2:id>5923530</ns2:id>
            <ns2:prefix>Mr</ns2:prefix>
            <ns2:firstName>Tom</ns2:firstName>
            <ns2:lastName>Boris</ns2:lastName>
          </ns2:clientPerson>
          <ns2:active>true</ns2:active>
          <ns2:customerPaymentStatus>NO_BILL</ns2:customerPaymentStatus>
          <ns2:supplierPaymentStatus>NO_BILL</ns2:supplierPaymentStatus>
          <ns2:serviceTable>
            <ns2:lines>
              <ns2:serviceId>1005139</ns2:serviceId>
              <ns2:serviceType>accommodation</ns2:serviceType>
              <ns2:created>2022-11-15T23:18:13.613+02:00</ns2:created>
              <ns2:modified>2022-11-15T23:18:14.286+02:00</ns2:modified>
              <ns2:status>CONFIRMATION_PENDING</ns2:status>
              <ns2:paymentMethodId>3842036</ns2:paymentMethodId>
              <ns2:supplierId>2051972</ns2:supplierId>
              <ns2:supplierCompanyName>Sultan Sands</ns2:supplierCompanyName>
              <ns2:supplierCode>company.2051972</ns2:supplierCode>
              <ns2:parentTO1Id>1711626</ns2:parentTO1Id>
              <ns2:refNum/>
              <ns2:startDateTime>2022-12-21T12:00:00+02:00</ns2:startDateTime>
              <ns2:endDateTime>2022-12-24T12:00:00+02:00</ns2:endDateTime>
              <ns2:serviceGroupId>0</ns2:serviceGroupId>
              <ns2:travelers>
                <ns2:travelerId>5923531</ns2:travelerId>
                <ns2:isTourLead>true</ns2:isTourLead>
                <ns2:travelerType>Adult</ns2:travelerType>
                <ns2:isChild>false</ns2:isChild>
                <ns2:citizenshipId>6880</ns2:citizenshipId>
                <ns2:citizenshipName>Germany</ns2:citizenshipName>
                <ns2:prefix>Mr</ns2:prefix>
                <ns2:name>
                  <ns2:firstName>Tom</ns2:firstName>
                  <ns2:middleName/>
                  <ns2:lastName>Boris</ns2:lastName>
                  <ns2:sentToSupplier>true</ns2:sentToSupplier>
                </ns2:name>
                <ns2:mealType>Half Board</ns2:mealType>
                <ns2:onExtraBed>false</ns2:onExtraBed>
                <ns2:onWithoutPlace>false</ns2:onWithoutPlace>
              </ns2:travelers>
              <ns2:salesTerms>
                <ns2:type>SUPPLIER</ns2:type>
                <ns2:price>
                  <ns2:currency>EUR</ns2:currency>
                  <ns2:amount>300.00</ns2:amount>
                  <ns2:commission>0.0</ns2:commission>
                  <ns2:amountDue>300.00</ns2:amountDue>
                </ns2:price>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-21</ns2:date>
                  <ns2:weekDayNumber>3</ns2:weekDayNumber>
                  <ns2:weekDayName>Wednesday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                  </ns2:price>
                </ns2:priceBreakDowns>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-22</ns2:date>
                  <ns2:weekDayNumber>4</ns2:weekDayNumber>
                  <ns2:weekDayName>Thursday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                  </ns2:price>
                </ns2:priceBreakDowns>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-23</ns2:date>
                  <ns2:weekDayNumber>5</ns2:weekDayNumber>
                  <ns2:weekDayName>Friday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                  </ns2:price>
                </ns2:priceBreakDowns>
              </ns2:salesTerms>
              <ns2:salesTerms>
                <ns2:type>CLIENT</ns2:type>
                <ns2:price>
                  <ns2:currency>EUR</ns2:currency>
                  <ns2:amount>300.00</ns2:amount>
                  <ns2:commission>0</ns2:commission>
                  <ns2:amountDue>300.00</ns2:amountDue>
                  <ns2:serviceFee>0.00</ns2:serviceFee>
                </ns2:price>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-21</ns2:date>
                  <ns2:weekDayNumber>3</ns2:weekDayNumber>
                  <ns2:weekDayName>Wednesday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                    <ns2:serviceFeeAmount>0.0</ns2:serviceFeeAmount>
                  </ns2:price>
                </ns2:priceBreakDowns>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-22</ns2:date>
                  <ns2:weekDayNumber>4</ns2:weekDayNumber>
                  <ns2:weekDayName>Thursday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                    <ns2:serviceFeeAmount>0.0</ns2:serviceFeeAmount>
                  </ns2:price>
                </ns2:priceBreakDowns>
                <ns2:priceBreakDowns>
                  <ns2:date>2022-12-23</ns2:date>
                  <ns2:weekDayNumber>5</ns2:weekDayNumber>
                  <ns2:weekDayName>Friday</ns2:weekDayName>
                  <ns2:price>
                    <ns2:currency>EUR</ns2:currency>
                    <ns2:amount>100.0</ns2:amount>
                    <ns2:serviceFeeAmount>0.0</ns2:serviceFeeAmount>
                  </ns2:price>
                </ns2:priceBreakDowns>
              </ns2:salesTerms>
              <ns2:modificationAllowed>false</ns2:modificationAllowed>
              <ns2:cancellationAllowed>false</ns2:cancellationAllowed>
              <ns2:violation>false</ns2:violation>
              <ns2:serviceDetails xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ns2:serviceDetailsAccommodation">
                <ns2:hotelId>8382794</ns2:hotelId>
                <ns2:hotelCode>SUL</ns2:hotelCode>
                <ns2:hotelName>Sultan Sands</ns2:hotelName>
                <ns2:countryId>26447</ns2:countryId>
                <ns2:countryName>Tanzania</ns2:countryName>
                <ns2:cityId>145428</ns2:cityId>
                <ns2:cityCode>145428</ns2:cityCode>
                <ns2:cityName>Zanzibar</ns2:cityName>
                <ns2:addressLine>Kiwengwa Beach, Zanzibar, 00000, Tanzania</ns2:addressLine>
                <ns2:category>4</ns2:category>
                <ns2:checkInFrom>12:00</ns2:checkInFrom>
                <ns2:checkOutTo>12:00</ns2:checkOutTo>
                <ns2:visaServiceSupportStatus>UNSUPPORTED</ns2:visaServiceSupportStatus>
                <ns2:rooms>
                  <ns2:roomId>5923533</ns2:roomId>
                  <ns2:roomTypeCode>Other</ns2:roomTypeCode>
                  <ns2:roomTypeName>Pwani Room</ns2:roomTypeName>
                  <ns2:mealTypeCode>(HB) HALF BOARD</ns2:mealTypeCode>
                  <ns2:mealTypeName>Half Board</ns2:mealTypeName>
                  <ns2:travelerIds>
                    <ns2:travelerId>5923531</ns2:travelerId>
                  </ns2:travelerIds>
                  <ns2:onExtraBed>false</ns2:onExtraBed>
                  <ns2:onWithoutPlace>false</ns2:onWithoutPlace>
                </ns2:rooms>
                <ns2:ownAccommodationInfo>
                  <ns2:serviceId>2052122</ns2:serviceId>
                  <ns2:tariffId>2052127</ns2:tariffId>
                  <ns2:tariffName>Standard</ns2:tariffName>
                  <ns2:mealTypeId>2052124</ns2:mealTypeId>
                  <ns2:categoryId>2052120</ns2:categoryId>
                  <ns2:categoryName>Standard</ns2:categoryName>
                </ns2:ownAccommodationInfo>
                <ns2:cardGuarantee>false</ns2:cardGuarantee>
              </ns2:serviceDetails>
              <ns2:taxesAndFeesIncluded>false</ns2:taxesAndFeesIncluded>
              <ns2:customerPaymentStatus>NO_BILL</ns2:customerPaymentStatus>
              <ns2:supplierPaymentStatus>NO_BILL</ns2:supplierPaymentStatus>
            </ns2:lines>
          </ns2:serviceTable>
        </ns2:order>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>

- JSON

<!-- -->

    {
     "order":
     {
       "orderId":9413,
       "title":"",
       "created":"2022-11-15T10:14:09+02:00",
       "modified":"2022-11-15T10:14:24.900+02:00",
       "status":"IN_PROGRESS",
       "agent":{
           "id":1716351,
        "prefix":"Mr",
        "firstName":"Hanz",
        "lastName":"Mueller"
       },
       "manager":{
        "id":1716351,
        "prefix":"Mr",
        "firstName":"Hanz",
        "lastName":"Mueller"
     },
     "agentCompanyId":1711626,
     "clientId":5923157,
     "clientType":"DirectSales",
     "clientCompanyName":"",
     "clientPerson":{
         "id":5923157,
         "prefix":"Mr",
         "firstName":"Tom",
         "lastName":"Boris"
     },
     "active":true,
     "customerPaymentStatus":"NO_BILL",
     "supplierPaymentStatus":"NO_BILL",
     "serviceTable":{
         "lines":{
             "serviceId":1005138,
             "serviceType":"accommodation",
             "created":"2022-11-15T10:14:22.778+02:00",
             "modified":"2022-11-15T10:14:23.512+02:00",
             "status":"CONFIRMATION_PENDING",
             "paymentMethodId":3842036,
             "supplierId":2051972,
             "supplierCompanyName":"Sultan Sands",
             "supplierCode":"company.2051972",
             "parentTO1Id":1711626,
             "refNum":"",
             "startDateTime":"2022-12-13T12:00:00+02:00",
             "endDateTime":"2022-12-14T12:00:00+02:00",
             "serviceGroupId":0,
             "travelers":{
                 "travelerId":5923158,
                 "isTourLead":true,
                 "travelerType":"Adult",
                 "isChild":false,
                 "citizenshipId":6880,
                 "citizenshipName":"Germany",
                 "prefix":"Mr",
                 "name":{
                    "firstName":"Tom",
                    "middleName":"",
                    "lastName":"Boris",
                    "sentToSupplier":true
                 },
                 "mealType":"Half Board",
                 "onExtraBed":false,
                 "onWithoutPlace":false
             },
             "salesTerms":[
                 {
                     "type":"SUPPLIER",
                     "price":{
                         "currency":"EUR",
                         "amount":"90.00",
                         "commission":0,
                         "amountDue":"90.00"
                     },
                     "priceBreakDowns":{"date":"2022-12-13",
                     "weekDayNumber":2,
                     "weekDayName":"Tuesday",
                     "price":{
                          "currency":"EUR",
                          "amount":90
                     }
                 }
             },
             {
             "type":"CLIENT",
             "price":{
                 "currency":"EUR",
                 "amount":"90.00",
                 "commission":0,
                 "amountDue":"90.00",
                 "serviceFee":"0.00"
             },
             "priceBreakDowns":{
                 "date":"2022-12-13",
                 "weekDayNumber":2,
                 "weekDayName":"Tuesday",
                 "price":{
                     "currency":"EUR",
                     "amount":90,
                     "serviceFeeAmount":0
                 }
             }
         }
     ],
     "modificationAllowed":false,
     "cancellationAllowed":false,
     "violation":false,
     "serviceDetails":{
         "@type":"serviceDetailsAccommodation",
         "hotelId":8382794,
         "hotelCode":"SUL",
         "hotelName":"Sultan Sands",
         "countryId":26447,
         "countryName":"Tanzania",
         "cityId":145428,
         "cityCode":145428,
         "cityName":"Zanzibar",
         "addressLine":"Kiwengwa Beach, Zanzibar, 00000, Tanzania",
         "category":4,
         "checkInFrom":"12:00",
         "checkOutTo":"12:00",
         "visaServiceSupportStatus":"UNSUPPORTED",
         "rooms":{
             "roomId":5923160,
             "roomTypeCode":"Other",
             "roomTypeName":"Baobab Room",
             "mealTypeCode":"(HB) HALF BOARD",
             "mealTypeName":"Half Board",
             "travelerIds":{
                 "travelerId":5923158
             },
             "onExtraBed":false,
             "onWithoutPlace":false
         },
         "ownAccommodationInfo":{
             "serviceId":5868363,
             "tariffId":5868398,
             "tariffName":"Standard",
             "mealTypeId":5868367,
             "categoryId":5868360,
             "categoryName":"Standard"
         },
         "cardGuarantee":false
         },
         "taxesAndFeesIncluded":false,
         "customerPaymentStatus":"NO_BILL",
         "supplierPaymentStatus":"NO_BILL"
         }
     }
      }
    }
