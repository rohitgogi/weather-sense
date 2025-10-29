const btn = document.getElementById("searchBtn");
const input = document.getElementById("cityInput");
const resultDiv = document.getElementById("result");

btn.addEventListener("click", async () => {
  const city = input.value.trim();
  if (!city) {
    resultDiv.innerHTML = "Please enter a city.";
    return;
  }

  resultDiv.innerHTML = "Loading...";

  try {
    const response = await fetch(`http://127.0.0.1:8000/weather?city=${city}`);
    if (!response.ok) throw new Error("City not found");

    const data = await response.json();
    resultDiv.innerHTML = `
      <h2>${data.city}</h2>
      <p><strong>Temperature:</strong> ${data.temperature}°C</p>
      <p><strong>Windspeed:</strong> ${data.windspeed} km/h</p>
      <p><strong>Condition:</strong> ${data.description}</p>
      <p><small>Updated at: ${data.time}</small></p>
    `;
  } catch (err) {
    resultDiv.innerHTML = `Error: ${err.message}`;
  }
});
