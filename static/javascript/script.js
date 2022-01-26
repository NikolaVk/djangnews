function initClock() {
    let hourHand = document.createElement('div');
    let minuteHand = document.createElement('div');
    let secondHand = document.createElement('div');
    let clockTime = document.createElement('div');
    let clockDate = document.createElement('div');
    let clock_element = document.getElementById('id_clock');

    if (clock_element) {

        clockTime.appendChild(hourHand);
        clockTime.appendChild(minuteHand);
        clockTime.appendChild(secondHand);
        clockTime.className = 'clock_time';
        clockDate.className = 'clock_date';
        clock_element.appendChild(clockTime);
        clock_element.appendChild(clockDate);
        hourHand.className = 'clock_hourhand';
        minuteHand.className = 'clock_minutehand';
        secondHand.className = 'clock_secondhand';

        let hourHandWidth = (clock_element.clientWidth * 0.04);
        let hourHandLength = (clock_element.clientWidth * 0.4);
        let minuteHandWidth = (clock_element.clientWidth * 0.03);
        let minuteHandLength = (clock_element.clientWidth * 0.45);
        let secondHandWidth = (clock_element.clientWidth * 0.025);
        let secondHandLength = (clock_element.clientWidth * 0.47);


        clockTime.style.width = clock_element.clientWidth + 'px';
        clockTime.style.height = clock_element.clientWidth + 'px';
        hourHand.style.width = hourHandWidth + 'px';
        hourHand.style.height = hourHandLength + 'px';
        hourHand.style.left = ((clock_element.clientWidth - hourHandWidth) / 2) + 'px';
        hourHand.style.top = ((clock_element.clientWidth / 2)) + 'px';
        hourHand.style.transformOrigin = '50% 0%';
        minuteHand.style.width = minuteHandWidth + 'px';
        minuteHand.style.height = minuteHandLength + 'px';
        minuteHand.style.transformOrigin = '50% 0%';
        minuteHand.style.left = ((clock_element.clientWidth - minuteHandWidth) / 2) + 'px';
        minuteHand.style.top = ((clock_element.clientWidth / 2)) + 'px';
        secondHand.style.width = secondHandWidth + 'px';
        secondHand.style.height = secondHandLength + 'px';
        secondHand.style.transformOrigin = '50% 0%';
        secondHand.style.left = ((clock_element.clientWidth - secondHandWidth) / 2) + 'px';
        secondHand.style.top = ((clock_element.clientWidth / 2)) + 'px';


        let currentTime = new Date();

        let hourFracts = (parseFloat(currentTime.getHours())) + (parseFloat(currentTime.getMinutes()) / 60);
        hourHand.style.transform = 'rotate(' + ((((hourFracts + 6) % 12) * 360) / 12) + 'deg)';
        minuteHand.style.transform = 'rotate(' + ((((currentTime.getMinutes() + 30) % 60) * 360) / 60) + 'deg)';
        secondHand.style.transform = 'rotate(' + ((((currentTime.getSeconds() + 30) % 60) * 360) / 60) + 'deg)';
        clockDate.innerHTML = currentTime.toLocaleDateString('en-uk');
        clock_element.style.height = (clockDate.clientWidth + clockDate.clientHeight) + 'px';

        setInterval(function() {
                let currentTime = new Date();
                let hourFracts = (parseFloat(currentTime.getHours())) + (parseFloat(currentTime.getMinutes()) / 60);
                hourHand.style.transform = 'rotate(' + ((((hourFracts + 6) % 12) * 360) / 12) + 'deg)';
                minuteHand.style.transform = 'rotate(' + ((((currentTime.getMinutes() + 30) % 60) * 360) / 60) + 'deg)';
                secondHand.style.transform = 'rotate(' + ((((currentTime.getSeconds() + 30) % 60) * 360) / 60) + 'deg)';
                clockDate.innerHTML = currentTime.toLocaleDateString('en-uk');
                clock_element.style.height = (clockDate.clientWidth + clockDate.clientHeight) + 'px';
            },
            1000);

    }

}