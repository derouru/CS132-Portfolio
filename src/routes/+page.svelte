<main>
  <title>BINI Data Science Portfolio</title>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ NAVIGATION BAR  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
	<div class="navbar bg-base-100">
		<div class="flex-1 text-xl px-5">BINI</div>
		<div class="flex-none">
			<ul class="menu menu-horizontal space-x-5">
        <!-- Navbar options -->
				<li class="btn px-3" >Overview</li>
				<li class="btn px-3" >Data</li>
        <li class="btn px-3" >Exploration</li>
        <li class="btn px-3" >Modelling</li>
        <li class="btn px-3" >Results</li>
        <li class="btn px-3" >Conclusion</li>
			</ul>
		</div>
	</div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ LANDING SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="hero min-h-screen bg-gradient-to-r from-red-300 from-20% via-red-300 via-30% to-red-100 to-90%">
    <div class="hero-content text-center">
      <div class="max-w-4xl">
        <h1 class="text-9xl py-2 font-medium text-zinc-950 font-['Helvetica']">Closing the Gap</h1>
        <p class="py-6 text-3xl font-bold text-zinc-950 ">An In-Depth Look at Gender Inequality in the Philippine Labor Force.</p>
        <!--<button class="btn btn-primary">Let's learn more</button>-->
      </div>
    </div>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ BACKGROUND / OVERVIEW SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col items-center justify-center h-3/4 w-3/4 mx-auto mt-6">
    <h1 class="text-5xl py-4 font-medium text-center">The fight for gender equality and women empowerment is <span class="text-red-300">long and arduous</span></h1>
    <span> In the Philippines, the patriarchal mindset is glaringly apparent, with the stigmatization of gender roles leaving women less likely to take on more domestic, familial duties, in favor of hanging the more productive work to males. 
    This is the case despite the fact that women&#39;s access to education have significantly improved--clearly, the issue lies in pervasive, discriminatory gender norms, which are behind the gender gap in the labor force despite women being as competent and employable as men.
    In an attempt to paint a better picture of how discrimination has affected opportunities for women to work, our group will investigate the gender gap present in the labor force. </span>
    
    <p class="my-4 text-center">According to the National Economic and Development Authority (NEDA), the Philippines has the lowest female labor force participation rate in the ASEAN region, and possesses one of the widest gender gaps in the labor force, as of 2019.
      Despite signs of improvement in the levels of gender parity in East Asia and the Pacific, as compared to the previous index, the Philippines still ranked 16th in the Gender Global Gap Index in 2023.
      From the 2023 Labor Force Survey, there is a 21.3% gap in labor participation status between men and women.</p>
  </div>
  <div class="divider"></div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ HYPOTHESIS SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="flex flex-col h-3/4 w-3/4 mx-auto">
    <h3 class="text-3xl py-4 font-medium text-center text-red-300">TLDR; What's the problem?</h3>
    <p>Gender bias strengthens the lack of institutionalized support for discrimination against women in the labor force.</p>
        
    <h3 class="text-3xl py-4 font-medium text-center text-red-300">What's our objective?</h3>
    <p>Use data science to study patterns and trends in the participation of women in the labor force, and propose solutions related to gender diversity and inclusion in the labor force.</p>
    <div class="divider"></div>
    <p class="py-8 text-3xl py-4 font-medium text-center">Through data analysis, we aim to answer the following questions:</p> 
    <p  class="text-3xl py-4 font-medium text-base-100 text-center bg-gradient-to-r from-red-300 from-20% via-red-300 via-30% to-red-100 to-90%">Q1: What jobs under the labor force do women take the most?</p>
    <p  class="text-3xl py-4 font-medium text-base-100 text-center bg-gradient-to-r from-red-300 from-20% via-red-300 via-30% to-red-100 to-90%">Q2: Over the years, what factors correlate significantly with lack of women employment?</p>
    <div class="divider"></div>
    <div class="flex max-w-6xl justify-center mx-auto">
      <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center">
        <h3 class="text-3xl">Null Hypothesis</h3>
        <p class="text-center text-red-300">There are no identifiable work types where women are more outnumbered. Additionally, there is no significant relationship between certain factors (e.g. region, relationship with house head, educational attainment, etc.) and the gender gap between men and women in the labor force.</p>
      </div>
      <div class="divider divider-horizontal"></div>
      <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center">
        <h3 class="text-3xl">Alternative Hypothesis</h3>
        <p class="text-center p-5 text-red-300">There are job types with a more prevalent gender gap, where women are significantly outnumbered and less likely to be found participating in. There are also identifiable factors that closely correlate with the gap between men and women in the labor force.</p>
      </div>
    </div>
    
    <div class="divider"></div>
    <h3 class="text-3xl py-4 font-medium text-center">So what now?</h3>
      <p>We analyzed data from factors affecting bias in recruitment, opportunities, and participation of women in the labor force.</p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DATA COLLECTION SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="divider"></div>
  <div class="flex flex-col h-screen w-3/4 mx-auto">
    <h1 class="text-5xl py-4 font-medium text-center text-red-300">Data Collection</h1>
    
    <h3 class="text-3xl py-4 font-medium text-center">Description of data set</h3>
        <p>The dataset was obtained by collating responses from the yearly Labor Force Survey conducted by the Philippine Statistics Authority (PSA). It contains data on the socioeconomic factors affecting employment levels, which aims to provide a basis for policies on the local labor market. </p>
    <h3 class="text-3xl py-4 font-medium text-center">Data collection process</h3>
        <p>Survey responses from five (5) years (2018-2022) were collected, with each being available from January of the succeeding year. The .xlsx files containing raw data observations and metadata dictionary were downloaded from the PSA website.</p>
    <h3 class="text-3xl py-4 font-medium text-center">Sampling method</h3>
        <p>Using Python and pandas 200 rows were randomly sampled out of each year and compiled into a .csv file.</p>
    <h3 class="text-3xl py-4 font-medium text-center">Data set size</h3>
        <p>A total of 1000 observations were collected!</p>
    <button class="btn py-4 mt-6">See our data set <a href="https://docs.google.com/spreadsheets/d/1JgijpA5MjRV2Fa3gpj7ithFEpoxXdo__7hyw2Q9ZnmM/edit?usp=sharing">here</a></button>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DATA EXPLORATION SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="divider"></div>
  <div class="flex flex-col w-3/4 mx-auto">
    <h1 class="text-5xl py-4 font-medium text-center text-red-300">Data Exploration</h1>
    <!-- ADD MORE CONTENT HERE LIKE DOCUMENTATION AND GRAPHS-->
    <p class="text-center">content here</p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ REFERENCES SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="divider"></div>
  <div class="flex flex-col w-3/4 mx-auto p-5">
    <h1>References</h1>
    <li>https://psada.psa.gov.ph/catalog/LFS/about</li>
    <li>https://neda.gov.ph/women-in-the-workplace-paving-a-better-landscape-in-the-labor-force/</li>
    <li>https://neda.gov.ph/wp-content/uploads/2021/09/Determinants-of-Female-Labor-Force-Participation-in-the-Philippines.pdf</li>
    <li>https://psada.psa.gov.ph/catalog/LFS/about</li>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ABOUT THE TEAM SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <footer class="footer p-10 bg-base-300 text-base-content">
    <nav>
      <h6 class="footer-title leading-3">Audrey Dela Vega</h6> 
      <a href="https://github.com/mycronare" class="link link-hover">@mycronare</a>
    </nav> 
    <nav>
      <h6 class="footer-title leading-3">Janelle Mendoza</h6> 
      <a href="https://github.com/sojaja" class="link link-hover">@sojaja</a>
    </nav> 
    <nav>
      <h6 class="footer-title leading-3">Jackie Vicerra</h6> 
      <a href="https://github.com/derouru" class="link link-hover">@derouru</a>
    </nav>
  </footer>
</main>
