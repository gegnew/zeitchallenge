
const API_URL = process.env.REACT_APP_API_URL;

export default async function client = (
    endpoint,
    {
      data,
      // accessToken,
      headers: customHeaders,
      ...customConfig
    }
) {
  const config = {
    method: data ? 'POST' : 'GET',
    body: data ? JSON.stringify(data) : undefined,
    headers: {
      // ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
      ...(data ? { 'Content-Type': 'application/json' } : {}),
      ...customHeaders,
    },
    ...customConfig,
  };

  return window.fetch(API_URL + endpoint, config).then(async response => {
    if (response.status === 401) {
      return Promise.reject(new Error('Please re-authenticate.'));
    }

    const responseData = await response.json();
    if (response.ok) {
      return responseData;
    }

    return Promise.reject(data);
  });
}
