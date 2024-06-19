<script>
</script>

<html lang='en'>
    <div class="flex flex-col h-3/4 w-3/4 mx-auto">
        <div class="my-8 flex justify-center items-center">
            <div class="max-w-4xl w-full p-6 bg-base-300 text-white rounded-lg shadow-lg">
              <h3 class="text-3xl py-4 font-medium text-center text-fuchsia-300">TLDR; What's the problem here?</h3>
              <p>There is an issue that lies in pervasive, discriminatory gender norms, which are behind the gender gap in the labor force despite women being as competent and employable as men.</p>
            </div>
        </div>
          
        <div class="my-8 flex justify-center items-center">
            <div class="max-w-4xl w-full p-6 bg-base-300 text-white rounded-lg shadow-lg">
                <h3 class="text-3xl py-4 font-medium text-center text-fuchsia-300">Then— what can we do?</h3>
                <p>In an attempt to paint a better picture of how discrimination has affected opportunities for women to work, our group will investigate the gender gap present in the labor force. </p>
                <br>
                <p>We will use data science to study patterns and trends in the participation of women in the labor force, and propose solutions related to gender diversity and inclusion in the labor force.</p>
            </div>
        </div>
    
        <div class="flex flex-col items-center text-center p-10 space-y-7 mb-10">
            <p class="text-4xl">That's quite a big topic! So let's narrow down. Through data analysis, we aim to answer the following questions:</p> 
            <p class="text-2xl"><span class="text-fuchsia-300">Q1:</span> What jobs under the labor force do women take the most?</p>
            <p class="text-2xl"><span class="text-fuchsia-300">Q2:</span> Over the years, what factors correlate significantly with lack of women employment?</p>
        </div>

        <div class="flex max-w-6xl justify-center mx-auto space-x-4">
            <div class="flex flex-col h-80 w-1/2 card bg-base-300 rounded-box p-6">
              <h3 class="text-3xl text-fuchsia-300 text-center">Null Hypothesis</h3>
              <p class="text-center p-5">There are no identifiable work types where women are more outnumbered.</p>
              <p class="text-center p-5">Additionally, there is no significant relationship between certain factors (e.g. region, relationship with house head, educational attainment, etc.) and the gender gap between men and women in the labor force.</p>
            </div>
            
            <div class="flex flex-col h-80 w-1/2 card bg-base-300 rounded-box p-6">
              <h3 class="text-3xl text-fuchsia-300 text-center">Alternative Hypothesis</h3>
              <p class="text-center p-5">There are job types with a more prevalent gender gap, where women are significantly outnumbered and less likely to be found participating in.</p>
              <p class="text-center p-5">There are also identifiable factors that closely correlate with the gap between men and women in the labor force.</p>
            </div>
        </div>
        
        <h3 class="text-3xl py-2 font-medium text-center mt-10">What now?</h3>
        <p>Let us start with collecting the data we need, doing data exploration, then analyzing the relationships to look at factors affecting bias in recruitment, opportunities, and participation of women in the labor force. Once we see the results, we will be able to draw a conclusion.</p>
        <ul class="timeline timeline-vertical mt-8 mb-5">
            <li>
              <div class="timeline-start timeline-box outline">Data Collection</div>
              <div class="timeline-middle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
              </div>
              <hr/>
            </li>
            <li>
              <hr/>
              <div class="timeline-middle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
              </div>
              <div class="timeline-end timeline-box outline">Data Exploration</div>
              <hr/>
            </li>
            <li>
              <hr/>
              <div class="timeline-start timeline-box outline">Modelling</div>
              <div class="timeline-middle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
              </div>
              <hr/>
            </li>
            <li>
              <hr/>
              <div class="timeline-middle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
              </div>
              <div class="timeline-end timeline-box outline">Results</div>
              <hr/>
            </li>
            <li>
              <hr/>
              <div class="timeline-start timeline-box outline">Conclusion</div>
              <div class="timeline-middle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
              </div>
            </li>
          </ul>
    </div>
</html>

<style>
</style>


