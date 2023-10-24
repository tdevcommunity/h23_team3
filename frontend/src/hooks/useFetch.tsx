import { useState, useEffect } from "react";

const API_URL = process.env.API_URL;

export default function useFetch(endpoint: string) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(endpoint);
      const json = await response.json();
      setData(json);
    };
    fetchData();
  }, [endpoint]);

  return data;
}