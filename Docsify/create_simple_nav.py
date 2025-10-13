#!/usr/bin/env python3
"""
Create a simplified MkDocs navigation with minimal nesting.
"""

from pathlib import Path
import yaml

def create_simple_nav():
    """Create a flat, user-friendly navigation structure."""

    nav = [
        {'Home': 'README.md'},
        {'Overview': 'overview/overview.md'},
        {'FAQ': 'faq/faq.md'},
    ]

    # User Manual section - flatten the structure
    user_manual = {
        'User Manual - Tour Operator': [
            {'Introduction': 'user-manual-tour-operator-director/gpte-introduction/gpte-introduction.md'},

            # Basic Functionality - flattened
            {'Analytics': 'user-manual-tour-operator-director/gpte-basic-functionality/analytics/analytics.md'},
            {'Dashboards': 'user-manual-tour-operator-director/gpte-basic-functionality/analytics/dashboards/dashboards.md'},
            {'Reports': 'user-manual-tour-operator-director/gpte-basic-functionality/analytics/some-examples-of-reports/some-examples-of-reports.md'},

            {'Company Profile': 'user-manual-tour-operator-director/gpte-basic-functionality/company-profile/company-profile.md'},
            {'Managing Users': 'user-manual-tour-operator-director/gpte-basic-functionality/company-profile/managing-company-users/managing-company-users.md'},
            {'User Roles': 'user-manual-tour-operator-director/gpte-basic-functionality/company-profile/managing-company-users/creating-new-user-profile/user-roles/user-roles.md'},
            {'Company Settings': 'user-manual-tour-operator-director/gpte-basic-functionality/company-profile/specifying-company-profile-settings/specifying-company-profile-settings.md'},

            {'Finance': 'user-manual-tour-operator-director/gpte-basic-functionality/finance/finance.md'},
            {'Invoices': 'user-manual-tour-operator-director/gpte-basic-functionality/finance/invoices/invoices.md'},
            {'Ledgers': 'user-manual-tour-operator-director/gpte-basic-functionality/finance/ledgers/ledgers.md'},
            {'Payment Settings': 'user-manual-tour-operator-director/gpte-basic-functionality/finance/payment-settings/payment-settings.md'},

            {'General Settings': 'user-manual-tour-operator-director/gpte-basic-functionality/general-settings/general-settings.md'},
            {'System Users': 'user-manual-tour-operator-director/gpte-basic-functionality/general-settings/managing-system-users/managing-system-users.md'},
            {'Templates': 'user-manual-tour-operator-director/gpte-basic-functionality/general-settings/templates/templates.md'},
            {'Notifications': 'user-manual-tour-operator-director/gpte-basic-functionality/general-settings/notifications/notifications.md'},

            {'Managing Clients': 'user-manual-tour-operator-director/gpte-basic-functionality/managing-clients-sales-settings/managing-clients-sales-settings.md'},
            {'Sales Settings': 'user-manual-tour-operator-director/gpte-basic-functionality/managing-clients-sales-settings/managing-sales-settings/managing-sales-settings.md'},
            {'Contracts': 'user-manual-tour-operator-director/gpte-basic-functionality/managing-clients-sales-settings/managing-sales-settings/managing-contracts/managing-contracts.md'},
            {'Markups & Commissions': 'user-manual-tour-operator-director/gpte-basic-functionality/managing-clients-sales-settings/managing-sales-settings/markups-and-commissions-settings/markups-and-commissions-settings.md'},

            {'Managing Suppliers': 'user-manual-tour-operator-director/gpte-basic-functionality/managing-suppliers-purchase-settings/managing-suppliers/managing-suppliers.md'},

            {'Reservations': 'user-manual-tour-operator-director/gpte-basic-functionality/reservations/reservations.md'},
            {'Searching Reservations': 'user-manual-tour-operator-director/gpte-basic-functionality/reservations/searching-for-reservations/searching-for-reservations.md'},
            {'Viewing & Editing': 'user-manual-tour-operator-director/gpte-basic-functionality/reservations/viewing-and-editing-reservations/viewing-and-editing-reservations.md'},

            {'Search & Book': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book.md'},
            {'Search Form': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-form/search-form.md'},
            {'Hotels': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-accommodation/search-book-of-accommodation.md'},
            {'Flights': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-flights/search-book-of-flights.md'},
            {'Trains': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-trains/search-book-of-trains/search-book-of-trains.md'},
            {'Transfers': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-transfers/search-book-of-transfers.md'},
            {'Activities': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-activities/search-book-of-activities.md'},
            {'Tours': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-tours/search-book-of-tours.md'},
            {'Visas': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-visas/search-book-of-visas.md'},
            {'Insurance': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-insurances/search-book-of-insurances.md'},
            {'Car Rentals': 'user-manual-tour-operator-director/gpte-basic-functionality/search-book/search-book-of-car-rent-services/search-book-of-car-rent-services.md'},

            {'Self-Operated Products': 'user-manual-tour-operator-director/gpte-basic-functionality/creating-self-operated-products/creating-self-operated-products.md'},
        ]
    }

    # Extended Functionality - grouped logically
    extended_manual = {
        'Extended Features': [
            {'Packaging': 'user-manual-tour-operator-director/gpte-extended-functionality/packaging/packaging.md'},
            {'Dynamic Packages': 'user-manual-tour-operator-director/gpte-extended-functionality/packaging/search-book-of-dynamic-packages/search-book-of-dynamic-packages.md'},

            {'Extended CRM': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-crm/extended-crm.md'},
            {'Loyalty Programs': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-crm/loyalty/loyalty.md'},
            {'Feedback & Reviews': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-crm/feedback-and-reviews/feedback-and-reviews.md'},

            {'Extended Company Structure': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-company-structure/extended-company-structure.md'},
            {'Multi-Level Distribution': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-company-structure/multi-level-distribution/multi-level-distribution.md'},
            {'Managing Agencies': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-company-structure/managing-agencies-clients/managing-agencies-clients.md'},

            {'Corporate Sales': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-corporate-sales/extended-corporate-sales.md'},
            {'Corporate Policy': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-corporate-sales/corporate-policy/corporate-policy.md'},
            {'Approvals': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-corporate-sales/approvals/approvals.md'},

            {'Service Teams': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-management-of-reservations/managing-service-teams/managing-service-teams.md'},

            {'Hotel Mappings': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-search-book-capabilities/mappings-of-hotels/mappings-of-hotels.md'},
            {'Flight Extensions': 'user-manual-tour-operator-director/gpte-extended-functionality/extended-search-book-capabilities/extended-flights-search-book/extended-flights-search-book.md'},

            {'Business Intelligence': 'user-manual-tour-operator-director/gpte-extended-functionality/business-intelligence/business-intelligence.md'},
            {'Channel Manager': 'user-manual-tour-operator-director/gpte-extended-functionality/channel-manager/channel-manager.md'},
            {'CRM Integration': 'user-manual-tour-operator-director/gpte-extended-functionality/integration-with-crm-systems/integration-with-crm-systems.md'},
            {'VOIP Integration': 'user-manual-tour-operator-director/gpte-extended-functionality/voip-integration/voip-integration.md'},
            {'Seat Map': 'user-manual-tour-operator-director/gpte-extended-functionality/seat-map/seat-map.md'},
            {'Trip Assistant': 'user-manual-tour-operator-director/gpte-extended-functionality/trip-assistant/trip-assistant.md'},
            {'Add-ons': 'user-manual-tour-operator-director/gpte-extended-functionality/extensions/add-ons/add-ons.md'},
        ]
    }

    # CMS Guide - simplified
    cms_guide = {
        'CMS User Guide': [
            {'Overview': 'user-guide-cms/user-guide-cms.md'},
            {'Accessing Admin Panel': 'user-guide-cms/accessing-the-admin-panel/accessing-the-admin-panel.md'},
            {'Collection Types': 'user-guide-cms/collection-types/collection-types.md'},
            {'Blogs': 'user-guide-cms/collection-types/blogs/blogs.md'},
            {'Destinations': 'user-guide-cms/collection-types/destinations/destinations.md'},
            {'Hotels': 'user-guide-cms/collection-types/hotels/hotels.md'},
            {'Info Pages': 'user-guide-cms/collection-types/infopages/infopages.md'},
            {'Single Types': 'user-guide-cms/single-types/single-types.md'},
            {'Creating Content': 'user-guide-cms/creating-saving-publishing-and-deleting-content/creating-saving-publishing-and-deleting-content.md'},
        ]
    }

    nav.append(user_manual)
    nav.append(extended_manual)
    nav.append(cms_guide)
    nav.append({'Support Tickets': 'support-tickets-instructions/support-tickets-instructions.md'})

    return nav

def main():
    script_dir = Path(__file__).parent
    mkdocs_file = script_dir / 'mkdocs.yml'

    # Read existing config
    with open(mkdocs_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Replace nav
    config['nav'] = create_simple_nav()

    # Write back
    with open(mkdocs_file, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print("=" * 60)
    print("Navigation Simplified!")
    print("=" * 60)
    print("Changes:")
    print("  - Removed redundant nested titles")
    print("  - Flattened hierarchy (max 2 levels)")
    print("  - Cleaned up section names")
    print("  - Fixed directory index issues")
    print()
    print("Next: Run 'mkdocs serve' to see the changes")
    print("=" * 60)

if __name__ == '__main__':
    main()
