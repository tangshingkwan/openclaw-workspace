# Workforce Management

*Source: Cegid Retail Y2 – Version 26 | Extracted: 2026-02-27*

---

# Workforce Management

## Staff Discount and Clothing Allowance

### Contents

Staff Discount and Clothing Allowance - Contents

The objective of this module is to manage the non-standard price lists of certain customers, as illustrated in the following examples:
- Clothing: certain categories of staff may be entitled to clothing from store stock up to a specific amount.
- VIP: Certain categories of staff (or customers) may purchase items based on a different price list from the consumer price list (consumer price list – 50%, purchase price + 15%, special price.)

Example 1:
- 2 purchases with a 30% or 50% discount, depending on the brand
- 6 months seniority required

Example 2:
- Staff allowance for store staff only, with 2 to 3 outfits approved by the regional manager on the basis of a specific discount code.
- Staff purchases: Maximum of 1,500 euros per year, with a 30% discount

Example 3:
- Staff allowance:: 100% discount per item season, with 10 items permitted per specific item category
- Staff purchases: 50% discount with a maximum amount per season
- Executive management allowance : 100% discount with various limits
- VIP allowance: 100% discount with various limits

Staff discount and clothing allowance settings
- Serialization
- Program categories
- Access rights
- User restrictions

Special condition programs
- Characteristics tab
- Pricing tab
- Controls tab

Customer information
- Defining employees as customers
- Viewing program and history
- Viewing the list of programs per customer
- Creating/Closing programs in batch mode
- Importing customers with allowances

Using special conditions at checkout
- Sales transactions with special conditions
- Changing a customer in a receipt with special conditions
- Item returns with special conditions
- Modifying the discount origin

Special features in Clothing type programs
- Supplementary management of allowances - clothing

### Required Settings

Staff Discount and Clothing Allowance Settings

Serialization of the module

Back Office > Administration > Company > Company settings

The Staff Discount & Clothing Allowance module must be serialized before it can be used.

This will automatically activate the company setting Clothing allowance special conditions , available in the Administration > Distribution branch.

Program categories

Back Office > Sales > Clothing allowances > Categories

Customers may be linked to several programs of special conditions. For example, they can benefit from a Clothing program and an Employee program. You will then need to create program categories. Such as:
- Sales to employees
- VIP sales
- Clothing sales
- Player programs

Access rights

Back Office > Administration > Users and access > Access right management

Select the Concepts (26) menu, and then the Commercial management submenu. In the Clothing allowances section you can authorize or prohibit staff use of the following options:
- Use of programs of level 1
- Use of programs of level 2
- Use of programs of level 3
- Associate program to customer
- Customize customer amounts

Returns against allowances are possible without using a return control feature if the Manual entry of an allowance return is enabled in the Sales receipts menu (107).

User restrictions

Back Office > Administration > Users and Access > Users > Restrictions tab

The Restriction categories for clothing allowances enables you to limit access to allowance programs to certain users.

Users have access to all allowances by default if no restrictions have been set.

### Special Condition Programs

Special Condition Programs

Back Office > Sales > Clothing allowances > Special conditions

This screen allows you to create or view special pricing condition programs. Each program corresponds to a category of customers who share the same pricing conditions.

Characteristics tab

Click the [New] button to create a program, then enter the required information.

![Figure 859](./images/img_0859.png)

| Field | Description |
| --- | --- |
| Category | Select one of the program categories set in the previous step. |
| Closed | Allows you to disable a special condition. |
| Application stores | List of the stores that can use the program. You can select the stores directly, or use a grouping of user-defined store tables. |
| Clothing | Allows you to specify that the item is supplied as clothing. Selecting this type of condition allows you to carry out a check on sales. “Clothing” refers to any item that must be returned by the employee after use. |
| Number of preservation days | Entering a number of days here allows you to set up a predefined alert. This alert will highlight all items that must be returned on a certain date. |
| Validity: from... to... | Date when validity of the condition starts and ends. This date range must be specified to enable the annual renewal process. |
| Exclusion- from …to …: | Allows you to deactivate the program during certain periods (e.g. during sales). |
| One-day only | Allows you to apply a special one-day only condition with sales based on the agreed conditions. Several receipts can be entered, provided that they all apply to the same sales day. This special condition can be used only once. It is disabled after use. |
| Renewal | Yearly Totals are systematically calculated by calendar year. The customer total is reset to 0 at the start of each year if the validity date is real (i.e. if it is not 01/01/1900-12/31/2099). This date reset process is carried out automatically when using the program. Example: For a validity from 01/01/2009 to 12/31/2009 with annual renewal: totals are reset to zero for purchases made from 01/01/2010. Please note! You must absolutely enter the first day of the year in the programs for special conditions and clothing with annual renewal in order to initialize them for the new year. None Only the periods configured above are taken into account. |

Pricing tab

| Field | Description |
| --- | --- |
| Special price list | The search for the price of the item included in this program is carried out in the specified price list you have selected: The search is carried out for the store price list, as well as for the special condition price list. The most favorable of the two price lists is applied. If a special price list has not been defined for the item being sold, the price is taken from the store price list. The item will not be included in the program. |
| Applying discounts | The item is eligible for special conditions under this program based on the item type: Grouping and values: Allows you to select a group of items (item categories, item price list categories, user-defined item tables). Coefficient: Percentage of the price to be applied to items following previous categories. For example, to apply a discount of 30%, the corresponding coefficient would be 0.7. Discount reason: Relates to the new price of the item. Maximum quantity: Defines the maximum number of items that can be sold in the grouping. To disregard this, enter a value of 0 in this field. The conditions are applied in sequential order, until the sales line comes under the specified category. It is therefore important to categorize these three lines in the order desired. Example: Discount 1: 30% discount on the 2009 Summer collection Discount 2: 40% discount on all collections In this example, a 30% discount is applied to an item from the 2009 Summer collection, even if the discount in the second option is more favorable. |
| Application to promotional price lists | Application to promotional price lists: supposing that an item with a store price of €100 benefits from the following conditions: Promotional/sale discount of 50% Special condition discount of 40% The following prices are systematically searched for and calculated: Base consumer price: €100 Current consumer price: € 50 If the above information has not been checked : A search will be done on the store’s base price list, so that special conditions can be applied. This price is compared with the public price list, along with any applicable store promotions. The best price is applied; the discount reason is the reason associated with the selected price. The line will not be marked “special condition” unless the condition is used. Base price of €100 - 50% sales discount = €50 Base price of €100 - 40% special condition discount = €60 The item is invoiced for €50 (best price) and is not included in the program. If the above field is checked: The discount will be applied to the store’s retail price, along with any applicable promotions. Base price of €100 - 50% sales discount = €50 - 40% special condition discount = €30 The item will be invoiced for €30 and included in the program. |
| Application to items w/o price list | If this option is checked, the price entered during the sale will become the base price to calculate the allocation. |
| Total on amounts | Tax excl./Tax incl.: Allows you to customize the totals for country-specific pricing. For example: Taxes excluded for USA, All taxes included for France. |
| Currency | Currency: A program is managed in one currency only. Only stores that use this currency can be attached to this allocation program. |
| Payment methods | Allows you to select the payment methods permitted for payment of purchases that are eligible for special condition discounts. For example, it is standard practice to request payment by means of a check drawn in the employee’s name. Please notice: If several payment methods are configured for a standard sales receipt and a sales receipt associated with payment conditions, the most restrictive condition applies. |
| Tax free | Allows you to specify whether the allocations are subject to sales tax. |

Controls tab

Conditions

| Field | Description |
| --- | --- |
| Alert on period | If this threshold is exceeded, a message will appear on the screen signaling the exceeded threshold, and an event will be sent to the event log. |
| Maximum on period | Cannot be exceeded. The item in question must be sold at the public price, or based on another special condition. Note: The turnover total in each program corresponds to the price of the store (converted if applicable) the special condition applies to. This total only includes receipt lines that are eligible for a special condition discount. |
| “AND” Option | Double-click for alerts and maximum thresholds : Option checked: The threshold is considered to be exceeded if both amounts are exceeded. Option not checked: The threshold is considered to be exceeded if at least one of the two amounts is exceeded. If you do not want these fields taken into account, enter a value of 0. |
| Log | Occurrences of the threshold being exceeded can be logged by all programs. This field can be configured to prevent unnecessary alerts from being written to the log. |
| Total of amounts after allocation | This option allows you to specify the value that will be taken into account in the totals: The amount prior to applying the allocation (option not checked) The amount after applying the allocation (option checked) In this case, there will be no total available for rules that a 100% discount applies to. |

Securing

The following special options can be selected when entering a customer :

| Field | Description |
| --- | --- |
| Customer entry via reader is mandatory | Customer cards must be scanned to benefit from the program. The program cannot be used if the code is entered manually. |
| Open special conditions for checking | During program selection |
| Ask customer | A message will be displayed on the register to facilitate the identification process. Example: Ask for ID. |
| Authorization level for use | Authorization level for use: there are 3 authorization levels. The program may be viewed by everyone, but used by authorized staff only. Three options have therefore been added to the user rights to enable the use of these programs (please refer to Access Rights .) The default value for all programs is 0, i.e. the program can be used by everyone. |

### Customer Management and Special Conditions

Customer Management and Special Conditions

Defining employees as customers

Back Office > Basic data > Store staff > Store staff

Every employee benefiting from special condition is stored in the information system in the same way as a customer. This type of “customer” belongs to special conditions programs.

You can use this button to create associated customer records when creating sales representatives. Once the customer record has been created, it will be shown in sales representative records.

![Figure 860](./images/img_0860.png)

The customer code displayed in sales representative records will be grayed out once the first sale covered by a clothing allocation program has been made for this customer/sales representative.

Please note!

If a deletion date other than the default date of 12/31/2099 is entered in the salesperson record associated with the customer record, the allowance program will be automatically closed (regardless of the various dates associated with the program.) An alert is then proposed for validation and verification whether the user closing the salesperson's record has the rights to act on the special conditions.

Viewing program and history

Back Office > Basic data > Customers > Customers > Conditions tab

Viewing programs in customer records

A Special Conditions field has been added to the Conditions tab of customer records to allow you to view a list of the special conditions for each customer.

Click this button to access the list of special conditions the customer is affiliated to, or link the customer to a program, if necessary.

![Figure 861](./images/img_0861.png)

Please note that the user must have the necessary rights to create this link (please refer to Access Rights ).

Access Rights

A customer may be affiliated to several programs: the number of programs the customer is linked to will be displayed in the Special Conditions field.

After opening a customer program, several actions may be done:
- Close: the program will no longer be available to the customer, even if the application period is still valid.
- Customize amounts: amounts can be customized for customers. In this case, amounts are retrieved directly from the record, and not from the program. If you check this option, amounts, alert quantities and maximum quantities can be modified for this customer.

Note:
- This action may be done only by a user belonging to a group for which the corresponding concept has been enabled (please refer to Access Rights ).
- This modification can also add an event to the log.

Viewing program history in customer records

Click this button, then open a special condition associated to the customer.

![Figure 862](./images/img_0862.png)

In the Outstanding section, each time a customer makes a purchase the fields are updated in the program and provide an overview of customer history. If the alert amount is exceeded, the layout of the fields will be changed: Total on period and Balance on period will be displayed in red.

If a special condition is applied at the register and another discount is entered manually, the total will not take this discount into account.

Example: If the special condition suggests a price of €25.00, and the cashier enters a discount of 10%, the total will be incremented by €25.00, and not by €22.50 (€25.00 - 10%).

Viewing list of programs per customer

Back Office > Sales > Allocations/clothing - List of programs per customer

This command displays the list of all the customers linked to a program.

A double-click on a line gives you access to all the information available from the customer record as seen before. It gives direct access to customers associated to a particular program.

Creating/Closing programs in batch mode

Back Office > Sales > Allocations/clothing > Batch association

This command enables you to perform batch operations such as creating or closing programs. Please note that these two actions are saved in the event log.

Batch creation

This option allows you to quickly create associations between a program of special conditions and a set of customer records.

To do this, simply select the customers to be processed using the keyboard space bar and click this button.

![Figure 863](./images/img_0863.png)

The Special conditions to use window displays where you can select the programs to associate with these customers. Once the selection validated, the application displays a report about the processing.

Batch closing

This option allows you to quickly deactivate associations among special condition records. This operation is the same as ticking the “Close” checkbox in the special conditions customer record (Conditions tab in the customer record), The process is similar to batch creation.

Importing customers with allocations

The customer import format contains the $$_DOTATION fields, allowing you to associate customers to one or more allocation programs. When import file elements are added to the list of fields, the $$_DOTATION field will be incremented as follows: $$_DOTATION 1, $$_DOTATION 2, etc.

### Using Special Conditions at Checkout

Using Special Conditions at Checkout

Front Office > Sales receipts > Sales > Enter transaction

Sales transactions with special conditions

Assigning one or more special conditions to customers

A customer arrives at the register and presents identification to the salesperson. If the customer is eligible for just one special condition, and this condition is still active, a message is displayed for the salesperson informing that the customer is entitled to a special condition.

The salesperson can accept this special condition, which is then applied to each sales line.

It is also possible to reject the condition, in which case this special condition is not applied to any receipt line.

If the customer is linked to a number of different special condition programs, a screen is displayed where the salesperson can select the special condition to apply to the current sale.

Please note that it is also possible to ignore any special condition.

Changing a special condition associated to a line

The special condition is applied directly to the sales line. It is handled in the same way as a discount entered by the salesperson. A markdown reason as defined in the program is allocated too.

The [Actions on lines/Change special condition] button available in the toolbar in Front Office, allows you to change the special condition for selected sales lines.

![Figure 864](./images/img_0864.png)

The line amount is then totaled in the new program, after the maximum amount has been checked.

Please note: the special condition selected at the top of the receipt will still be applied by default to the next sales line.

Exceeding the maximum authorized amount

When validating the sales receipt, if the alert amount is exceeded, a message informs the salesperson that the customer has reached the alert threshold and the discount is applied.

#### Changing a customer in a receipt with special conditions

When creating receipts
- The sales receipt has special conditions. Lines have already been entered on the receipt for a customer eligible for special conditions. It is not possible to modify the customer, and a message informs the salesperson if there is an attempt to modify the customer. To change the customer, you need to delete the lines first, or cancel the receipt.
- The sales receipt has no special conditions. Lines have already been entered on the receipt without special conditions. The new customer is associated with the receipt. It is the responsibility of the salesperson to re-allocate each line to a special condition. The condition that was selected when changing the customer is applied to all lines entered after allocation of the customer.

After receipt validation

Once validated, a receipt with special conditions cannot be allocated to another customer. In this case, the following steps must be carried out:
- Cancel the receipt
- Create a new receipt associated with a different customer

Item returns with special conditions

A sale with a special condition program can be returned in a store. There are two possible cases:
- If the return has been done on the basis of the original sale, the item is returned under the terms of the special condition. The return will reduce the total that is saved in the program for the customer, in the same way as when a receipt is canceled. If the original line cannot be found, the return cannot be carried out against the allocation. In this case, the return must be carried out without any checks.
- If returns are managed without verification, the special condition must be added manually to the return line by clicking the [Actions on lines/Change special condition] button in the toolbar. You can do this only if the special condition is still valid at the time of the return. Otherwise, the return line cannot benefit from the allowance, and the total will not be reduced as a result of the return.

Returns against allowances are possible without using a return control feature if the Manual entry of an allowance return is enabled (please refer to Access Rights ).

Access Rights

### Supplementary Allowance - Clothing Management

Supplementary Allowance - Clothing Management

Compared with special conditions management, there are a number of additional steps involved in managing clothing programs.

Check the number of preservation days setting

Back Office > Sales > Clothing allowances > Special conditions

There is an option linked to clothing (Characteristics tab) that determines the number of days clothes will be kept. If this number of preservation days is set to 0, the clothing alert will be disabled and the return date will not be calculated.

View clothing list

Back Office > Sales > Clothing allowances > Clothing

This command lets you view all clothing, with selection criteria to obtain the following lists:
- List of clothing for a specific customer
- List of pending returns
- List of clothing already returned

Mark clothing as returned

Back Office > Sales > Clothing allowances > Clothing

Double-click on the relevant line to open the desired clothing record.

The Returned clothing checkbox allows you to mark the item as returned (or discarded).

You can use the comment field to add a special comment, such as the reason why the item is not returned, for example.

More about “Clothing” type sales operations

A specific process will start up when a “clothing” sale is made. When the sale is validated, a field will be added to a new table to allow access to the following information:
- Sales information: all sales line information is available (date, store, register, cashier, customer, item, quantity, etc.)
- Estimated return date: calculated on the number of days of preservation set in the program.

## In Store Planning Management

### In Store Optimisation

#### Contents

Staff Management in Stores - Contents

The Schedule module is used to enter for every store, every day and every employee a forecasted schedule. This schedule can be viewed by the Headquarters according to the access rights granted. With the theoretical schedule being defined, the staff can use a timeclock feature to register the real attendance times of the staff. This allows management to compare the forecasted schedule with the actual one and generate alerts in case of anomalies. It is possible to connect the module with an entry counter system enabling the calculation of the sales transformation rate. The combined use of such a system and the schedule management enables the implementation of controls aimed at creating a system to facilitate the diagnostic assessment of poor performance in stores.

General settings of the schedule
- Company settings
- Configuring stores
- Defining settings for employees
- Managing access rights

Specific settings of the schedule
- Setting up activity ranges
- Setting up schedule templates
- Setting up special events

Forecasted schedule management
- Entering one or more forecasted ranges
- Modifying a forecasted range
- Adding an employee from another store
- Displaying schedule information
- Duplicating a schedule
- Printing a schedule from its entry screen
- Miscellaneous actions on the schedule

Approval management for schedules
- Required settings
- Asking for approval
- Validating visas

Realized schedule management (or activity follow-up)
- Entering the activity on a one-by-one basis
- Entering the activity at register closing
- Entering the activity on a global basis

Time clock management
- Timeclock management

Analyses and alerts linked to the staff's activity
- Analyses and reports
- Schedule alerts

Exporting schedules to Cegid Paie
- Export types
- Selecting the export format
- Exporting schedules

#### General Settings of the Schedule

Specific Settings of the Schedule

Defining company settings

Back Office : Administration – Company – Company Settings – Link to .Next modules >HR Optimisation

Depending on the desired operation mode, populate the fields described here and validate.

described here

Configuring stores

Back-Office > Basic data > Stores > Stores

Procedure
1. Select and open a Store record and go to tab Store staff.
2. Check checkbox Activate management of forecasted schedule .
3. If you want to handle visas on schedules, tick the Activate visa management c heckbox.
4. Define the various timeslots for the store in order to define daytime and night-time hours. This information is mandatory if you determine your payroll results according to the exported schedules in order to respect differences in wages for day and night shifts.
5. Specify the hours for a standard day. This is mandatory if you want to manage resources in half-days, in order to define the hours for a half-day in your store.
6. Specify the Daily average cost of your store. This daily average cost is used to calculate the profitability of stores for the “Profitability of stores” report
7. The Link to payroll field is used to specify the export characteristics for the schedule. For further information on the export of a schedule and its characteristics to specify, please refer to chapter Export the schedule to Cegid Paie.

Defining settings for employees

Back-Office > Basic data > Store staff > Store staff

In an employee record, the Contract tab gathers all information relevant for the employee's contract, which may have an impact on how to manage schedule and activity. In addition to some general data (address, employee code...,) this record is used to specify the following:
- The employee's position
- His/her contract type
- If the employee works part-time: working hours are limited to 35 hours per week. In this case, when you define the schedule and if this threshold is exceeded, an alert will inform you that this employee cannot work more than 35 hours a week.
- The number of working hours per week.
- The maximum number of weekly hours: when you define the schedule and if the threshold specified in this field is exceeded, an alert will inform you that the employee's contract states XX hours per week.
- The starting date of the contract and its end date. The display of the employee on the schedule do take into account these dates. The employee will not appear on the schedule before and after the period defined, but within this date range.
- The stores where the employee can work: this is very useful if you have to replace another employee usually working in the store. This option is also used if the employee usually works in several stores.

Note that it is possible to define the position of each employee (manager, salesperson...) and his/her contract type (part-time job, full-time job...)

These two lists can be customized if you click on the [Subtable settings] button, located next to these selection lists or via the following commands:

![Figure 865](./images/img_0865.png)
- Settings > Store staff > Positions
- Settings > Store staff > Contract type

Access rights management

Back Office > Administration > Users and access > Access right management

Concepts (26) > Commercial management > Management of the store staff

| Concept | Description |
| --- | --- |
| Access to sales representatives' contracts | Authorize or forbid the access to tab Contract of the employee’s record by clicking the [Add employee] button available in Schedule entry or Activity reporting (refer to Adding an Employee from Another Store .) - If the user is authorized, he has access to the entire record, and especially to the Contract tab. If not, the user can access the record, but the Contract tab is not accessible. |
| Authorize the modification of schedules | Authorize or prohibit the creation of schedules for the staff members of one or more stores. If the user is authorized, he can modify the schedules. If not, the right-click on the schedule is not active and no change can be made. |
| Apply forecasted hours on realized hours | Authorize or forbid the ability to apply when entering activities, the forecasted hours on the realized ones (refer to Entering Realized Hours .) If the user is authorized, the [Automatically apply forecasted hours on realized hours] button is available and copies forecasted hours to realized ones. If not, the button is made inaccessible, forcing the user to enter the realized hours. |
| Viewing the objective on the schedule | Authorize or prohibit the display of the objective if the latter has been configured to be displayed on the schedule (refer to Setting Up Schedule Templates - Analytical Information .) - If authorization is granted, the daily objective is displayed on the schedule. If not, this information is not displayed. |
| Viewing the sales figures on the schedule | Authorize or forbid the user to view the sales figures on the schedule, if the sales figures have been configured to appear on the schedule (refer to Setting Up Schedule Templates - Analytical Information .) If authorization is granted, the sales figures are displayed on the schedule. If not, this information is not displayed. |
| Authorize modification of ranges after export | Authorize or prohibit the modification of schedules after their export. Just remind: Schedules are entered and/or modified in Back-Office, in module Store staff, menu Enter, command Schedule (right-click on the range). Schedules are exported from Back Office, in module Data exchanges, menu Data export, command Export schedules. - If the user is granted authorization, and after the exports of the schedules, the user can modify them by right-clicking on the range to modify. If not, the right-click to modify the range is not operating. |
| Print schedule | Authorize or forbid the user to print the forecasted schedules (refer to Printing the Forecasted Schedule .) - If the user is granted authorization, the user can use this button to print the schedule. If the right is denied, and the user tries to print the schedule, a message will inform the user that he is not authorized to perform this operation. |
| Export schedule to Excel | Authorize or prohibit the export of the schedule (refer to Export the schedule to Excel (refer to Exporting the schedule to Excel .) - If the user is granted authorization, the user can use the [Excel] button to export the schedule. If the right is denied, and the user tries to export the schedule, a message will inform the user that he is not authorized to perform this operation. |
| Force registration | In the store, the clock-in/clock-out management is used to handle the activity times of the salespeople. The manager of the store may sometimes force this control, for example, if one of the staff members has forgotten to clock in or to clock out (refer to Timeclock Management . ) |
| Initialization of passwords | Authorize or forbid the user to create a password in the sales representative's record. We are talking about the creation of a password and not about its change. Moreover, the employee must not have had a password before. The main access is given by the [Confidentiality - Initialize password] from the employee’s record. This gives access to the Initialize password window. If the user is granted authorization, the button [Confidentiality - Initialize password] is available and enables the initialization of the employee’s password. If not, the "Initialize password" option is not accessible and the password cannot be created. |
| Authorize the modification of schedules after approval | Authorize or prohibit the modification of schedules after their approval by visa (refer to Validating Visas .) If the user is granted authorization, he can modify schedules via a right-click on the appropriate range, even if a visa has been granted. If not, the right-click to modify the range is not operating. |

Store staff (104)

The commands impacted by these rights are located in Back Office, in module Store staff and especially in menus Enter, Settings, and Analysis. In these menus:
- If the user is authorized, he can use the commands concerned without restriction.
- If not, the command concerned is hidden, and the user has no access to the feature.

Settings (105) > Store staff

These access rights directly impact the sales employees' records. Just to remind, these records are set up in module Settings, menu Store staff. So, this is aimed at granting or not access rights to some user groups to enable them to manage the employees' settings, in particular: User-defined titles, User-defined tables, Business areas, Positions, Contract types, Password strategy, and Badges.

#### Specific Settings of the Schedule

Specific Settings of the Schedule

Setting up activity ranges

Back-Office > Store staff > Settings > Ranges

This screen is used to define the various ranges required to determine the schedules:
- Periods of attendance, such as presence in the store, in the stockroom, training, etc.
- Periods of absence, such as holidays, breaks, etc.
- Other: if you select this type of range you will be able to manage quantitative elements and not hours as it is the case for absence and attendance. You can then manage luncheon voucher or packed lunch allowances granted to the employee, and calculated based on the hours worked.

The essential fields of the Ranges record are explained hereafter:

| Fields | Description |
| --- | --- |
| Range type | This field is used to define whether the hours of the range are accounted for worked hours. For example, this will be the case for an Attendance period, but not for an Absence period or a range type "Other" |
| Payroll heading | You have to fill in this field if you want to export the schedules. For further information on the export of schedules, please refer to chapter Export the schedule to Cegid Paie. |
| Restriction categories | You can also add restrictions on the ranges defined. These restrictions are defined in module Administration, menu Users and access, command User restrictions > Restriction categories. You can then define the Scope of use relating to the Store staff. On the schedule, you can then view the ranges that do not pertain to the restriction categories of the user; but you cannot change, duplicate or delete them. These restrictions can be implemented in the Schedule, Schedule duplication, and Activity reporting menus. For further information on restriction categories, please refer to the documentation about user restrictions. |
| Management in days and half-days | In order to facilitate the management of holidays and additional days off, you can activate the "Management in days" and "Management of half-days" checkboxes in order to account for the ranges specified in days or those specified in half-days rather than in hours. This type of management is not available for Attendance periods. |
| Accessible via activity input | This option is used to define if this type of range can be directly entered via the activity follow-up as this feature is used to manage the realized schedule. |
| Graphical representation of ranges | For a better visual reading, you can define graphical elements for ranges by defining the background color, the text color and the font style. All these graphical elements will help you to recognize easily a forecasted range from a realized one. |

Setting up schedule templates

Back Office > Store staff > Settings > Templates

This screen is used to define the various graphical representations of the schedules.

Characteristics tab

| Fields | Description |
| --- | --- |
| Default schedule | The schedule template will open by default. |
| Active | The active templates will be available for the creation of the schedule. |
| Frequency | Is used to define the display scale of the schedule (day, hour, quarter of an hour, and half an hour.) |
| Display format | Is used to define the display format of the hours on the schedule. The user has to set up a format that is consistent with the other settings. |
| Starting time - End time | Defines the display time range of the schedule. If this information is not filled in, the current opening hours for the store will be automatically recovered for entry. |
| Viewing range | Specifies if the schedule will be displayed for the week or the month. |
| Refreshing | Determines the refreshing frequency of the schedule. |
| Height of data lines / Width of data columns: | Defines the dimensions of the schedule |
| Graphic shape | Determines the shape of the graphical representation for ranges on the schedule. |
| Contents of the shape | Is used to set up the information that appears within the range. |
| Tooltip contents | Is used to set up the information that appears in the tooltip relating to the range. |
| Order and sorting | Is used to define the order in which employees appear on the schedule and allows the user to make groupings, if need be. |

Layout tab

| Fields | Description |
| --- | --- |
| Header of fixed column | Is used to define any information about employees that appears on the schedule (last name, first name, position, etc.) The user can define up to 6 columns. Before you select a column to display, specify in field "Left fixed column" the number of columns on the left you want to display on the schedule. The fields available in this tab are recovered from other records (contract, employee, etc.) The Contract field will display on the schedule, the number of weekly hours as defined in the staff member's record. The Total field will display on the schedule, the forecasted total (absence, attendance, but not ranges of type "Other".) The Work field will display the worked hours on the schedule. |
| Layout | Is used to define the colors for the background of the schedule and for the selections made, as well as for the days of the week. |

Analytical information tab

This tab is used to display the sales figures and the attendance of the previous week, as well as the week's objective; the user can also select the graphical display template. This data will be displayed in the bottom part of the schedule when the latter is entered, in the colors defined in the settings.

| Fields | Description |
| --- | --- |
| Display objective | Tick this option if you want to display the objective on the schedule. Objectives must have been activated first in the company settings, via Commercial management/Default settings. Objectives are set up in Front Office: module Sales Receipts, menu Sales, command Store goals |
| Display comment | Tick this option if you want to display, when entering the schedule, an entry field for a user-defined text associated with the store/week. |
| Display sales figures | When entering a schedule, this is used to view the tax included or tax excluded sales figures over the period selected. |
| Display attendance | When entering a schedule, this is used to view the attendance over the period selected. Therefore, you have to establish a connection with an entry counter system. |
| Display of totals | This display is available only for schedules in hours and days. When entering a schedule, this enables the user to view totals per timeslot and per employee. Note that this button gives you a direct preview of the current setup. |

Setting up special events

Back Office > Store staff > Settings > Schedules

This setup is not mandatory, but if you want you can create special events such as bank holidays, flea market, sales periods, etc., and display them on the schedule. These special events must be created first on the schedule and then be associated with one or more store records via the Store staff tab.

Once these operations carried out, these events are automatically displayed on the schedules of the stores concerned.

#### Forecasted Schedule Management

Forecasted Schedule Management

Back Office and Front Office > Store staff > Enter > Schedule

Please note that all the entries done via the Schedule command will save a schedule described as Forecasted.

The so-called Realized schedule can also be viewed using the Schedule command (but in this case, the realized ranges are displayed in the colors defined in chapter Graphical Representation of Ranges ); their management will be performed in the Activity Follow-up .

Graphical Representation of Ranges

Activity Follow-up

As soon as you click the Schedule command, you are prompted to specify a date and a store. The list of the stores proposed for selection takes into account the default restrictions defined, as well as the activation of the schedule management for these stores. Each tab of the schedule corresponds to a template defined. Therefore, it is very easy to navigate via the various existing representations.

Entering one or more forecasted ranges

Creating a forecasted range

To create a range, you just have to drag the mouse over the desired timeslot for the selected employee and right-click on the mouse and select option Creation. Then, select in the screen that appears the type of range to create. Dates and hours are recovered automatically, and the system calculates the duration. If the selected range type is managed in days, then the relevant field calculating the corresponding number of days will appear. If you want to support half-days, please refer to chapter Setting up Activity Ranges (field “Management in days and half days”.)

Setting up Activity Ranges

Creating several forecasted ranges

You can enter several ranges at once. Therefore, you have to activate the Multirange entry option in the company settings. To perform a multirange entry, you just have to drag the mouse over the desired timeslot for the selected employee and right-click on the mouse and select option Multirange entry. On the entry screen that displays, you can then enter several ranges for the same staff member.

Multirange entry

The [New] button located in the upper left part of the screen enables the creation of a new range for the staff member without leaving the screen.

![Figure 866](./images/img_0866.png)

Use the [Delete] button to delete the range.

![Figure 867](./images/img_0867.png)

Modifying a forecasted range

To modify a created range, you just have to position the mouse on the start time or end time of the range in order to display a double arrow.

Then, you can drag this arrow with your mouse and move the range, reduce or increase it, or duplicate it. You can also right-click with your mouse on the range to display a drop-down menu which allows you to modify or delete the range. If the range has a multirange type, right-click with your mouse and select Multirange entry to make changes to one of the existent ranges.

Adding an employee from another store

Timeslots are assigned to employees that do exist in the database and are linked to the store. However, you can add to the schedule employees that are working in other stores. Therefore, you can either:
- List in the employee's record (tab Contract, field "List of additional stores") the stores where the employee may be working, or
- Use this button when entering the schedule to select the sales representatives to display on this schedule. Please note that this feature enables you to access the employee’s record, even tab Contract. If you want to hide the Contract tab since it contains confidential data, please refer to chapter Access to the Sales Representatives' Contracts .

Displaying information on the schedule

Displaying information as a decision-making aid

To help the user in establishing schedules, certain information can be directly displayed on the schedule:
- Sales figures for N-1
- Attendance N-1
- Sales objective of the day
- The total worked hours takes into account the ranges for which the checkbox Total worked hours is activated (refer to Setting up Ranges )
- A comment

The display of this information depends on the settings defined in the schedule templates (refer to Analytical Information Tab ), and on the following access rights granted: Viewing the objective on the schedule and Viewing the sales figures on the schedule.

Analytical Information Tab

Please note, if the sales figures are displayed in a graphical shape on the schedule, the hours displayed are comprised in the range from H to H +59 minutes. For example, the displayed range goes from 06:00 PM to 06:59 PM. To display the sales figures save at 07:00 PM to the database, you must display the schedule until 08:00 PM.

Displaying a comment on the schedule

It is possible to display a text field for the week that will also appear on the Schedule report. This comment can be displayed permanently or on demand:
- Display the comment permanently: in order to display this text field permanently, you have to activate option Display comment available in the schedule template (please refer to the Analytical Information Tab .) Once this option activated, the user can enter information in the comment text field which appears permanently in the middle of schedule screen.
- Display the comment on demand: If you want this comment be available on demand, no specific setup is necessary. The [Display comment] button is available on the schedule and opens the text field dedicated to the comment. This button is available only if the previous option is not activated.

The comment field is a user-defined text entry field located in the lower part of the screen. You can delete or validate your comments with the following buttons:
- Erase the comment
- Validate the comment

Duplicating a schedule

To avoid unnecessary entries, the user can duplicate a schedule using the [Duplicate] button. This feature enables:

![Figure 868](./images/img_0868.png)
- The duplication of several weeks at once
- The duplication of an employee’s schedule to several other employees
- The duplication of the selected ranges
- The deletion of the original schedule after the duplication (used to manage temporary employees via a standard employee)

Note that the schedule can also be duplicated outside the Schedule command. You can use the “Schedule duplication” command available in the Store staff module, Enter menu.

Focus on the Schedule duplication window

Once you have specified the information described below, validate to start the duplication.

| Fields | Description |
| --- | --- |
| Store | Select a store. Note that in Front Office, the store of the cash register is specified by default. |
| Original schedule | Specify the week or the day to copy. |
| Target schedule | Specify the period to supply. |
| Initial salespeople | If you want to duplicate all salespeople, then checkmark option All salespeople. If you want to carry out a one-by-one duplication, then select option By salesperson. You then have to select the initial salesperson and the target salesperson in the window that displays in the right part of the screen. The Cut/Paste option enables the deletion of the original schedule after the duplication. Column Selection is used to check the salespeople that will be duplicated. In any case, a click on the salesperson's line is enough to select or deselect that employee. Please note that it is possible to integrate employees from other stores by checkmarking the relevant option. |
| Original range | All ranges: all ranges of the original schedule will be copied. Per range: allows you to select the ranges to duplicate. |

Printing a schedule from its entry screen

The features described hereafter offer the possibility to print the forecasted and/or realized schedule from the Schedule command. If you prefer to print a Forecasted/Realized comparison, rather use the Schedule report command, available in menu Analysis.

Printing the forecasted schedule

For legal reasons, the forecasted schedule must be printed and displayed in the stores. A graphical representation and a graphical edition of the store schedule are available via the [Print] button on the schedule entry screen. If visa management is activated, the following notices: Awaiting validation, Validated or Not validated may appear on the printout.

Note!

The printing of the schedule is subject to the Print schedule access right.

Moreover, its advisable to tick the “Color printing” option in the Miscellaneous tab of the User record (Administration > Users and Access > Users.)

Printing the realized schedule

Use the [Print realized] button to print the realized schedule.

Miscellaneous actions on the schedule

Moving through the schedule

Use the arrow buttons to move from one week to the other, or from one day to the other.

Going back to the selection screen of the date and the store

The [Access to schedule] button enables you with one click to select a new date and a new store.

![Figure 869](./images/img_0869.png)

Entering holidays

The employees' holidays can be directly entered onto the schedule by specifying a range of type Absence.

In no way these elements are subject to controls or locks (concerning the number of remaining holidays, for example.)

Resetting a period

The [Reset a period] button rests the data of the schedule. A screen displays to select the period and the employee to reset.

![Figure 870](./images/img_0870.png)

Note!

Only non validated forecasted periods can be erased.

Displaying the caption

Click the [Caption] button to display the caption of the elements used in the schedule The caption will use the colors and the fonts defined in the settings of the range (refer to the Graphical Representation of Ranges .)

![Figure 871](./images/img_0871.png)

Graphical Representation of Ranges

Refreshing the schedule

Use the [Refresh] button to update the schedule based on the data entered into the database (especially if several users manage the same schedule.) By default, the schedule is updated automatically according to the settings defined in the schedule template, tab Characteristics.

![Figure 872](./images/img_0872.png)

Export schedule to Excel

Use the [Excel] button to export the schedule. The export path must have been specified first in the company settings (refer to Export of Schedules .)

![Figure 873](./images/img_0873.png)

Note!

The export of the schedule is subject to the Export Schedule to Excel access right.

Export Schedule to Excel

Duplicating a schedule from its entry screen

To accelerate the entry of the schedule you can duplicate it via the [Duplicate] button.

![Figure 874](./images/img_0874.png)

#### Approval Management for Schedules

Approval Management for Schedules

Required settings

Forecasted schedules may require a visa. The use of a visa may be permanent or subject to compliance coefficients. In the case where the visa management is supported, the schedule specified in the store must be approved by the Headquarters.

Activating visa management

Back Office > Basic data > Stores > Stores

The visa management is activated in the store record via the Store staff tab.

Setting up visa status

Back Office > Store staff > Settings > Visas

A visa may have 3 different statuses: Awaiting validation, Validated or Not validated. The wording and the graphical representation of these 3 statuses can be redefined at your convenience.

Asking for approval

Requesting a visa when entering a forecasted schedule

Back Office and Front Office > Store staff > Enter > Schedule

When a forecasted schedule is entered in the store, the system automatically applies status Awaiting validation to the schedule.

This button sends the request for approval to the Headquarters. The manager can then validate or not the proposed schedule, from the Back Office via module Store staff, menu Enter, command Visas.

![Figure 875](./images/img_0875.png)

The manager can use the notepad to comment his decision.

If a schedule does not get approval, any new change to the schedule makes the visa status change to “Awaiting validation.” However, it is also possible to prohibit any change on the schedule using the Access Rights granted.

Access Rights

Requesting several visas for schedules

Back Office: > Store staff > Enter > Request for visa

This screen is used to request several visas over a period of several weeks.

Please!

No visa can be requested for weeks having no ranges or for weeks with a pending visa request.

Validating visas

Back Office > Store staff > Enter > Visas

Select on the screen that displays the lines you want to validate and click the [Launch process] button. Then, select the status you want to apply to the selected visas.

![Figure 876](./images/img_0876.png)

The status allocated can be modified, if need be, by repeating the operation with a new status.

Prohibiting the modification of an approved schedule

By default the modification of an approved schedule is authorized. However, if you want to forbid any modification of the schedule after it has been approved, you have to prohibit access right Authorize the Modification of Schedules after Approval .

Authorize the Modification of Schedules after Approval

#### Realized Schedule Management (Activity Follow-up)

Realized Schedule Management (Activity Follow-up)

The activity follow-up is aimed at specifying very accurately the hours worked by the staff. This is no longer the management of a forecasted schedule, but the management of the realized schedule. This later allows the user to compare the initially forecasted attendance with the actual attendance, justify possible gaps, and if need be, send the hours of attendance to a payroll system. The attendance time can be entered in two different ways:

worked
- A simple entry at daily register closing on a global or one-by-one basis
- The use of a timeclock system.

Entering the activity on a one-by-one basis

Back Office and Front Office > Store staff > Enter > Activity reporting

This feature is used to enter realized hours in deferred time at register closing. The principle is to enter for each forecasted range the actual realized hours. The total of forecasted hours, of realized hours, and the gap are calculated automatically upon entry, and refreshed in the header of the screen. First of all, you have to select the day and the store. The screen is divided as follows:

realized hours
- The upper part of the screen called header grid displays for each staff member the forecasted sign-in and sign-out times.
- The lower part of the screen, called detail grid is used to enter the actual worked hours of each staff member.

To enter the activity times of each staff member, select the employee in the header grid. The detail grid then displays information linked to the forecasted activity of the employee selected: type of activity, the forecasted start and end times, as well as the total estimated time.

of the employee selected:

Entering realized hours

If the realized hours do match the forecasted hours and if you have been granted the appropriate access rights (refer to Apply Forecasted Hours on Realized Hours ,) you can use this button to initialize automatically the realized hours with the forecasted hours. This automatic process avoids any unnecessary entry if the realized hours do match the forecasted hours.

![Figure 877](./images/img_0877.png)

and

Apply Forecasted Hours on Realized Hours

You do not have these rights or if the forecasted information does not match the actual hours, you can enter the realized time in the relevant blank fields: activity type, considered start and end times. The considered time will be calculated automatically.

or

Please note that you can also enter:
- A realized activity that was not forecasted
- An absence in the activity follow-up, if it as has been defined as Accessible via activity input.

Repeat this operation for all the employees displayed in the header grid.

Miscellaneous actions

When activity is entered on a one-by-one basis, you may perform several actions:

Specify the reasons for gaps

If there is a gap between the forecasted and the realized times, or between a forecasted range and a realized one, and if the entry of the reason for the gap is mandatory (refer to the Company Settings, Entry of a Justification ) a screen will display at validation where you can specify the reason of the gap.

and

Company Settings, Entry of a Justification

Non justified gaps will display this button.

![Figure 878](./images/img_0878.png)

You can also use this button to enter or change the gap justification for the selected line.

![Figure 879](./images/img_0879.png)

Delete an activity line

If you want to delete an activity line after it has been saved, just go back to the concerned day and position the cursor on the line to delete. Then blank out the whole line and validate: the record of this activity is deleted. In the case where this activity line is linked to a timeclock operation, the latter can be modified again: its status has changed from blocked to modifiable.

Add an employee

Use this button to add an employee who is not on the list.

![Figure 880](./images/img_0880.png)

Entering activity at register closing

Front Office: Sales receipts > Daily operations > Closing

This feature allows you to enter the realized schedule at register closing. To be able to use this feature, you must have activated first the "Enter times at the end of the day” option, available in:

realized schedule
- Back Office > Settings > Front Office > Register > Register record > Daily operations tab
- Front Office > Settings > Registers > Registers > Register record > Daily operations tab

Then, at register closing, after having entered the day's events, a new window displays where you can enter the activity. By default, the current date and the store linked to the cash register are displayed.

The entry procedure for the activity is the same as the procedure detailed in the previous chapter “Enter the activity on a one-by-one basis.” Please refer to it if need be.

Entering the activity on a global basis

Back Office and Front Office: Store staff > Enter > Global entry of activity

This global entry allows you to validate the schedule and the staff clock-in/clock-out over a given period for a group of employees. The lines that are displayed show for each employee the totals for the forecasted, checked and considered times over the selected period.

The "Validated time" criterion is used to filter data according to the elements already validated or not.

Moreover, if timeclock management is enabled:
- The Gap between forecasted and checked superior or equal to xxx hours criterion is available to select the activity according the gap entered in hours. Otherwise, this criterion is hidden. Note that this criterion is not taken into account if a value is specified in field Hours.
- The Consider forecasted time (instead of checked time) criterion must be checkmarked if you want to use the forecasted times instead of the checked times. If you have not activated timeclock management, this criterion is hidden because in this case forecasted times are always taken into account.

From the global entry screen you can enter information such as "Considered start" and Considered end" for each range to make adjustments compared to the schedule or the timeclock feature.

Note if you support timeclock management and the rounding of clocked in/out hours, rounding for these hours will be applied in this screen.

and

For further information about this rounding of hours, please refer to the documentation about Timeclock Feature for Salespeople .

Timeclock Feature for Salespeople

#### Timeclock Feature for Salespeople - Contents

Timeclock Feature for Salespeople - Contents

In the stores, timeclock management is used to handle the activity times of the salespeople.

This feature is subject to the serialization of the following module: In store HR Optimisation for Back and Front Office

The feature may work even if the schedule management is not enabled. For further information about schedule management and activity input, please refer to HRO - In Store Optimisation - Store staff .

HRO - In Store Optimisation - Store staff

If timeclock management is associated with authentication, it will allow you to manage the salespeople's activity based on the configured work ranges.

For further information about the salespeople authentication, refer to section Authenticating Salespeople.

Timeclock settings
- Enabling timeclock management
- Configuring the stores impacted
- Setting up activity ranges
- Limiting the list of salespeople to the people who clocked in
- Configuring an alert on non clocked out users
- Managing access rights

How the feature works in Front Office
- Arrival and departure dates
- Controls performed during timeclock operations
- Daily opening and closing of the register
- Modify time

Analyses and alerts
- Analyses on salespeople's attendance
- Alert on non clocked-out users

Standalone mode and restrictions
- Timeclock operations in standalone mode
- Restrictions linked to timeclock operations

#### Analyses and Alerts Linked to the Staff's Activity

Analyses and Alerts Linked to the Staff's Activity

Analyses and reports

Back Office and Front Office > Store staff > Analysis
- Edit schedule: This report displays the forecasted schedules, the initial ones (supplied by the employees' timeclock operations) or the considered ones (or realized ones if timeclock management is not supported) according to the stores and the date range selected.
- Edit transformation rates: This report states per store and for each salesperson, the number of sales made according the attendance rate.
- Profitability of stores: This report gives you an overview of the total sales, the margin obtained, the number of salespeople, etc., as compared to the average operating cost of the store. This average cost is an element entered into the store record (see Configuring stores .)
- Evolution for sales figures and attendance: This report shows in the shape of a curve, the evolution of the sales figures and the attendance. To get an idea of the attendance rate, you have to establish a connection with an entry counter system.
- Attendance of salespeople: This report is usable only if you support timeclock management for the staff (see Timeclock Feature for Salespeople .) According to the criteria specified, you will get information about the employees' attendance, or a history.

Schedule alerts

Back-Office > Administration > Alert management > Settings

Various controls generating alerts can be implemented for the entry of a schedule:

Alerts on non entered schedules
- CEG-PLANNINGPREV - Forecasted schedule week W+2 not entered: Lists the stores that have not entered their schedule W+2 (legal obligation).
- CEG-PLANNINGREA - Realized schedule D-1 not entered: Lists the stores that have not entered their realized schedule for the previous day.

Alerts on gap justifications
- CEG-JUSTIFECART: Lists the activities that are different from those forecasted, per store and employee, as well as the comment entered to justify the gap.
- CEG-POINTAGEFORCE: List of forced clock-ins
- CEG-RETARDCOLLAB: List of employees who are late to work. You can define the number of minutes from which you want to take into account the delay.
- CEG-RETARDCOLLABO: Same alert as the previous one, but for Oracle versions.

Configurable alerts

Non-exhaustive list of alerts that can be configured:
- Alert listing the employees who have not clocked-in and are present on the forecasted schedule.
- Alert showing the days without a forecasted schedule (ex: date rolling over the next 15 days)
- Alert showing the schedules validated or not.
- Alert on controls on worked hours.
- Alert on recoverable hours not supported in the payroll system that lists the remaining hours to recover. There is an example of 2 range types (hsr and hre) that are the range types associated with the recoverable hours and the hours to recover. The name of the alert is: CEG-HEURESRECUP.

#### Exporting Schedules to Cegid Paie

Exporting Schedules to Cegid Paie

The export of the schedule to a payroll system is explained hereafter. However, a more detailed description of the feature is available; please refer to the documentation about Import/export to Cegid Paie.

Export types

Three types of exports are available:

Standard data export of the schedule (customizable format)

Back Office > Data exchanges > Data export > Export schedules

This export is used to extract data relating to schedules. These exports may supply a payroll system.

Export without the "HR Activity and attendance" module of the payroll application

This export directly works with Cegid Paie but without the "Activity and attendance" module. The feature exports totals per heading without additional calculation:
- The number of luncheon vouchers
- The number of vacation days
- The number of worked hours
- Etc.

It is possible to manage overtime hours and additional hours with extra allowances with 3 possible thresholds.

Export with the "HR Activity and attendance" of the payroll application

This export is used in the case where the number of worked hours per week is not known or if the payroll rules are complex.

The export via the "Activity and attendance" module works together with the Cegid Paie HR module "Activity and attendance". All the calculations of overtime hours and additional hours with extra allowances are performed according to the rules defined in the "Activity and attendance" module.

Selecting the export format

Back Office > Settings > Stores > Link to payroll

The export format is chosen for each store.

| If the number of worked hours is: | You will assign: |
| --- | --- |
| < number of contract hours | worked hours to the heading. |
| < (contract hours + 10% (threshold 1 for part-time) | the number of contract hours to the heading of threshold 1 for part-time. |
| > contract hours + 10% (threshold 1 for part-time) and worked hours < threshold 2 for part-time | the number of contract hours to the heading of worked hours, and all the rest to the heading of threshold 2 for part-time (no allocation based on percentages for these two headings.) |

Please notice if the number of worked hours for part-time exceeds the number of hours of threshold 2, the contract is automatically redefined as full-time.

Definition of timeslots

The definition of the hours for the beginning of the afternoon is used to differentiate the morning and the afternoon for the export of absences. This is why it is very important to define these timeslots in the store record, as described in chapter Configuring Stores .

Configuring Stores

Exporting schedules

Back Office > Data exchanges > Data export > Export schedules

The planned ranges for which a corresponding code is defined in the payroll are exported (forecasted ranges, realized activity, etc.)

This Heading code is defined in the range record. For further information, please refer to chapter Setting up activity ranges, in particular the Payroll heading field.

Payroll heading

Exported information

Three types of information can be exported, knowing that each range is associated with a payroll heading:
- Attendance (worked hours)
- Absence (holidays, additional days off, sickness)
- Other types managed in quantities (luncheon vouchers, packed lunch allowances, etc.)

In addition to ranges you can also export the following:
- Forecasted hours
- Worked hours
- Night hours
- Legal holidays

### Timeclock Feature for Salespeople

#### Contents

Timeclock Feature for Salespeople - Contents

In the stores, timeclock management is used to handle the activity times of the salespeople.

This feature is subject to the serialization of the following module: In store HR Optimisation for Back and Front Office

The feature may work even if the schedule management is not enabled. For further information about schedule management and activity input, please refer to HRO - In Store Optimisation - Store staff .

HRO - In Store Optimisation - Store staff

If timeclock management is associated with authentication, it will allow you to manage the salespeople's activity based on the configured work ranges.

For further information about the salespeople authentication, refer to section Authenticating Salespeople.

Timeclock settings
- Enabling timeclock management
- Configuring the stores impacted
- Setting up activity ranges
- Limiting the list of salespeople to the people who clocked in
- Configuring an alert on non clocked out users
- Managing access rights

How the feature works in Front Office
- Arrival and departure dates
- Controls performed during timeclock operations
- Daily opening and closing of the register
- Modify time

Analyses and alerts
- Analyses on salespeople's attendance
- Alert on non clocked-out users

Standalone mode and restrictions
- Timeclock operations in standalone mode
- Restrictions linked to timeclock operations

#### General Settings for Timeclock Feature

Settings for Timeclock Feature

Enabling the clock-in/clock-out management

Back Office > Administration > Company > Company Settings > Link to .Next modules > HR Optimisation

To enable the timeclock feature, tick the Clock in/out management checkbox. The following options are optional:

| Fields | Description |
| --- | --- |
| Automatic clock-out when closing register | If you check this option, if sales staff have not checked out before leaving the store, they will do so when the last open register closes. Once the salesperson who closes this register has manually clocked out, all the other salespeople will be clocked out automatically. A list of these salespeople will then appear on the screen. |
| Number of hours beyond... | Specify the maximum number of hours the operator is authorized to work before he is clocked out automatically. If you specify 4, this means that the salesperson is automatically clocked out 4 hours after he has clocked in. When the salesperson clocks in again, the following message will display: "You clocked in more than 4 hours ago. You were disconnected automatically”. The salesperson then validates the message to clock in again. |
| Round clock-in / clock-out hours | If you want to implement the automatic handling of rounding, specify your options here. These values will be used automatically for the global entry of activity (refer to Store’s Staff Management ). |

Configuring the stores impacted

Back Office > Basic data > Stores > Stores

Timeclock operations can be managed at store level. Each store record must therefore be configured to determine whether or not the store supports this feature.

Open the record of the store for which you want to implement this feature, and go to the Store staff tab.

| Fields | Description |
| --- | --- |
| Activate clock-in/clock-out management | Tick this checkbox option to enable the timeclock feature in this store. |
| Authentication type | Select from the scrolling list, the identification method for the salesperson: Authentication with password only Authentication with badge only Authentication with password or badge Authentication with password and badge Authentication by selecting the salesperson Authentication via fingerprint Authentication via fingerprint or password For further information about the salespeople authentication, refer to section Authenticating Salespeople. |

Setting up activity ranges

Back Office > Store staff > Settings > Ranges

Setting up ranges for attendance or absence ranges allows you to refine the timeclock management.

Click on the [New] button to create a range. The Range record displays allowing you to create the creation of attendance and absence ranges.

![Figure 881](./images/img_0881.png)

Example:

| Fields | Description |
| --- | --- |
| Range and Description | Specify the range you want to create as well as its description. For example: Attendance in the store, Training, Attendance in the stockroom, Holidays, etc. |
| Range type | Select from this scrolling list if you want to create a range of type Attendance or Absence. |
| Restriction categories | If need be, specify a restriction category (refer to User Restrictions .) |
| Default type | Tick this checkbox option, if you want to propose this range first for the this clock-in/clock-out feature. |
| Sales area | Tick this checkbox option, if you want this rage account for the calculation of the sales capacity of items. |
| Settings for ranges (forecasted and realized) | The bottom part of the screen is used to configure the layout of the ranges (forecasted and realized) by specifying the background color, the text color and the font. |

Limiting the list of salespeople to the people who clocked in

Back Office > Settings > Front Office > Register > Preferences tab

A salesperson is effectively present if he clocked in. Upon sales receipt entry, when the dynamic touch pad of the salespeople displays, the number of salespeople can be limited to the salespeople present in the store.

To implement this display restriction, go to the Preferences tab of the register settings and tick the Only salespeople that have clocked in on the touch pad checkbox option. Then, the touch pad will only display the salespeople who effectively clocked in.

In a "multiple registers per store" environment, the list of salespeople is loaded into memory in order to optimize the display of the dynamic pad.

Please notice that the sales receipt entry screen allow the buttons of the present salespeople to be refreshed.

Therefore you must press the [Other actions] button and select the Update the touch pad of the present salespeople option.

![Figure 882](./images/img_0882.png)

Configuring an alert on non clocked-out users

Back Office > Settings > Front Office > Register > Daily operations tab

If you want to be notified about users who did not clock-out, tick the Alert on non-clocked out users checkbox option. These alerts can then be viewed in the Sales receipts > Daily operations > Daily brief, and from the register opening and closing screens.

Access rights management

Back Office > Administration > Users and access > Access right management

These access rights allow you to define the user groups that will be authorized or not to use functions linked to the timeclock feature.

Menu Concepts (26) > Commercial Management > Store Staff

Modify time

The manager of the store may sometimes force this control, for example, if one of the staff members has forgotten to clock in or to clock out. The commands impacted by these rights are located in Front Office:
- Sales receipts > Timeclock > Modify Time
- Store staff > Analysis > Attendance of salespeople: after having chosen Attendance history as analysis type, the buttons used to modify the clock-in or clock-out values are visible according to the access right granted or not.

Menu Sales receipts (107) > Timeclock

Clock-in

The command impacted by this right is located in Front Office > Sales receipts > Timeclock > Clock-in.
- If the user is granted authorization, he can use this function without restrictions.
- If not, the command is hidden.

Clock-out

The command impacted by this right is located in Front Office > Sales receipts > Timeclock > Clock-out.
- If the user is granted authorization, he can use this function without restrictions.
- If not, the command is hidden.

Modify time

The manager of the store may sometimes force this control, for example, if one of the staff members has forgotten to clock in or to clock out. The command impacted by this right is located in the Front Office > Sales receipts > Timeclock > Modify time.
- If the user is granted authorization, he can use this function without restrictions.
- If not, the command is hidden.

#### How the Feature Works in Front Office

How the Feature Works in Front Office

Arrival and departure data

The Clock-in function records the arrival of a salesperson; the clock-out function records the departure of the salesperson. Controls are based on the system date of the workstation. Clock-in/out times and dates cannot be modified buy the salespeople.

Please notice that a salesperson can connect to 2 stores, each of them remaining independent.

In the case the user is still considered present in another store, a non-blocking information message will be displayed.

The information required when clocking in or out depends on the settings defined for the authentication of salespeople.

Clock-in must be performed before the salesperson is authenticated; and a salesperson who is not considered present in the store cannot be authenticated.

before

On the sales receipt entry screen, for a faster use you can configure on the touch pad a button dedicated to the timeclock functions.

Clock-in

Front Office > Sales receipts > Timeclock > Clock-in

Front Office > Sales receipts > Sales > Enter transaction > button [Other actions/Clock-in]
1. Once the Clock-in window is displayed, the salesperson must identify.
2. The arrival time is the displayed, and cannot be modified.
3. He must then select the appropriate type of attendance.
4. You will find here the ranges defined previously: attendance in store, stockroom, training, etc.
5. After validation the salesperson is considered active.

Clock-out

Front Office >Sales receipts > Timeclock > Clock-out

Front Office > Sales receipts > Sales > Enter transaction > button [Other actions/Clock-out]
1. Once the Clock-out window is displayed, the salesperson must identify himself.
2. The departure time is the displayed as well as the attendance type selected when the salesperson had clocked in.
3. You cannot make any changes to these two elements.

Controls performed during timeclock operations

Salesperson has already clocked in

This refers to situations where the salesperson inadvertently clocks in twice:
- If a salesperson tries to clock in when he has already done so, the following message will appear: "You have already clocked in. You have to disconnect before you can clock in again.”
- If a salesperson tries to clock out again whereas he has already done so, the following message will appear: “You have already clocked out. You have to reconnect before you can clock out again.

Salesperson has clocked in to another store

If a salesperson is not clocking in to his main store (information contained in the salesperson's record, in the Identity tab), the following message will be displayed: “You are not clocking in to your main store, do you want to proceed?”

Attendance ignores the implemented controls

This refers to controls defined in the company settings. For further information about these controls, please refer to section Enabling Timeclock Management . This information is logged to the event log.

Enabling Timeclock Management

Salesperson clocks in to more than one store

In the case the user is still considered present in another store, a non-blocking information message will be displayed.

Daily opening and closing of the register

If the salesperson who opens or closes the register did not clock in, the following message will be displayed: “The salesperson did not clock in."

If this message is validated the Clock-in window will display so that the salesperson can clock in and proceed with the opening or closing of the register.

Notice the presence of the [Clock-in] and [Clock-out] buttons that are used to perform these operations in connected mode and in standalone mode.

Just remind: A company setting allows salespeople to be clocked out automatically when closing the register. You just have to tick the Automatic clock-out when closing register checkbox option in the company settings (refer to Enabling Timeclock Management .

Enabling Timeclock Management

Modify time

Front Office > Sales receipts > Timeclock > Modify Time

This functionality allows a manager to clock a sales person in or out, if this person has forgotten to do so.

On the Modify time window, specify the store and the salesperson, and then click on this button.

![Figure 883](./images/img_0883.png)

As appropriate, the message "Force departure" or Force arrival", as well as the range and the time will be displayed. Validate to record the activity.

#### Analyses and Alerts

Analyses and Alerts

Analyses on salespeople's attendance

Back Office and Front Office > Store staff - Analysis - Attendance of salespeople

According to the criteria specified, you will get information about the employees' attendance, or a history.

Attendance of salespeople

This function displays the list of the employees who have clocked in to a store, and are therefore theoretically present, together with the clock-in date and time. The attendance period is calculated when the clock-in and clock-out information is known.

Various icons are used to specify the attendance status and the clock-in/clock-out method. Select for the Attendance field option Present or Not present depending on what you want to view.

Attendance history

To get the history of timeclock operations in a store, select Attendance history for the Attendance field and specify a period.

Note that all timeclock operations for all store can be accessed via the Back Office. However, when viewing an individual store, this is limited to the timeclock operations for that store.

Alert on non clocked-out users

Front Office > Sales receipts > Daily operations - Opening/closing and Daily brief

If this alert has been enabled in the register settings (refer to Setting up an alert on non clocked out users ), the list of the non clocked out users is available via the following commands:

Setting up an alert on non clocked out users
- Daily opening and closing of the register,
- Daily brief

#### Timeclock Feature in Standalone Mode and Restrictions

Timeclock Feature in Standalone Mode and Restrictions

Timeclock operations in standalone mode

Timeclock operations are carried out transparently in standalone mode.

Please note!

When in standalone mode, a salesperson should clock in or out on only one register.

If, however, multiple clock-ins are performed, they can be corrected/deleted via the Attendance of salespeople.

Restrictions linked to timeclock operations

Register operations

In Front Office, salespeople who have not clocked in cannot perform the following tasks:
- Enter sales transactions
- Create documents that trigger inventory movements
- Open the register
- Close the register

Item returns

Please note!

If in the register settings, in the Management tab, the Recover salesperson from original receipt option is enabled, note that this option requires that the salesperson allocated to the return line is present in the store, that is to say he/she clocked in to the store.