
  
/* const facts = document.querySelectorAll('.fact');
let currentFact = 0;
let nextFact = 1;
let prevFact = facts.length - 1;

setInterval(() => {
  facts[currentFact].classList.remove('active');
  facts[nextFact].classList.add('next');
  facts[prevFact].classList.add('prev');

  setTimeout(() => {
    facts[nextFact].classList.remove('next');
    facts[prevFact].classList.remove('prev');
    facts[currentFact].classList.add('active');

    currentFact = (currentFact + 1) % facts.length;
    nextFact = (nextFact + 1) % facts.length;
    prevFact = (prevFact + 1) % facts.length;
  }, 1000);
}, 5000);*/

$(document).ready(function(){
  $('.news-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true, // enable autoplay
    autoplaySpeed: 3000, // set autoplay speed to 5 seconds
    dots: true,
    arrows: false
  });
  
});
  

// Select all the fact elements
const facts = document.querySelectorAll('.fact');

// Set the index of the current, next and previous fact
let currentFact = 0;
let nextFact = 1;
let prevFact = facts.length - 1;

// Function to switch to the next fact
function switchToNextFact() {
  // Remove the active class from the current fact
  facts[currentFact].classList.remove('active');
  // Add the next class to the next fact
  facts[nextFact].classList.add('next');
  // Add the prev class to the previous fact
  facts[prevFact].classList.add('prev');

  // Set a timeout to remove the next and prev classes and add the active class
  setTimeout(() => {
    // Remove the next class from the next fact
    facts[nextFact].classList.remove('next');
    // Remove the prev class from the previous fact
    facts[prevFact].classList.remove('prev');
    // Add the active class to the current fact
    facts[currentFact].classList.add('active');

    // Update the index of the current, next and previous fact
    currentFact = (currentFact + 1) % facts.length;
    nextFact = (nextFact + 1) % facts.length;
    prevFact = (prevFact + 1) % facts.length;
  }, 1000);
}

// Set an interval to switch to the next fact every 5 seconds
setInterval(switchToNextFact, 5000);

// Loop through each fact element and add event listeners
facts.forEach((fact) => {
  fact.addEventListener('mouseover', (e) => {
    // Get the icon element and rotate it
    const icon = e.currentTarget.querySelector('.fact-icon');
    icon.style.transform = 'rotate(360deg)';

    // Get the title and text elements and fade them in
    const title = e.currentTarget.querySelector('.fact-title');
    title.style.opacity = '1';
    title.style.transform = 'translateY(-10px)';
    const text = e.currentTarget.querySelector('.fact-text');
    text.style.opacity = '0';
    text.style.transform = 'translateY(10px)';
    setTimeout(() => {
      text.style.opacity = '1';
      text.style.transform = 'translateY(0)';
    }, 200);

  });

  fact.addEventListener('mouseleave', (e) => {
    // Get the icon element and rotate it back to the original position
    const icon = e.currentTarget.querySelector('.fact-icon');
    icon.style.transform = 'rotate(0deg)';

    // Get the title and text elements and fade them out
    const title = e.currentTarget.querySelector('.fact-title');
    title.style.opacity = '0';
    title.style.transform = 'translateY(0px)';
    const text = e.currentTarget.querySelector('.fact-text');
    text.style.opacity = '0';
    text.style.transform = 'translateY(10px)';
  });
});

// Animate the facts when the page loads
// Animate the facts when the page loads
window.addEventListener('load', () => {
  let delay = 0;
  facts.forEach((fact) => {
    // Add a random rotation to the fact icon
    const icon = fact.querySelector('.fact-icon');
    const randomRotation = Math.floor(Math.random() * 360);
    icon.style.transform = `rotate(${randomRotation}deg)`;

    // Add the animate class to the fact element
    setTimeout(() => {
      fact.classList.add('animate');
    }, delay);
    delay += 200;
  });
});


const boxes = document.querySelectorAll('.box-container');
boxes.forEach(box => {
  box.addEventListener('mouseover', () => {
    box.classList.add('animate');
  });

  box.addEventListener('mouseleave', () => {
    box.classList.remove('animate');
  });
});
