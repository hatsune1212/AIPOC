import axios from "axios";

export const apiClient = axios.create({
  baseURL: "/api",
  timeout: 15000
});

// TODO: add auth headers, tenant scoping, and error handling in later tickets.
