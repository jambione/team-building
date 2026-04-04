// Health check endpoint for API service
export const healthCheck = () => {
  return { status: 'ok', message: 'API is healthy' };
};
