<script>
    import bg from "$lib/assets/bg.png";
    import bg2 from "$lib/assets/bg2.png";
    import bg3 from "$lib/assets/bg3.png";
    import bg4 from "$lib/assets/bg4.png";
    import bg5 from "$lib/assets/bg5.png";
    import { onMount } from 'svelte';

    let scrollY = 0;

    onMount(() => {
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    });

    function handleScroll() {
        scrollY = window.scrollY;
        updateParallax();
    }

    function updateParallax() {
        document.querySelector('.bg').style.transform = `translateY(${scrollY * 0.9}px)`;
        document.querySelector('.bg2').style.transform = `translateY(${scrollY * 0.6}px)`;
        document.querySelector('.bg3').style.transform = `translateY(${scrollY * 0.4}px)`;
        document.querySelector('.bg4').style.transform = `translateY(${scrollY * 0.2}px)`;
    }
</script>

<html lang='en'>
    <div class='parallax'>
        <div class="bg mt-5">
            <img src={bg} alt="background1" width="100%" height="auto">
        </div>
        <div class="bg2">
            <img src={bg2} alt="background2" width="100%" height="auto">
        </div>
        <div class="bg3">
            <img src={bg3} alt="background3" width="100%" height="auto">
        </div>
        <div class="bg4">
            <img src={bg4} alt="background4" width="100%" height="auto">
        </div>
        <div class="bg5">
            <img src={bg5} alt="background5" width="100%" height="auto">
        </div>
    </div>
    <div class="spacer"></div>
</html>

<style>
    .spacer {
        width: 100%;
        height: 25vh;
        z-index: -1;
    }
    .parallax {
        position: relative;
        top: 20px;
        width: 100%;
        height: 100vh;
        overflow: hidden;
        z-index: -1;
    }
    .parallax div {
        height: 100%;
        width: 100%; 
        position: absolute;
        left: 0;
        top: 0;
        z-index: -1;
    }
    .parallax img {
        height: 100%;
        width: 100%;
        object-fit: contain;
        z-index: -1;
    }
</style>


