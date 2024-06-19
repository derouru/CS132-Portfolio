<script>
    import EmployedGender from "$lib/assets/employedIndividualsbyGender.png"
    import HouseHead from "$lib/assets/householdHead.png"
    import HouseSize from "$lib/assets/householdSize.png"
    import MaritalStat from "$lib/assets/maritalStatus.png"
    import NatureEmploy from "$lib/assets/natureOfEmployment.png"
</script>

<html lang='en'>
    <h3 class="text-3xl py-4 font-medium">Identifying female-centric work types</h3>
    <p class="text-left">The following are visualizations of the gender gap calculated for each category under different primary occupation types, different industry types, and worker class:</p>
    <!--INSERT 3 GRAPHS HERE-->
    <span class="flex justify-center items-center">
        <!--<img class="mt-5" id="formula" src="{}" alt="formula" width="75%" height="auto">-->
    </span>

    <p class="text-left">The t-tests were able to identify that women are prevalent in the following work classifications:</p>
    <!--INSERT TO SMALLER CARD-->
    <div class="max-w-4xl mx-auto bg-base-300 shadow-lg rounded-lg overflow-hidden m-5">
          <!-- Smaller Card 1 -->
          <div class="bg-base-100 rounded-lg p-4 mb-4">
            <h4 class="text-3xl py-4 font-medium">Primary occupation type</h4>
            <p class="text-left">
              1. Clerical Support Workers (p = 0.0245)<br>
              2. Service and Sales Workers (p = 0.0417)
            </p>
          </div>
      
          <!-- Smaller Card 2 -->
          <div class="bg-base-100 rounded-lg p-4 mb-4">
            <h4 class="text-3xl py-4 font-medium">Primary occupation industry type</h4>
            <p class="text-left">
              1. Wholesale and Retail Trade; Repair of Motor Vehicles* (p = 00014)<br>
              2. Human Health and Social Work Activities (p = 0.0479)
            </p>
          </div>
      
          <!-- Smaller Card 3 -->
          <div class="bg-base-100 rounded-lg p-4">
            <h4 class="text-3xl py-4 font-medium">Class of worker</h4>
            <p class="text-left">
              1. Private household (p = 0.0281)<br>
              2. Without pay (Family-owned business) (p = 0.0005)**
            </p>
          </div>
      </div>
      

    <p class="text-left">Meanwhile, women are significantly outnumbered in the following:</p>

    <div class="max-w-4xl mx-auto bg-base-300 shadow-lg rounded-lg overflow-hidden m-5">

        <div class="bg-base-100 rounded-lg p-4 mb-4">
            <h4 class="text-3xl py-4 font-medium">Primary Occupation Type</h4>
            <p class="text-left">
            1. Skilled Agricultural, Forestry and Fishery Workers** (p = 0.0002)<br>
            2. Craft and Related Trades Workers* (p = 0.0030)<br>
            3. Plant and Machine Operators and Assemblers** (p = 0.0001)
            </p>
        </div>

        <div class="bg-base-100 rounded-lg p-4 mb-4">
            <h4 class="text-3xl py-4 font-medium">Primary Occupation Industry Type</h4>
            <p class="text-left">
            1. Agriculture and Forestry** (p = 0.0004)<br>
            2. Fishing and Aquaculture (p = 0.0580)<br>
            3. Construction** (p = 0.0001)<br>
            4. Transportation and Storage** (p = 0.0001)
            </p>
    </div>

    <div class="bg-base-100 rounded-lg p-4">
        <h4 class="text-3xl py-4 font-medium">Class of Worker</h4>
            <p class="text-left">
             1. Private Establishment** (p = 0.0001)
            </p>
    </div>
</div>
    <!--END INSERT TO SMALLER CARD-->
    
    <h3 class="text-3xl py-4 font-medium">Identifying factors that correlate with gender gaps in the labor force</h3>
    <p class="text-left">The following are visualizations of the distribution of men and women in different work classifications:</p>
    <!--INSERT GRAPH-->
    <p class="text-left">An unpaired t-test between two means showed that there is a significant difference between employed male and female workers across all categories (p = 0.0001). The total number of men and women were 509 and 491, respectively. Men had an employment rate of 47.937% &#40;244&#41;, and women had an employment rate of 34.623% &#40;170&#41;.</p>
    <!--INSERT GRAPH-->
    <p class="text-left">The figure above shows the computed gender ratio for each household size category.</p>
    <p class="text-left mt-5">The t-tests were able to identify that there is a significant gender gap among those employed with a household size of 2 (p = 0.0366) and 5 (p = 0.0367)--women are severely outnumbered in these categories. As for the rest of the household sizes, the analysis yielded no significant findings. This could be attributed to the fact that 2 and 5 are more common household sizes, with the average national household size being 4.1.
        <sup><a class="text-fuchsia-300 font-bold" href="https://www.arcgis.com/home/item.html?id=5e9a37f7a6734cac9e5c3ec0431e56f3#:~:text=Description-,This%20layer%20shows%20the%20average%20household%20size%20in%20Philippines%20in,household%20population%20by%20total%20households.">[4]</a></sup>
    </p>
    <!--INSERT GRAPH-->
    <p class="text-left mt-5">There is a weak positive correlation between household size and women ratio, meaning that in a group of employed people with the same family size will have more women in proportion to men as the family size increases. however the correlation is only weakly positive.</p>
    <!--INSERT GRAPH-->
    <p class="text-left mt-5 mb-5">The figure above shows the computed gender ratio for each category under relationship to household head. </p>
    <p class="text-left">One sample t-test on each relationship category showed that there is a significant gender gap within household heads (p = 0.0001), and women are greatly outnumbered in this category. However, among those that identify as spouses to the household head (p = 0.0001), it is the opposite as women greatly outnumber men. Other statistically significant gender gaps are among those that identify as sons/daughters of the head (p = 0.0429) and sons/daughters in law (p = 0.0245).</p>
    <!--INSERT GRAPH-->
    <p class="text-left mt-5 mb-5">The figure above shows the computed gender ratio for each marital status.</p>
    <p class="text-left mt-5 mb-5">One sample T-test showed that there is no significant gender gap among single and divorced/separated employed people. However, the gender ratio is skewed towards men among married employed people significantly (p = 0.0002). This is also the case for widowed people (p = 0.0148), but towards women.</p>
    <!--INSERT GRAPH-->
    <p class="text-left mt-5 mb-5">The figure above shows the computed gender ratio for each category under nature of employment.</p>
    <p class="text-left mt-5 mb-5">One sample t-test showed that there is a significant gender gap among people with permanent jobs (p = 0.0055) and short term jobs (p = 0.0044).</p>
</html>

<style>
</style>