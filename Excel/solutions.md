# Solutions for Public TestDome Excel Questions

Note: Didn't add the Excel files to the repo. I don't know if there are any problems or security concerns to doing so. In researching whether you can mix Git and Excel, I discovered [xltrail](https://www.xltrail.com/), which offers version control for Excel workbooks.

## Tax Inclusive

Formulas needed are `=B10 + (B10 * $A$5)` and `=B10 + (B10 * $B$5)`.

## Order Discounts

To calculate the discount rate use `=VLOOKUP(B5, Discounts!A:B, 2, TRUE)`. To calculate the order amount with discount, use `=B5-(B5*D5)`.

## Time Filters

For Sheet 1, you need to click on the date column and add a filter using the `is between` condition.  Add the dates, and that's enough. For Sheet 2, you use the same dates of 6/30/2018 and 8/31/2018 and add a filter using the `is not between` condition.

## Performance Reviews

Using Google Sheets, you don't really need to do much to generate the first pivot table, as the condition needed (Sum of Total for each Employee by Category) should be available from the initial displayed options. To make the second pivot table, you need to add Employee to Column, CompanyId and Category to Rows, and Total to Values.

## Sales Comparison

I don't think a 100% score is possible for this challenge using Google Sheets. Google Sheets doesn't have a specific "clustered column chart" option under its standard chart types. If you select all the data first and then insert a chart, it will appear rendered as a clustered column chart. You need to set the horizontal axis title to blank, as you cannot delete the horizontal axis title property. Because the property still exists in the chart's metadata (guessing), you will not pass the horizontal title requirement. The checker does seem to check property conditions. Leaving an auto setting for the legend does have the chart display correctly, but the TestDome test will fail. The range for the vertical axis is also a problem. Setting the range as 200-280 in Google Sheets means that all the ticks will not show. The minor ticks will be missing. If you set the range to 200-270, every tick will show a number increased by 10. Since the checker looks for 280, I don't think this requirement is passable. The tick step and count options are limited, and I wasn't willing to invest more time in experimenting to get the whole range's numbers to display. I did set the ticks to display outside to match the picture, but I don't know if the checker actually cares or if something else is affecting this test. I could never get past 60% for a Google Sheets chart.
