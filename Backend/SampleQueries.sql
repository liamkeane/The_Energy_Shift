/*Sample queries for all functions in the API */

/* Replaces getEnergyForState() function in the API

Sums all electricity generation by all catagories in a given state
 */
SELECT SUM(
        january +
        february +
        march +
        april +
        may +
        june +
        july +
        august +
        september +
        october +
        november +
        december
    )
FROM colorado
WHERE categoryofproduction = 'All fuels';

/* Replaces getTotalRenewableEnergyByState() function in the API

Sums the total amount of renewable energy for the specified state
 */
SELECT SUM(
        january +
        february +
        march +
        april +
        may +
        june +
        july +
        august +
        september +
        october +
        november +
        december
    )
FROM colorado
WHERE categoryofproduction <> 'All fuels';

/* Replaces getTotalEnergyForStateByMonth() function in the API

Retrieves monthly total electricity generation throughout the year for a given state
*/
SELECT january,
        february,
        march,
        april,
        may,
        june,
        july,
        august,
        september,
        october,
        november,
        december
FROM colorado
WHERE categoryofproduction = 'All fuels';


/* Return the total renewable energy output amount for Wisconsin for each category of production
    the table 'colorado ' could be replaced by other table or user's input*/

SELECT categoryofproduction, 
        january +
        february +
        march +
        april +
        may +
        june +
        july +
        august +
        september +
        october +
        november +
        december 
        AS Amount
FROM colorado 
WHERE categoryofproduction != 'All fuels';

/* Alternative query that accomplishes the same thing (because a 'total' column is included) 
   Condensed onto one line for simplicity of string input */

SELECT categoryofproduction, total FROM colorado WHERE categoryofproduction != 'All fuels';