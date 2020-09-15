document.addEventListener("DOMContentLoaded", () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach((el) => {
      el.addEventListener("click", () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle("is-active");
        $target.classList.toggle("is-active");
      });
    });
  }
});

// COMMENT: PATCH Movies

// COMMENT: PATCH Actors
// COMMENT: POST movie
//COMEMENT: POST ACTORS
// COMMENT: authenticate and store token

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

// document.addEventListener('DOMContentLoaded', () => {

function addMovie() {
  const submitMovieBtn = document.getElementById("submit-movie");
  if (submitMovieBtn) {
    submitMovieBtn.addEventListener("click", function (e) {
      e.preventDefault();
      const title = document.getElementById("title").value;
      const releaseDate = document.getElementById("release_date").value;
      const image_link = document.getElementById("image_link").value;
      const description = document.getElementById("description").value;

      if (!title || !releaseDate || !image_link || !description) {
        alert("Please fill out all field");
      } else {
        fetch("/add_movies", {
          method: "POST",
          body: JSON.stringify({
            title: title,
            release_date: releaseDate,
            image_link: image_link,
            description: description,
          }),
          headers: {
            "Content-Type": "application/json",
            // 'Authorization': 'Bearer ' + localStorage.token
          },
        }).then(function () {
          setTimeout(() => {
            alert("Movie success fully added");
          }, 3000);
          window.location.href = "http://localhost:5000/movies";
        });
      }
    });
  }
}
addMovie();

//POST ACTOR
function addActor() {
  const submitActorBtn = document.getElementById("submit-actor");
  if (submitActorBtn) {
    submitActorBtn.addEventListener("click", function (e) {
      e.preventDefault();
      const name = document.getElementById("actor_name").value;
      const age = document.getElementById("age").value;
      const gender = document.getElementById("gender").value;
      const image_link = document.getElementById("image_link").value;
      console.log(name);
      console.log(gender);
      console.log(age);
      fetch("/add_actors", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          age: age,
          gender: gender,
          image_link: image_link,
        }),
      }).then(() => {
        setTimeout(() => {
          alert("Actor successfully added");
        }, 1500);
        window.location.href = "http://localhost:5000/actors";
      });
    });
  }
}
addActor();

function deleteModel() {
  const deleteBtn = document.querySelectorAll("#delete-actor");
  for (let i = 0; i < deleteBtn.length; i++) {
    const btn = deleteBtn[i];
    btn.onclick = function (e) {
      const modelId = e.target.dataset["id"];
      console.log("Delete button was click", modelId);
      fetch(`/actors/${modelId}`, {
        method: "DELETE",
      })
        .then(() => {
          window.location.href = "/actors";
        })
        .catch((e) => {
          console.log("error", e);
        });
    };
  }
}
deleteModel();

//close btn on flash message

document.addEventListener('DOMContentLoaded', () => {
  (document.querySelectorAll('.notification, .delete') || []).forEach(($delete) => {
    $notification = $delete.parentNode;
    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    })
  })
})

//delete model
function deleteMovie() {
  const deleteBtn = document.querySelectorAll('#delete-movie');
  for(let i = 0; i < deleteBtn.length; i++) {
    const btn = deleteBtn[i];
    btn.onclick = function(e) {
      const movieId = e.target.dataset['id'];
      console.log('Button was click: ', movieId);
      fetch(`/movies/${movieId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
           // 'Authorization': 'Bearer ' + localStorage.token
        },
      })
      .then(() => {
        window.location.href = '/movies';
      })
      .catch((e) => {
        console.log('err', e)
      })
    }
  }
}
deleteMovie();