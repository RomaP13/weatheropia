function submitForm() {
  var searchInput = document.getElementById("searchInput");
  var city = searchInput.value.trim();

  if (city) {
    window.location.href = "/?city=" + city;
  }

  return false;
}