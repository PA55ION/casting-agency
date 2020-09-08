let auth0 = null
// import createAuth0Client from "auth0/auth0-spa-js";
const configureClient = async () => {
    auth0 = await createAuth0Client({
    domain: "dev-ys0-cxsi.us.auth0.com",
    client_id: "Er4ULFDP3EJpPh3Ds6Pu1kgNGN6yI2mz",
    cacheLocation: 'localstorage'
  });
};

const updateUI = async () => {
  const isAuthenticated = await auth0.isAuthenticated();

  document.getElementById("btn-logout").disabled = !isAuthenticated;
  document.getElementById("movies").disabled = isAuthenticated;
  document.getElementById("login").disabled = isAuthenticated;

  if(isAuthenticated) {
      document.getElementById('gate-content').classList.remove('hidden')
  }
  else {
    document.getElementById("gated-content").classList.add("hidden");
  }
};

window.onload = async () => {
  await configureClient();
  updateUI();

  const query = window.location.search;
  if (query.includes("code=") && query.includes("state=")) {
    // Process the login state
    await auth0.handleRedirectCallback();
    updateUI();
    // Use replaceState to redirect the user away and remove the querystring parameters
    window.history.replaceState({}, document.title, "/");
  }
};

const login = async () => {
    document.getElementById("login").addEventListener("click", async () => {
        await auth0.loginWithRedirect({
          redirect_uri: 'http://127.0.0.1:5000/'
        });
        const user = await auth0.getUser();
        console.log(user);
      });
};

login()

const logout = async () => {
    document.getElementById('logout').addEventListener('click', () => {
        auth0.logout();
    })
}
