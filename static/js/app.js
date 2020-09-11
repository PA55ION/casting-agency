document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
  
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
  
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
  
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
  
        });
      });
    }
  });


// COMMENT: PATCH Movies

// COMMENT: PATCH Actors
// COMMENT: POST movie
//COMEMENT: POST ACTORS
// COMMENT: authenticate and store token

// const postWeather = async (url = '', data = {}) => {
//   const response = await fetch(url, {
//           method: 'POST',
//           credentials: 'same-origin',
//           headers: {
//               'Content-Type': 'application/json'
//           },
//           body: JSON.stringify({
//               latitude: post.geonames[0].lat,
//               longitude: post.geonames[0].lng,
//               departure: leaving,
//               cityName: post.geonames[0].name,
//           })
//       }).then(res => res.json())
//       .then(data => {
//           console.log('post response:', data)
//           console.log(data);
//           updateUI(data)
//       }).catch(err => {
//           console.log('err', err)
//       })
// }

// const newMovie = async (e) => {
//   e.preventDefault()
//   const response = await fetch('/add_movies', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       // Authorization: `Bearer ${accessToken}`
//     },
//     body: JSON.stringify({
//       'title': document.getElementById('title').value,
//       'release_date': document.getElementById('release_date').value,
//       'description': document.getElementById('description').value,
//       'image_link': document.getElementById('image_link').value
//     })
   
//   }).then(() => window.location.href = "http://localhost:5000/movies")
// }

// const submitMovieBtn = document.getElementById('submit-movie');
// submitMovieBtn.addEventListener('click', () => {
//   newMovie()
// })
//COMMENT POST movie
document.getElementById("submit-movie").addEventListener("click", (e) => {
  e.preventDefault()
  const title = document.getElementById('title').value;
  const releaseDate = document.getElementById('release_date').value;
  const image_link = document.getElementById('image_link').value;
  const description = document.getElementById('description').value;
  
  console.log(title);
  console.log(releaseDate);
  console.log(description);
  if(!title || !releaseDate || !image_link || !description ) {
    alert('Please fill out all field');
  }  else {
    fetch('/add_movies', {
        method: 'POST',
        body: JSON.stringify({
            'title': title,
            'release_date': releaseDate,
            'image_link': image_link,
            'description': description,
        }),
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': 'Bearer ' + localStorage.token
        }
    })
    .then(function() {
      window.location.href = "http://localhost:5000/movies";
    });
  }
})

//POST ACTOR


