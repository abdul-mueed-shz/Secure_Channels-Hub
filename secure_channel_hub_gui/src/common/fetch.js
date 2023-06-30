/* eslint-disable */
const ver = "api/v1/";
const baseUrl =
  process.env.NODE_ENV === "development"
    ? "http://localhost:8000/" + ver
    : "" + ver;

export default async function ({
  endpoint = "",
  method = "POST",
  headers = {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  body = null,
  cache = "default",
}) {
  return await fetch(baseUrl + endpoint, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null,
    cache,
  });
}
