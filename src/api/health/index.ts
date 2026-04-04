// src/api/health/index.ts
// Health check endpoint implementation.
// Follows the principle of simplicity and single responsibility.

export const healthCheck = () => {
  return { status: 'ok', message: 'API is healthy' };
};