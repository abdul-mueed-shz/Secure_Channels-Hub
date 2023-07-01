const ver = "api/v1/";
export const baseUrl =
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
  try {
    const res = await fetch(baseUrl + endpoint, {
      method,
      headers,
      body: body ? JSON.stringify(body) : null,
      cache,
    });
    const jsonRes = await res.json();
    if (
      jsonRes["detail"] &&
      jsonRes["detail"].includes("credentials were not provided")
    ) {
      throw new Error(jsonRes["detail"]);
    }
    return jsonRes;
  } catch (err) {
    throw new Error(err);
  }
}
