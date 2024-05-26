<main>
  <title>BINI Data Science Portfolio</title>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ NAVIGATION BAR  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
	<div class="navbar bg-base-100">
		<div class="flex-1 text-xl px-5">BINI</div>
		<div class="flex-none">
			<ul class="menu menu-horizontal">
        <!-- Navbar options -->
				<li class="px-5">Overview</li>
				<li class="px-5">Data</li>
        <li class="px-5">Exploration</li>
        <li class="px-5">Modelling</li>
        <li class="px-5">Results</li>
        <li class="px-5">Conclusion</li>
        <li class="px-5">The Team</li>
			</ul>
		</div>
	</div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col items-center justify-center h-screen w-full bg-slate-50">
    <h1 class="text-9xl py-4 font-medium text-zinc-950">Closing the Gap</h1>
    <h2 class="text-3xl font-bold text-zinc-950">An In-Depth Look at Gender Inequality in the Philippine Labor Force</h2>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col h-screen w-full">
    <h1 class="place-self-center text-5xl py-4 font-medium">Overview</h1>
    <span>The fight for gender equality and women empowerment is long and arduous. In the Philippines, the patriarchal mindset is glaringly apparent, with the stigmatization of gender roles leaving women less likely to take on more domestic, familial duties, in favor of hanging the more productive work to males. 
    This is the case despite the fact that women&#39;s access to education have significantly improved--clearly, the issue lies in pervasive, discriminatory gender norms, which are behind the gender gap in the labor force despite women being as competent and employable as men.
    In an attempt to paint a better picture of how discrimination has affected opportunities for women to work, our group will investigate the gender gap present in the labor force. </span>

    <h3>Problem</h3>
    <p>Gender bias strengthens the lack of institutionalized support for discrimination against women in the labor force.</p>
        
    <h3>Solution</h3>
    <p>Use data science to study patterns and trends in the participation of women in the labor force, and propose solutions related to gender diversity and inclusion in the labor force.</p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col h-screen w-full">
    <h1>Background</h1>
      <p>According to the National Economic and Development Authority (NEDA), the Philippines has the lowest female labor force participation rate in the ASEAN region, and possesses one of the widest gender gaps in the labor force, as of 2019.
      Despite signs of improvement in the levels of gender parity in East Asia and the Pacific, as compared to the previous index, the Philippines still ranked 16th in the Gender Global Gap Index in 2023.
      From the 2023 Labor Force Survey, there is a 21.3% gap in labor participation status between men and women.
      Through data analysis, we aim to answer the following questions:</p>

      <li>What jobs under the labor force do women take the most?</li>
      <li>Over the years, what factors correlate significantly with lack of women employment?</li>
        
    <h3>Null Hypothesis</h3>
      <p>There are no identifiable work types where women are more outnumbered. Additionally, there is no significant relationship between certain factors (e.g. region, relationship with house head, educational attainment, etc.) and the gender gap between men and women in the labor force.</p>
            
    <h3>Alternative Hypothesis</h3>
      <p>There are job types with a more prevalent gender gap, where women are significantly outnumbered and less likely to be found participating in. There are also identifiable factors that closely correlate with the gap between men and women in the labor force.</p>
            
    <h3>Action Plan</h3>
      <p>Analyze data from factors affecting bias in recruitment, opportunities, and participation of women in the labor force.</p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col h-screen w-full">
    <h1 class="place-self-center text-5xl py-4 font-medium">Data Collection</h1>
    <p> See our data set <a href="https://docs.google.com/spreadsheets/d/1JgijpA5MjRV2Fa3gpj7ithFEpoxXdo__7hyw2Q9ZnmM/edit?usp=sharing">here</a> </p>
    <h3>Description of data set</h3>
        <p>The dataset was obtained by collating responses from the yearly Labor Force Survey conducted by the Philippine Statistics Authority (PSA). It contains data on the socioeconomic factors affecting employment levels, which aims to provide a basis for policies on the local labor market. </p>
    <h3>Data collection process</h3>
        <p>Survey responses from five (5) years (2018-2022) were collected, with each being available from January of the succeeding year. The .xlsx files containing raw data observations and metadata dictionary were downloaded from the PSA website.</p>
    <h3>Sampling method</h3>
        <p>Using Python and pandas 200 rows were randomly sampled out of each year and compiled into a .csv file.</p>
    <h3>Data set size</h3>
        <p>A total of 1000 observations were collected.</p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col items-center justify-center text-5xl py-4 font-medium">
    Data Exploration
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col">
    <h1>References</h1>
    <li>https://psada.psa.gov.ph/catalog/LFS/about</li>
    <li>https://neda.gov.ph/women-in-the-workplace-paving-a-better-landscape-in-the-labor-force/</li>
    <li>https://neda.gov.ph/wp-content/uploads/2021/09/Determinants-of-Female-Labor-Force-Participation-in-the-Philippines.pdf</li>
    <li>https://psada.psa.gov.ph/catalog/LFS/about</li>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONTENT SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col items-center justify-center text-5xl py-4 font-medium">
    The Team
  </div>
</main>
