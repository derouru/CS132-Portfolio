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
    <!--INSERT GRAPH2-->
    <!--INSERT GRAPH3-->
    <p class="text-left">The t-tests were able to identify that there is a significant gender gap among those employed with a household size of 2 (p = 0.0366) and 5 (p = 0.0367)--women are severely outnumbered in these categories. As for the rest of the household sizes, the analysis yielded no significant findings. This could be attributed to the fact that 2 and 5 are more common household sizes, with the average national household size being 4.1. </p>
    <!--INSERT GRAPH4-->
</html>

<style>
</style>