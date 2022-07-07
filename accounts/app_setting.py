USER_TYPE = (('admin', 'admin'),
             ('client', 'client'),
             ('sales_man', 'Sales Man'),
             ('partner','Partner'),
             ('agent', 'Agent'),
             ('store manager', 'Store Manager'),
             ('accounts', 'Accounts'),
             ('hr','Human resources'),
             ('su','Super User'),
             ('new_joined','New Joined'),
             ('consulter','Consulter'),
             ('researcher','Researcher'),
             )

STATUS_TYPE = (('Approved', 'Approved'),
               ('Submitted', 'Submitted'),)

PRODUCT_CHOICE = (
    ('consumable', 'Consumable'),
    ('sale_only', 'Sale Only'),
    ('raw_material', 'Raw Material'),
    ('sales_and_raw', 'Sales and Raw'),
)



PRODUCT_QUOTATION_STATUS = (
    ('draft', 'Draft'),
    ('approved', 'Approved'),
    ('email_sent', 'Email Sent'),
    ('deleted', 'Cancelled'),
    ('submitted' , 'Submitted')
)

PRODUCT_ORDER_STATUS = (
    ('payment_done', 'Payment Done'),
    ('payment_pending', 'Payment Pending'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
    ('submitted' , 'Submitted'),
    ('approved', 'Approved'),
)

COMPANY_TYPE = (
    ('kaata', 'Kaata'),
    ('client', 'Client'),
    ('vendor', 'Vendor'),
    ('mine', 'Mine'),
    ('crusher', 'Crusher'),
    ('minecrusher', 'Mine&Crusher'),
    ('contractor', 'Contractor'),
    ('transporter', 'Transporter'),
    ('individual', 'Individual'),
    ('properitor', 'Properitor'),
    ('partner', 'Partner'),
    ('llp', 'LLP'),
    ('pvt_ltd', 'PVT LTD'),
    ('ltd', 'LTD'),
)

PROJECT_STATUS = (
    ('on_hold', 'On Hold'),
    ('on_going', 'On Going'),
    ('completed', 'Completed'),
)

PRODUCT_TYPE = (
    ('type_a', 'Type-A'),
    ('type_b', 'Type-B'),
)

DEVICE_TYPE = (
        ('android', 'android'),
        ('ios', 'ios'),
    )


LEAD_STATUS = (
    ('initial_lead', 'Initial Lead'),
    ('inactive', 'Inactive'),
    ('converted', 'Converted'),
)


ADDRESS_TYPE = (
    ('shipping', 'Shipping'),
    ('billing', 'Billing'),
)

INVENTORY_TYPE = (
    ('in', 'IN'),
    ('out', 'Out'),
)

INVOICE_REQUEST_STATUS = (
    ('approved', 'Approved'),
    ('denied', 'Denied'),
    ('pending', 'Pending'),
    ('created', 'Created'),
    ('closed','Closed'),
)

PRODUCT_REQ_STATUS = (
    ('approved', 'Approved'),
    ('deleted', 'Deleted'),
    ('pending' , 'Pending'),
    ('completed', 'Completed')
)

FULFILMENT_STATUS = (
    ('delivered', 'Delivered'),
    ('partially_delivered', 'Partially Delivered'),
    ('work_in_progress', 'Work In Progress'),
    ('dispatched','Dispatched'),
)


SALES_CATEGORY_TYPE = (
    ('mine', 'Mine'),
    ('crusher', 'Crusher'),
    ('distributer', 'Distributer,1'),
    ('nhai', 'NHAI,1'),
    ('precast', 'Precast,1'),
    ('real_estate','Real Estate,1'),
    ('rmc','RMC,1'),
    ('supplier','Supplier,1'),
    ('stp','STP,1'),
    ('water_treatment_htp','Water Treatment & HTP,1'),
    ('infra_projects','Infra Projects,1'),
    ('retail','Retail,1'),
    ('metro','Metro,1'),
    ('pwd','PWD,1')
)

TRIGGER_TYPE = (
    ('customer', 'Customer'),
    ('quotation', 'Quotation'),
    ('order', 'Order'),
    ('lead', 'Lead'),
)

QUERY_STATUS_CHOICES = (
    ('submitted', 'Submitted'),
    ('Closed', 'Closed'),
    ('acknowledged', 'Acknowledged'),
    ('reopen', 'Reopen'),
)


BLODD_GROUP_CHOICE = (
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

GENDER_TYPES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)