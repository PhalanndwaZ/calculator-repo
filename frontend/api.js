// Change BASE_URL or adjust how endpoints are passed
const BASE_URL = "http://127.0.0.1:8000/api";

async function callApi(endpoint, method = "GET", data = null) {
    const body_object = {
        method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (data) {
        body_object.body = JSON.stringify(data);
    }

    const response = await fetch(BASE_URL + endpoint, body_object);
    const result = await response.json();

    if (!response.ok) {
        throw new Error(result.detail || "Something went wrong.");
    }

    return result;
}