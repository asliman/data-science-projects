# Donation Analysis
This program identify repeated donors.  
This program requires 'itcont.txt' and 'percentile.txt' in the 'input' folder.
The program output a file, 'repeated_donors.txt', into the 'output' folder.
Each line of this file should contain these fields:

- recipient of the contribution (or CMTE_ID from the input file)
- 5-digit zip code of the contributor (or the first five characters of the ZIP_CODE field from the input file)
- 4-digit year of the contribution
- running percentile of contributions received from repeat donors to a recipient streamed in so far for this zip code and calendar year. Percentile calculations should be rounded to the whole dollar (drop anything below $.50 and round anything from $.50 and up to the next dollar)
- total amount of contributions received by recipient from the contributor's zip code streamed in so far in this calendar year from repeat donors
- total number of transactions received by recipient from the contributor's zip code streamed in so far this calendar year from repeat donors

