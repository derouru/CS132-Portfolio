<script>
  import Parallax from '$lib/Parallax/Parallax.svelte'
  import Hypothesis from '$lib/Hypothesis/Hypothesis.svelte'
  import DataCollection from '$lib/DataCollection/DataCollection.svelte'
  import Footer from '$lib/Footer/Footer.svelte'

  function scrollToSection(id) {
        const section = document.getElementById(id);
        if (section) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const offset = navbarHeight + 20; // Navbar offset

            window.scrollTo({
                top: section.offsetTop - offset,
                behavior: 'smooth'
            });
        }
    }
</script>

<html lang=en>
  <title>BINI Data Science Portfolio</title>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ NAVIGATION BAR  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div class="navbar bg-base-100 z-50 fixed top-0 w-full px-5 py-3">
    <div class="max-w-screen-lg mx-auto flex items-center justify-between">
        <div class="text-3xl font-bold pr-8">BINI</div>
        <ul class="flex space-x-3">
            <li><button class="btn px-2" on:click={() => scrollToSection('overview')}>Overview</button></li>
            <li><button class="btn px-2" on:click={() => scrollToSection('data')}>Data</button></li>
            <li><button class="btn px-2" on:click={() => scrollToSection('exploration')}>Exploration</button></li>
            <li><button class="btn px-2" on:click={() => scrollToSection('modelingAndResults')}>Modelling & Results</button></li>
            <li><button class="btn px-2" on:click={() => scrollToSection('conclusion')}>Conclusion</button></li>
        </ul>
    </div>
</div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ PARALLAX COVER SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <Parallax />
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ BACKGROUND / OVERVIEW SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div id="overview" class="flex flex-col items-center justify-center h-3/4 w-3/4 mx-auto mt-6">
    <h1 class="text-5xl mb-10 font-medium text-center">The fight for gender equality and women empowerment is <span class="text-fuchsia-300">long and arduous</span></h1>
    <p> In the Philippines, the patriarchal mindset is glaringly apparent, with the stigmatization of gender roles leaving women less likely to take on more domestic, familial duties, in favor of hanging the more productive work to males. 
    This is the case despite the fact that women&#39;s access to education have significantly improve.
    <sup><a class="text-fuchsia-300 font-bold" href="https://neda.gov.ph/women-in-the-workplace-paving-a-better-landscape-in-the-labor-force/">[1]</a></sup>
    </p>
    
    <p class="my-4">According to the National Economic and Development Authority (NEDA), the Philippines has the lowest female labor force participation rate in the ASEAN region, and possesses one of the widest gender gaps in the labor force, as of 2019.
      Despite signs of improvement in the levels of gender parity in East Asia and the Pacific, as compared to the previous index, the Philippines still ranked 16th in the Gender Global Gap Index in 2023.
      From the 2023 Labor Force Survey, there is a 21.3% gap in labor participation status between men and women.
      <sup><a class="text-fuchsia-300 font-bold" href="https://neda.gov.ph/wp-content/uploads/2021/09/Determinants-of-Female-Labor-Force-Participation-in-the-Philippines.pdf">[2]</a></sup>
    </p>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ HYPOTHESIS SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <Hypothesis />
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DATA COLLECTION SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div id="data" class="divider"></div>
  <DataCollection />
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DATA EXPLORATION SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div id="exploration" class="divider"></div>
  <div class="flex justify-center items-center">
    <div class="max-w-4xl mx-auto p-6 bg-base-300 rounded-lg shadow-lg">
      <h1 class="text-5xl py-4 font-medium text-center text-fuchsia-300">Data Exploration</h1>
      <p class="text-center">content here</p>
    </div>
  </div>

  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ RESULTS SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div id="modelingAndResults" class="divider"></div>
  <div class="flex justify-center items-center">
    <div class="max-w-4xl mx-auto p-6 bg-base-300 rounded-lg shadow-lg">
      <h1 class="text-5xl py-4 font-medium text-center text-fuchsia-300">Modeling & Results</h1>
      <p class="text-center">content here</p>
    </div>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ CONCLUSION SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <div id="conclusion" class="divider"></div>
  <div class="flex justify-center items-center">
    <div class="max-w-4xl mx-auto p-6 bg-base-300 rounded-lg shadow-lg">
      <h1 class="text-5xl py-4 font-medium text-center text-fuchsia-300">Conclusion</h1>
      <p class="text-center">content here</p>
    </div>
  </div>
  <!-- ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ABOUT THE TEAM SECTION ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ -->
  <Footer />
</html>

<style>
</style>