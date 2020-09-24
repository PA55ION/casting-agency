
//     auth0 = await createAuth0Client({
//     domain: 'dev-ys0=cxsi.us.auth0.com',
//     client_id: 'Er4ULFDP3EJpPh3Ds6Pu1kgNGN6yI2mz',
//     audience: "casting-agency",
//     redirect_uri: "http://localhost:5000",
//     cacheLocation: 'localstorage'
//   });
// };


// const updateUI = async () => {
//   const isAuthenticated = await auth0.isAuthenticated();

//   document.getElementById("logout").disabled = !isAuthenticated;
//   document.getElementById("login").disabled = isAuthenticated;

//   if(isAuthenticated) {
//       document.getElementById('gate-content').classList.remove('hidden')
//   }
//   else {
//     // document.getElementById("gated-content").classList.add("hidden");
//   }
// };

// window.onload = async () => {
//   await configureClient();
//   updateUI();

//   const query = window.location.search;
//   if (query.includes("code=") && query.includes("state=")) {
//     // Process the login state
//     await auth0.handleRedirectCallback();
//     updateUI();
//     // Use replaceState to redirect the user away and remove the querystring parameters
//     window.history.replaceState({}, document.title, "/");
//   }
// };


//     document.getElementById("login").addEventListener("click", async () => {
//         await auth0.loginWithRedirect({
//           redirect_uri: 'http://localhost:5000'
//         });
//         const user = await auth0.getUser();
//         console.log(user);
//       });

// // const login = async () => {
//     // document.getElementById("login").addEventListener("click", async () => {
//     //     await auth0.loginWithRedirect({
//     //       redirect_uri: 'http://127.0.0.1:5000/'
//     //     });
//     //     const user = await auth0.getUser();
//     //     console.log(user);
//     //   });
// // };


// const logout = async () => {
//     document.getElementById('logout').addEventListener('click', () => {
//         auth0.logout();
//     })
// }



// (async () => {
//   var lock = new Auth0Lock(
//       // These properties are set in auth0-variables.js
//       AUTH0_CLIENT_ID,
//       AUTH0_DOMAIN,
      
//   );


//   var userProfile;

//   document.getElementById('login').addEventListener('click', function() {
//     lock.show(function(err, profile, token) {
//       if (err) {
//         // Error callback
//         console.error("Something went wrong: ", err);
//         alert("Something went wrong, check the Console errors");
//       } else {
//         // Success calback

//         // Save the JWT token.
//         localStorage.setItem('userToken', token);

//         // Save the profile
//         userProfile = profile;
//         if(!userProfile)
//         document.getElementById("logout").classList.add = hidden;
//         document.getElementById("login").classList.remove = hidden;
//       }
//     });
//   });


//   // document.getElementById('btn-api').addEventListener('click', function() {
//   //     // Just call your API here. The header will be sent
//   // })
// })();
let userToken = window.location.href.match(/\#(?:access_token)\=([\S\s]*?)\&/);
let permissions;

if (userToken) {
  localStorage.setItem('token', userToken[1]);
  permissions = JSON.parse(atob(userToken[1].split('.')[1])).permissions;
  localStorage.setItem('permissions', permissions)
}

const updateUI = async () => {


  document.getElementById("logout").disabled = !userToken;
  document.getElementById("login").disabled = userToken;

  if(userToken) {
      document.getElementById('gate-content').classList.remove('hidden')
  }
  else {
    document.getElementById("gated-content").classList.add("hidden");
  }
};




