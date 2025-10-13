# USER MANUAL. TOUR OPERATOR. DIRECTOR

## **GPTE Technical Requirements**

## 1. Single Server Requirements

<table>
  <thead>
    <tr>
      <th></th>
      <th><strong>Live Server</strong></th>
      <th><strong>Test Server</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>CPU:</strong></td>
      <td>8 cores with HT, starting from 2.5 GHz</td>
      <td>8 cores with HT, starting from 2.5 GHz</td>
    </tr>
    <tr>
      <td><strong>RAM:</strong></td>
      <td>64-128 GB (more - better)</td>
      <td>32-64 GB</td>
    </tr>
    <tr>
      <td><strong>STORAGE:</strong></td>
      <td>1TB+ SSD NVMe Drive in RAID 1 1TB external for backups</td>
      <td>500GB+ SSD NVMe Drive in RAID 1</td>
    </tr>
    <tr>
      <td><strong>OS:</strong></td>
      <td>Ubuntu Server 24.04 x64 in min setup (only ssh server installed)</td>
      <td>Ubuntu Server 24.04 x64 in min setup (only ssh server installed)</td>
    </tr>
    <tr>
      <td><strong>CREDS:</strong></td>
      <td>- root password; * server IP-address; * domain name for installation</td>
      <td>- root password; * server IP-address; * domain name for installation</td>
    </tr>
  </tbody>
</table>

**Ideal Internet connection:** 100 Mb/sec at least. 1GB/sec is preferred.

**Supported Parameters:** Full performance of GP Travel Enterprise installed on a single server is guaranteed at ≤ 3,000 bookings per month at a look-to-book ratio of ≤ 500:1.

## 2. Multi-server Installation

In case Supported Parameters (for a single server) are exceeded, the system load may become too high for a standard single-server system configuration.

A multi-server installation and additional system configuration works might be required to support high system load. The scope of particular server/system configuration and such additional works will depend on various factors:

- The types of travel products sold
- The suppliers used
- The types of sales channels used
- Whether the high load comes from searches or bookings
- Peak load
- Other

Depending on these factors, our specialists evaluate the best way to optimize the system load on a case-by-case basis, which includes load-testing. Each multi-server installation is configured to fit a particular client's requirements.
