<script>
</script>

<html lang='en'>
    <h3 class="text-3xl py-4 font-medium">Preprocessing</h3>
    <p class="text-left">For the first part of exploratory data analysis, the data is first cleaned. Missing values were filled in appropriately and it was made sure that all data points are formatted correctly. Columns or areas of interest relevant to hypothesis testing were identified and standardized, and data irrelevant to the factors being inspected were discarded. Responses made by underage and unemployed respondents were also discarded.</p>
    <p class="text-left mt-8 mb-8">In order to identify which jobs under the labor force have more prevalent women employment, responses indicating sex, work and job indicators, primary occupation type, primary occupation industry, and worker class were considered. This data will be analyzed and statistically tested to check if women outnumber men significantly in certain work areas.</p>
    <p class="text-left">In order to identify which factors correlate significantly with lack of women employment, certain categories of employed people will be inspected and checked if the gender ratio within these categories are significantly skewed against women. For this, household size, relation to household head, marital status, and nature of employment were considered. </p>

    <h3 class="text-3xl py-4 font-medium">Visualization</h3>
    <p class="text-left">The data was summarized and converted into graphs for easier inspection of results. Data for all relevant categories were organized and collated into appropriate plots, and later interpreted and statistically analyzed.</p>
    
    <h3 class="text-3xl py-4 font-medium">Statistical Analysis</h3>
    <p class="text-left">The total number of men and women employed under each category per metric were tallied. Gender ratios were obtained per metric using the formula:</p>
    <!-- Insert mathematical formula-->
    <p class="text-left mt-8 mb-8">The gender ratio was statistically analyzed via a one-sample t-test against an expected mean of 0.5 &#40;equal gender distribution&#41;. The standard deviation for each sub-metric assessment would also be 0.5, since each male employee would set the data point to 0 and each female employee would set it to 1. N for each sub-metric is obtained by getting the sum of men and women that possess work that fall under them.</p>
    <p class="text-left">The t-tests were performed with two &#40;2&#41; tails and a 95% confidence interval. The significance of the difference between men and women under each sub-metric were assessed via obtained p-values, and are sorted into the following categories: not significant, significant &#40;p &lt; 0.05&#41;, very significant* &#40;p &lt; 0.005&#41;, and extremely significant** &#40;p &lt; 0.001&#41;. The latter three classifications are where the null hypothesis is rejected, and it can be assumed that women are either the dominant or the ones being outnumbered for that job type or categorization—identifying which of these is true was done by inspecting the gender ratio, a value less than 0.5 would indicate that the latter is the case.</p>

</html>

<style>
</style>