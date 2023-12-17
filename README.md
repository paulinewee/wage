# What the Tech?

An Overview of Global Tech Salaries

by Pauline Wee for Data Bootcamp Fall 2023

### Overview

How does tech worker compensation vary across roles, companies, and countries? To find out, I looked at three datasets of tech salaries from the US, India, and Argentina from Kaggle. I individually cleaned and analyzed the datasets for relevant insights about pay.

### Data Source and Cleaning

I initially planned to scrape Glassdoor or Indeed to get a more recent set of salaries, but due to hostile anti-scraping mechanisms implemented on both sites, I opted to stick with three datasets that I found on the dataset aggregator Kaggle.

US and Europe Dataset (2016)

[https://www.kaggle.com/datasets/thedevastator/know-your-worth-tech-salaries-in-2016](https://www.kaggle.com/datasets/thedevastator/know-your-worth-tech-salaries-in-2016)

This dataset compiled by Brandon Telle has data from a Hacker News survey of user salaries in the tech industry in 2016, providing detailed job titles, experience years, geographical locations, annual benefits, and signing and stock bonuses from employers. Many are US-based, but several are also from Europe. I cleaned the dataset to remove spam entries, junk entries, and poorly or inconsistently formatted fields.

India Dataset (2020)

[https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022](https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022)

This dataset contained a large amount of tech salaries from cities and companies in India, created by Sourav Banerjee from Glassdoor India. The dataset poster noted that the IT industry accounted for 8% of India's GDP in 2020, with a revenue estimated at US Dollars 194 billion in FY 2021 and a total of around 4.5 million people employed as of March 2021. I renamed header fields and expanded rows marked with “Number of Salaries Reported” so that each reported salary would have its own entry, allowing for easier comparison and calculation. I also converted the salaries to annual pay in USD based on the India-US currency conversion rate.

Argentina Dataset (2023)

[https://www.kaggle.com/datasets/aletbm/argentina-salary-survey-sysarmy/](https://www.kaggle.com/datasets/aletbm/argentina-salary-survey-sysarmy/)

This was a dataset of Argentinian salary surveys published on the Sysarmy blog. OpenQube works to provide up-to-date information about jobs in the information technology field. I translated whatever I could from Spanish to English, cleaned up irrelevant fields, and converted the salaries to annual pay in USD.

### Histograms

To examine the initial spread of the data, I used histograms. I found an interesting spread of data for each country / region, with spikes around common “round” numbers, likely because salaries tend to round up or down towards the nearest hundred or thousand rather than have very specific values.

US & EU Dataset

![](https://lh7-us.googleusercontent.com/9mUpmiOUKaN9IzMHGXGAgv6QyE-9qOhvcGJFVJsjSiNCHePm7iixGFqnur6L2GlJrAGuba2zdEnMii2LTQWGtQNgwHE9XaJ-LaYErFGi4AoEioSloN4EGd6cVdmfCJa3hBB-aFl1LvdmDvqq4IHd2Hw)

India Dataset

![](https://lh7-us.googleusercontent.com/LgB8BMqEfW2F4JIglsV6Zgo9CTTs86R2jxKr24o115kXF5wikvLtiY-gi1asrQ90-_SCDD7i4GDHCHNOBQAkMQGyE5PaxrqGOdeWbUZNFEIZUPflxJCM2xzZFFtioavsvqYKGnBszw8mLgvjYU8qNi4)

Argentina Dataset

![](https://lh7-us.googleusercontent.com/Kp-t9QRXxAjjHlP2YzrvwI1zQv-GqR3x8wD_bIw6xI98lsXu4WtEnci65uV1sG99dFEcufcyjFFDEiEN22609-kzGe0cTz_5v9cMOUXZn0iLxjp1jQf_TcWhIe2Ide2t3qWOyUFnaZ6wrkn9NWfogrg)

### Comparing Countries

I first wanted to understand how compensation varied, not just in how countries compensate the same role, but by looking at what roles, locations, and companies are at the top of the compensation list.

1. Given the same role (Developer / Engineer), how much does each country pay?

For this bar graph, I searched for any role that contained “developer” or “engineer” and averaged their compensation for each country. From there, I found that on average, the US/EU salary annual base pay is 7.07 times bigger than the salary in Argentina and approximately 12.57 times bigger than the salary in India.

Figure 1.1: Average Pay for Developer/Engineer Roles by Country (Table)![](https://lh7-us.googleusercontent.com/WxLYCKb05yN6S_INay-3wx-UGrUhLNjRs521yFyNq6JSq-FxV1n_S7OGXs_gqY4Qko7UQEjUFMt7fDia3WTYkEgRd616HvPJBZ0w8rbr-_BKOYAcGTJl1cpKaum7k6KcvVxbj-Q1GLKR78y5CwB-ln4)

Figure 1.2: Average Pay for Developer/Engineer Roles by Country (Bar Graph)
![](https://lh7-us.googleusercontent.com/6TdR5vz4kiDIRAEwDUVILDTVE2LzTPz9oO91wgyhDUwOtHkn1CaqY5OAxSgm_9li7zj6CGZt-Xbvc6IO8pdMwrFwCpMr6bF7bi7ITMA0Opfv6ZNs6JQa1d2mHbe-IDEyln-ZT-R3WLBS3FkG69zw5R0)

To better understand this pay gap, we have to acknowledge that variations in cost of living obviously play a big role. The data aggregator Numbeo helps us get a good picture of this by estimating from a large amount of user data the prices of local groceries, rent, and more.

In the United States, the average monthly expenses, excluding rent, amount to $1,196.8, with an additional $1,843.30 for a one-bedroom apartment in the city center. Consequently, the estimated monthly expenses, including rent, for a single person in the U.S. total $3,040.1, accumulating to $36,481.2 annually. Contrastingly, in India, the cost of living is markedly lower, with estimated monthly expenses of $347.0 (₹28,921.3) before rent. Rent in India, on average, is 86.6% lower than in the U.S. The monthly rent for a one-bedroom apartment in the city center is ₹18,347.39, equivalent to approximately $246.8. Therefore, the total estimated monthly expenses, including rent, for a single person in India amount to $596.8, and annually, this equates to $7,161.6. Meanwhile, in Argentina, the estimated monthly expenses for a single person, excluding rent, are $441.9. The average rent in Argentina is 85.2% lower than in the U.S., with a monthly cost of $273.48 for a one-bedroom apartment in the city center. Consequently, the total estimated monthly expenses, including rent, in Argentina sum up to $715.38, and on a yearly basis, this amounts to $8,584.56.

Figure 1.3: Cost of Living Across 3 Countries

![](https://lh7-us.googleusercontent.com/J-fgfc0FY8Yq_tOtijpg_qGwpWJXboyTGSEXag2w5hzAaSHhhrTpqkc83dtLCs75n-EGWgCmfwRNZxrA308ThEwQ9lBq4UP6EmIF74W6PaTYZElCU8r-Oimt4cLB21uO-uxFAyGjnQ6-4hUlpWQIrsU)

Thus, the yearly expenses in the US/EU are approximately 4.25 times higher than in Argentina and approximately 5.09 times higher than in India. This is still way below the comparatively higher wages, as shown in the bar. We can further see just how large this gap is with the bar graph below, showing annual base pay compared to cost of living for each country.

Figure 1.4 Cost of Living Compared to Annual Base Pay

![](https://lh7-us.googleusercontent.com/3EPWYJAKJ5Jk5aeKfLk4Ac1vhs6fgNzaUvADCWjDdhdfn9JkYmbD5Pg2K1fjaLSNRzRHvGc7QaLzMJ-RKMzyjYzQ9xkX_LuA0zxhveI61SDTlQVSyvZQApxy1TwhMJCx2BGjUO9bg4mc40szGXm_Dlg)

From this analysis, it is evident that despite variations in the cost of living, technology professionals in the US and EU still enjoy significantly higher compensation compared to their counterparts in India and Argentina. This discrepancy aligns with the widespread notion that higher-wage engineering roles are more prevalent in developed countries.

These salary differences shed light on the reasons behind the increasing trend of remote work and globalization, leading many companies to outsource engineering tasks to Latin America and India. However, it's worth noting that they also show the limits of outsourcing, which still tends to be more prevalent for lower-wage engineering work, while the highest-paying and leadership roles are likely to remain concentrated in the US and EU.

This data thus emphasizes the profound impact of economic development and industry maturity on salary structures. In essence, it supports the hypothesis that the tech industry in developed countries presents more financially rewarding opportunities for engineering professionals even when compared to cost of living, making them an attractive destination for top talent seeking higher salaries.

Regardless of whether those high tech salaries in the US are because of network effects, superior education, or venture capital structures, the economic benefit of being in the US/EU as a tech worker is unrivaled to any other location. Until this changes, we are likely to continue observing large waves of tech-related immigration to the US, increasing competition in the US/EU job market and making visas for H1B applicants even more competitive.

2. What are the highest-paying roles per country?

Based on the data in Figure 1, I was curious to see which positions were most highly-paid per country, so I created pivot tables to find the most highly paid roles.

Figure 2: Highest Paid Positions per Country

![](https://lh7-us.googleusercontent.com/HJlFL1d_9o06NaVKmbOQBuQ5zOFC4NV9wEZY-3amKr01sE4PISMTcV_xCzVBy8ds3Z_9LtlxGduB5y3cyrTXSQ7kCyNdDftZyVVsbmcLc6q7ZNxhpbnrrafbNFm2-wwpzz_V34OFgz1tR4msMtXfP68)

The obvious takeaway from these tables is that specific, one-of-a-kind technical positions and leadership positions are the most highly compensated by all countries, evidenced by how titles like “UX Designer” did not come up. The more interesting insight is that India and Argentina have very similar top-salary positions despite Argentina having higher salaries on average. This may be due to the datasets being biased by their differences in survey respondents. However, at least in this data, India may have proportionally more poorly-compensated jobs, but it also has highly compensated jobs comparable to those in Argentina. A last note is the front-end intern for India, which might be an outlier, but might also reflect that interns are highly compensated in some companies or for some specialties.

3. What are the highest-paying regions in each country?

Similarly, these pivot tables, using the same code as before but with a different column, examined compensation by location.

Figure 3: Highest Paid Locations per Country

![](https://lh7-us.googleusercontent.com/DJPnq8i6bRaDGgcv2AFILlXR-YwXZBHCLIg1H9i6Y__2So5evhbqSOtSd8IvIJy5kxGkj00x9u2vKaMO3Gb_p_rwr-ZeDg-LpeO6Nrd6bMBb243uHPOeMzGTk6SR4GPycJgAlILAVvWrZMGjuHlQJZ4)

These values are easily distorted by one or more salaries being extremely highly compensated, or by some areas being much more well-represented than others (the EU salaries, for example, are likely the only ones reported for their area, while the Indian and Argentinian locations each likely represent at least two or more salaries averaged together). However, it is crucial to note that while the Swedish salary might look extremely high, marginal tax in Sweden is nearly 33% for salaries above $500,000. Similarly, marginal tax rate for Los Angeles for a $300,000 salary is 48.7%. Thus, much of what appears to be inequality in compensation is also extracted by taxation.

4. What is the average pay for the most common job titles in each country?

Figure 4: Average Pay for Top 10 Most Common Job Titles

![](https://lh7-us.googleusercontent.com/cZ27le0YtQezr_RQACOUOMt7460KGMjt6DbgnwqrkrLkFln2C72yCQ6FFqpgmO9yN_JNhbo0Rn712bS0Tx20HP9d3DN6Sjl_ukfqVqYT88JHsMHv3WQwpCZUMoCYYdIvImLwPMiNZ-JPgl4rO1hDdvc)![](https://lh7-us.googleusercontent.com/vUKN3H8Q5pp4SaZlv1RfGWUmOiNv-7nnoRnOc_RxEpCcxVnnak2dMfnOgshcNTDPLR_0mD9XtQX8KQcj9DLmqCJ_LN1HeiDE5agZh-H4VfipTLVWvjlRxiQ2lHs6qP_J4jZgnJXR30oPfEcf3u1AOhQ)![](https://lh7-us.googleusercontent.com/KjKZ-vnJRreQxpXu1omwkkgRBekRO8a7g_pGif4060P97udswwTpcJ4sgJhca1ZXEQxOUXAWw7IAObhwQoKEJfv2PcSN90kqN5xa7j6wpk_hxiqmQhuUBsZNGgbjpxLNN2iM3h2vWhT4pznDF9yWeG4)

**	**Again, it is quite clear that leadership and technical skills are well compensated, but compensation might still be much more dependent on the company than on the title, as evidenced by how Software Engineer II is below Software Engineer in the US/EU.

### Deep Dive: Gender in Argentina

5. How does gender affect pay for tech salaries in Argentina?

**	**The Argentinian dataset was the only one with gender data, so I decided to compare the mean salary for the same role for each gender. I found an interesting pattern.
Figure 5: Comparison of Compensation by Job Title in Argentina

![](https://lh7-us.googleusercontent.com/rvmz0l92UnqEQJvBbc2jvlguMT2R9hf6CtCHGalcebvViSqjKVMQLDlG-Ls8iPgPqj8DF5OiS6wpmOBLRsMEHAkPxYPICfyxXz6DN10ow8mWkr5Clbj-BpJVXAod_lYXE9phljzrizy-TA2yBAepS3M)

Figure 6: Comparison of Compensation by Job Title in Argentina, Tabulated

![](https://lh7-us.googleusercontent.com/IJPZppWEiWhNjbfBYfEM7Lu0btHLSm7cJfypphhtHna3g58xIQSu0mK12BPhLTP2FoXaCi2cZ7SlPulBqCcl7Xs1_WkP5dUu9FqeDOTauZLose3CFdu1VYPrMXO7j6NW3WQ2MB35nFOrGVeDLjDv8S0)

For technical positions, men seem to have a higher mean salary than women. However, for less technical positions in testing, project management, and UX design, the gender pay gap is less steep. This may be for a number of reasons. First, Argentina is still quite patriarchal, which might affect norms around traditionally male or female jobs. Engineers may still be seen as primarily male, and therefore women may be disincentivized to aggressively pursue both the career or subsequent promotions. Second, women and men may have answered the survey in disproportionate quantities. Lastly, the jobs themselves may have slightly different compensation structures. However, I also suspect that this pattern may emerge from other factors such as motherhood penalty or the effect of career breaks and workplace discrimination in more traditionally male-dominated industries such as engineering.

### Conclusions and Insights

In summary, this analysis of global tech salaries across the United States, India, and Argentina reveals substantial disparities in how similar roles are compensated based on country, location, and even gender. Despite the constraints of all three datasets, technical and leadership positions, in the end, still command the highest compensation. Notably, India and Argentina exhibit similarities in top-salary positions, hinting at convergence in certain sectors despite overall average pay differences. Examining compensation by gender in the Argentinian dataset unveils a gender pay gap, particularly in technical positions. Other datapoints reveal relevant insights about taxation and globalization.

All in all, these patterns in compensation point to interesting differences between developing and developed countries. They prompt further investigation into societal norms, respondent demographics, and compensation structures, emphasizing the need for targeted efforts to address disparities in the tech industry. In the future, I would like to get more comprehensive data in order to conduct more accurate cross-country comparisons and get a more nuanced understanding of the tech landscape for all three countries.

### References

Numbeo. (n.d.). Cost of living in United States. Retrieved from [https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States](https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States)

Numbeo. (n.d.). Cost of living in Argentina. Retrieved from https://www.numbeo.com/cost-of-living/country_result.jsp?country=Argentina

Numbeo. (n.d.). Cost of living in India. Retrieved from https://www.numbeo.com/cost-of-living/country_result.jsp?country=India

Telle, B. (n.d.). Know Your Worth: Tech Salaries in 2016. Retrieved from https://www.kaggle.com/datasets/thedevastator/know-your-worth-tech-salaries-in-2016

Banerjee, S. (n.d.). Software Industry Salary Dataset - 2022. Retrieved from https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022

Sysarmy. (n.d.). Argentina Salary Survey. Retrieved from https://www.kaggle.com/datasets/aletbm/argentina-salary-survey-sysarmy

**
